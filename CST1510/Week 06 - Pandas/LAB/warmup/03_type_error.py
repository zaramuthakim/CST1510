import pandas as pd

df = pd.DataFrame({"value": ["87", "120", "45"], "limit": [100, 100, 100]})

# Convert the 'value' column to numeric before calculating
df["value"] = pd.to_numeric(df["value"])

df["percent"] = (df["value"] / df["limit"]) * 100

print(df)