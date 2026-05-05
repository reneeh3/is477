import pandas as pd
import os

os.makedirs("results", exist_ok=True)

# Load cleaned datasets
moma = pd.read_csv("results/moma_snakefile_cleaned.csv")
met = pd.read_csv("results/met_snakefile_cleaned.csv")

# Add source labels
moma["source"] = "MoMA"
met["source"] = "MET"

# Combine
combined = pd.concat([moma, met], ignore_index=True)

# Save
combined.to_csv("results/combined_moma_met.csv", index=False)

print("Combined dataset created")
