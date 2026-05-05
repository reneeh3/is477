import pandas as pd

moma = pd.read_csv(snakemake.input.moma)
met = pd.read_csv(snakemake.input.met)

moma["source"] = "MoMA"
met["source"] = "MET"

combined = pd.concat([moma, met], ignore_index=True)
combined.to_csv(snakemake.output[0], index=False)
print("Combined dataset created")
