import pandas as pd

df = pd.read_csv("sample.csv", dtype={"Phone": str})

# Missing values bharo
df["Email"] = df["Email"].fillna("Not Provided")
df["Phone"] = df["Phone"].fillna("Not Provided")
df["City"] = df["City"].fillna("Unknown")

# Duplicate rows hatao
df = df.drop_duplicates()

print("\n--- SHAPE AFTER DEDUP ---")
print(df.shape)

# Extra spaces hatao
df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()

# Capitalization fix karo
df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()

# Capitalization ke baad dobara duplicate check
df = df.drop_duplicates()

print("\n--- FINAL SHAPE ---")
print(df.shape)

print(df)
print("\n--- MISSING AFTER ---")
print(df.isnull().sum())

# Clean data save karo
df.to_csv("cleaned.csv", index=False)
print("\n✅ Cleaned data saved to cleaned.csv")
