import pandas as pd
import os

os.makedirs("results", exist_ok=True)

moma = pd.read_csv("results/final_moma.csv", low_memory=False)
met = pd.read_csv("results/final_met.csv", low_memory=False)

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

combined.to_csv("results/combined_moma_met.csv", index=False)

print("Combined dataset created")
print(combined.shape)
print(combined["source"].value_counts())
