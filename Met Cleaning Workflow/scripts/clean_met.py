import pandas as pd
import numpy as np
import re

ARTISTS_FILE = "data/artists.txt"
ARTWORKS_FILE = "data/artworks.txt"

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

def clean_nationality(val):
    if pd.isna(val):
        return np.nan
    val = str(val).strip().strip("()").split(",")[0].strip()
    if val in ("", "nan", "None"):
        return np.nan
    return NATIONALITY_MAP.get(val, val)

def standardize_gender(val):
    if pd.isna(val):
        return np.nan
    val = str(val).strip().strip("()").lower()
    if val in ("male", "man", "m"):
        return "Male"
    if val in ("female", "woman", "f"):
        return "Female"
    if val in ("non-binary", "nonbinary", "non binary"):
        return "Non-Binary"
    return np.nan

def extract_year(val):
    if pd.isna(val):
        return np.nan
    match = re.search(r"\b(1[0-9]{3}|20[0-2][0-9])\b", str(val))
    return int(match.group()) if match else np.nan

def main():
    artists = pd.read_csv(ARTISTS_FILE, sep="\t")
    artworks = pd.read_csv(ARTWORKS_FILE, sep="\t")

    artists.columns = artists.columns.str.strip().str.lower().str.replace(" ", "_")
    artworks.columns = artworks.columns.str.strip().str.lower().str.replace(" ", "_")

    for col in ("displayname", "nationality", "gender"):
        if col in artists.columns:
            artists[col] = artists[col].astype("string").str.strip()

    for col in ("title", "date"):
        if col in artworks.columns:
            artworks[col] = artworks[col].astype("string").str.strip()

    artists["constituentid"] = artists["constituentid"].astype("string").str.strip()
    artworks["constituentid"] = artworks["constituentid"].astype("string").str.strip()
    artworks["objectid"] = artworks["objectid"].astype("string").str.strip()

    artists["begindate"] = pd.to_numeric(artists["begindate"], errors="coerce").replace(0, np.nan)
    artists["enddate"] = pd.to_numeric(artists["enddate"], errors="coerce").replace(0, np.nan)

    artists["nationality"] = artists["nationality"].apply(clean_nationality)
    artists["gender"] = artists["gender"].apply(standardize_gender)

    if "year_created" not in artworks.columns:
        artworks["year_created"] = artworks["date"].apply(extract_year)
    else:
        artworks["year_created"] = pd.to_numeric(artworks["year_created"], errors="coerce")

    artists = artists.drop_duplicates(subset="constituentid")

    artist_lookup = artists[[
        "constituentid",
        "displayname",
        "nationality",
        "gender",
        "begindate",
        "enddate"
    ]].rename(columns={
        "constituentid": "artist_constituentid",
        "displayname": "artist_name",
        "nationality": "artist_nationality",
        "gender": "artist_gender",
        "begindate": "artist_birthyear",
        "enddate": "artist_deathyear",
    })

    df = artworks.merge(
        artist_lookup,
        left_on="constituentid",
        right_on="artist_constituentid",
        how="left"
    )

    df["nationality_clean"] = df["artist_nationality"]
    df["gender_clean"] = df["artist_gender"]

    df = (
        df.dropna(subset=["objectid", "accessionnumber"], how="all")
          .drop_duplicates()
          .drop_duplicates(subset=["objectid", "artist_constituentid"])
          .reset_index(drop=True)
    )

    print(df.shape)
    print(df.duplicated().sum())
    print(df["nationality_clean"].value_counts().head(10))
    print(df[["objectid", "artist_constituentid", "nationality_clean", "gender_clean"]].isna().sum())

    df.to_csv(snakemake.output[0], index=False)
