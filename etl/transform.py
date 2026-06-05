import pandas as pd

# Read extracted CSV file
df = pd.read_csv("../data/cleaned/output.csv")

print("Original Data:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Clean spaces in name column
if "name" in df.columns:
    df["name"] = df["name"].str.strip()

print("\nCleaned Data:")
print(df)

# Save cleaned CSV
df.to_csv("../data/cleaned/cleaned_output.csv", index=False)

print("\nCleaned file saved successfully!")