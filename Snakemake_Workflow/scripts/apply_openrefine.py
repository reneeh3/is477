import pandas as pd
import json

input_path = snakemake.input.data
operations_path = snakemake.input.operations
output_path = snakemake.output[0]

df = pd.read_csv(input_path)

with open(operations_path, "r") as f:
    operations = json.load(f)

for op in operations:
    if op.get("op") == "core/mass-edit":
        col = op.get("columnName")
        if col not in df.columns:
            continue
        for edit in op.get("edits", []):
            for old_val in edit.get("from", []):
                df[col] = df[col].replace(old_val, edit["to"])

df.to_csv(output_path, index=False)
print(f"OpenRefine operations applied. Output saved to {output_path}")
