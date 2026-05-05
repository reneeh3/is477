# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import re

# FILE PATH
MET_FILE = "data/MetObjects_small.csv"

# NATIONALITY MAPPING
NATIONALITY_MAP = {
    "American": "American", "United States": "American", "USA": "American", "US": "American",
    "British": "British", "English": "British", "Scottish": "British", "Welsh": "British", "UK": "British",
    "German": "German", "West German": "German", "East German": "German",
    "French": "French", "Italian": "Italian", "Spanish": "Spanish",
    "Japanese": "Japanese", "Chinese": "Chinese",
    "Russian": "Russian", "Soviet": "Russian",
    "Dutch": "Dutch", "Swedish": "Swedish", "Swiss": "Swiss", "Austrian": "Austrian", "Belgian": "Belgian",
    "Brazilian": "Brazilian", "Mexican": "Mexican", "Argentine": "Argentine", "Argentinian": "Argentine",
    "Canadian": "Canadian",
}

# CLEANING FUNCTIONS
def clean_nationality(val):
    if pd.isna(val):
        return np.nan
    val = str(val).strip().strip("()").split(",")[0].strip()
    if val in ("", "nan", "None", "None|", "|"):
        return np.nan
    return NATIONALITY_MAP.get(val, val)


def extract_year(val):
    if pd.isna(val):
        return np.nan
    match = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", str(val))
    return int(match.group()) if match else np.nan


# MAIN CLEANING PIPELINE
def main():

    # Load dataset
    met = pd.read_csv(snakemake.input[0], low_memory=False)

    # Standardize column names
    met.columns = (
        met.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Clean text columns
    for col in met.select_dtypes(include="object").columns:
        met[col] = met[col].astype("string").str.strip()

    # Rename columns to match project schema
    met = met.rename(columns={
        "object_id": "objectid",
        "object_number": "accessionnumber",
        "artist_display_name": "artist_name",
        "artist_nationality": "nationality_clean",
        "artist_begin_date": "artist_birthyear",
        "artist_end_date": "artist_deathyear",
        "object_date": "date"
    })

    # Extract year fields
    met["artist_birthyear"] = met["artist_birthyear"].apply(extract_year)
    met["artist_deathyear"] = met["artist_deathyear"].apply(extract_year)
    met["year_created"] = met["date"].apply(extract_year)

    # Clean nationality values
    met["nationality_clean"] = met["nationality_clean"].apply(clean_nationality)

    # Select final columns
    final = met[[
        "title",
        "artist_name",
        "artist_birthyear",
        "artist_deathyear",
        "nationality_clean"
    ]].copy()

    # Remove incomplete rows
    final = final.dropna(subset=[
        "title",
        "artist_name",
        "artist_birthyear",
        "nationality_clean"
    ])

    # Remove duplicates
    final = final.drop_duplicates().reset_index(drop=True)

    # Print summary statistics
    print("Final dataset shape:", final.shape)
    print("\nTop nationalities:")
    print(final["nationality_clean"].value_counts().head(10))
    print("\nMissing values:")
    print(final.isna().sum())

    # Save output
    try:
        output_path = snakemake.output[0]
    except NameError:
        output_path = "results/met_snakefile_cleaned.csv"

    final.to_csv(output_path, index=False)
    print("\nSaved to:", output_path)
main()
