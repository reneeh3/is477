import pandas as pd
import matplotlib.pyplot as plt


# =========================
# LOAD DATA
moma = pd.read_csv("final_moma.csv", low_memory=False)
met = pd.read_csv("final_met.csv", low_memory=False)

print("MoMA columns:")
print(moma.columns.tolist())

print("\nMET columns:")
print(met.columns.tolist())


# =========================
# STANDARDIZE AND COMBINE DATASETS
# =========================
columns = [
    "title",
    "artist_name",
    "artist_birthyear",
    "artist_deathyear",
    "nationality_clean"
]

moma = moma[columns].copy()
met = met[columns].copy()

moma["source"] = "MoMA"
met["source"] = "MET"

combined = pd.concat([moma, met], ignore_index=True)

print("\nCombined dataset shape:")
print(combined.shape)

print("\nRecords by museum:")
print(combined["source"].value_counts())

combined.to_csv("combined_moma_met.csv", index=False)


# =========================
# DATA QUALITY: MISSINGNESS
print("\n=== MISSINGNESS SUMMARY ===")

missing = (
    combined
    .isna()
    .mean()
    .sort_values(ascending=False)
)

print(missing)


# =========================
# VISUALIZATION 1:
# NATIONALITY PROPORTIONS BY MUSEUM
nationality_df = combined.dropna(subset=["nationality_clean"]).copy()

top_nationalities = (
    nationality_df["nationality_clean"]
    .value_counts()
    .head(10)
    .index
)

nationality_df = nationality_df[
    nationality_df["nationality_clean"].isin(top_nationalities)
]

nationality_counts = (
    nationality_df
    .groupby(["source", "nationality_clean"])
    .size()
    .reset_index(name="count")
)

nationality_counts["proportion"] = (
    nationality_counts
    .groupby("source")["count"]
    .transform(lambda x: x / x.sum())
)

nationality_plot = (
    nationality_counts
    .pivot(
        index="nationality_clean",
        columns="source",
        values="proportion"
    )
    .fillna(0)
)

nationality_plot.plot(kind="bar", figsize=(12, 6))
plt.title("Nationality Proportions by Museum")
plt.xlabel("Nationality")
plt.ylabel("Proportion")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# =========================
# VISUALIZATION 2:
# REPRESENTATION OVER TIME
time_df = combined.dropna(
    subset=["artist_birthyear", "nationality_clean"]
).copy()

time_df["artist_birthyear"] = pd.to_numeric(
    time_df["artist_birthyear"],
    errors="coerce"
)

time_df = time_df.dropna(subset=["artist_birthyear"])
time_df["artist_birthyear"] = time_df["artist_birthyear"].astype(int)

time_df = time_df[
    (time_df["artist_birthyear"] >= 1500) &
    (time_df["artist_birthyear"] <= 2026)
]

top_trend_nats = (
    time_df["nationality_clean"]
    .value_counts()
    .head(6)
    .index
)

time_df = time_df[
    time_df["nationality_clean"].isin(top_trend_nats)
]

time_df["decade"] = (time_df["artist_birthyear"] // 10) * 10

trend_counts = (
    time_df
    .groupby(["source", "decade", "nationality_clean"])
    .size()
    .reset_index(name="count")
)

for museum_name in trend_counts["source"].unique():
    subset = trend_counts[trend_counts["source"] == museum_name]

    pivot = (
        subset
        .pivot(
            index="decade",
            columns="nationality_clean",
            values="count"
        )
        .fillna(0)
    )

    pivot.plot(figsize=(12, 6))
    plt.title(f"Artist Birth-Year Trends by Nationality - {museum_name}")
    plt.xlabel("Artist Birth Decade")
    plt.ylabel("Number of Artwork Records")
    plt.tight_layout()
    plt.show()


# =========================
# GENERAL SUMMARY TABLES
print("\n=== TOP PROPORTIONS OF NATIONALITIES BY MUSEUM ===")

top_by_museum = (
    combined
    .dropna(subset=["nationality_clean"])
    .groupby("source")["nationality_clean"]
    .value_counts(normalize=True)
    .mul(100)
    .round(3)
    .rename("Percent")
    .reset_index()
)

print(top_by_museum.groupby("source").head(10))


print("\n=== TOP NATIONALITIES OVERALL: BOTH MUSEUMS ===")

top_overall = (
    combined["nationality_clean"]
    .value_counts(dropna=False)
    .head(15)
)

print(top_overall)
)
