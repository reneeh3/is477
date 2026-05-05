import pandas as pd
import numpy as np
import re

ARTISTS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/43399bad2fad626a0750ab6801ced6f1e83b0a41/Artists.csv"
ARTWORKS_URL = "https://media.githubusercontent.com/media/MuseumofModernArt/collection/a46be68e826552737fce8152b002dcd603c0a300/Artworks.csv"

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
    if match:
        return int(match.group())
    return np.nan


def parse_ids(val):
    if pd.isna(val):
        return []
    return [int(x) for x in re.findall(r"\d+", str(val))]


def main():
    artists = pd.read_csv(ARTISTS_URL)
    artworks = pd.read_csv(ARTWORKS_URL, low_memory=False)

    artists.columns = artists.columns.str.strip().str.lower().str.replace(" ", "_")
    artworks.columns = artworks.columns.str.strip().str.lower().str.replace(" ", "_")

    for col in ("displayname", "nationality", "gender"):
        if col in artists.columns:
            artists[col] = artists[col].astype("string").str.strip()

    artists["constituentid"] = pd.to_numeric(artists["constituentid"], errors="coerce")
    artists[["begindate", "enddate"]] = (
        artists[["begindate", "enddate"]]
        .apply(pd.to_numeric, errors="coerce")
        .replace(0, np.nan)
    )

    artists["nationality"] = artists["nationality"].apply(clean_nationality)
    artists["gender"] = artists["gender"].apply(standardize_gender)
    artists = artists.drop_duplicates(subset="constituentid")

    for col in ("title", "artist", "nationality", "gender"):
        if col in artworks.columns:
            artworks[col] = artworks[col].astype("string").str.strip()

    artworks["objectid"] = pd.to_numeric(artworks["objectid"], errors="coerce")
    artworks["nationality"] = artworks["nationality"].apply(clean_nationality)
    artworks["gender"] = artworks["gender"].apply(standardize_gender)
    artworks["year_created"] = artworks["date"].apply(extract_year)
    artworks["year_acquired"] = pd.to_datetime(artworks["dateacquired"], errors="coerce").dt.year

    artworks["constituentid_list"] = artworks["constituentid"].apply(parse_ids)
    artworks = artworks.explode("constituentid_list")
    artworks["constituentid_list"] = pd.to_numeric(artworks["constituentid_list"], errors="coerce")

    artist_lookup = artists[["constituentid", "displayname", "nationality", "gender", "begindate", "enddate"]].rename(
        columns={
            "constituentid": "artist_constituentid",
            "displayname": "artist_name",
            "nationality": "artist_nationality",
            "gender": "artist_gender",
            "begindate": "artist_birthyear",
            "enddate": "artist_deathyear",
        }
    )

    df = artworks.merge(
        artist_lookup,
        left_on="constituentid_list",
        right_on="artist_constituentid",
        how="left",
    )

    df["nationality_clean"] = df["artist_nationality"].combine_first(df["nationality"])
    df["gender_clean"] = df["artist_gender"].combine_first(df["gender"])

    df = (df.dropna(subset=["objectid", "accessionnumber"], how="all").drop_duplicates().drop_duplicates(subset=["objectid", "artist_constituentid"]).reset_index(drop=True))

    print(df.shape)
    print(df.duplicated().sum())

    print(df["nationality_clean"].value_counts().head(10))
    print(df[["objectid", "artist_constituentid", "nationality_clean", "gender_clean"]].isna().sum())

df.to_csv(snakemake.output[0], index=False)
