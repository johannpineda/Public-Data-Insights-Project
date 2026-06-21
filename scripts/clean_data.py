import pandas as pd

df = pd.read_csv("../data/public_data.csv")

print("Original rows:", len(df))

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values (if any)
df = df.dropna()

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Create new features
df["Month"] = df["Date"].dt.to_period("M")

df["DayOfWeek"] = df["Date"].dt.day_name()

df.to_csv("../data/clean_public_data.csv", index=False)

print("Clean dataset saved")