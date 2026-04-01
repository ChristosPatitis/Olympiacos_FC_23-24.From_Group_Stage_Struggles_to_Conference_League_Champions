import pandas as pd

# Load data
file_path = "data/raw/olympiacos_matches_raw.csv"
df = pd.read_csv(file_path)

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Create competition_type
europe_comps = ["Europa League", "Champions League", "Conference League"]
df["competition_type"] = df["competition"].apply(
    lambda x: "Europe" if x in europe_comps else "Greece"
)

# Create goal difference
df["goal_difference"] = df["goals_for"] - df["goals_against"]

# Create result column
def get_result(row):
    if row["goals_for"] > row["goals_against"]:
        return "Win"
    elif row["goals_for"] < row["goals_against"]:
        return "Loss"
    else:
        return "Draw"

df["result"] = df.apply(get_result, axis=1)

# Create points column
def get_points(result):
    if result == "Win":
        return 3
    elif result == "Draw":
        return 1
    else:
        return 0

df["points"] = df["result"].apply(get_points)

# Show result
print("\nCleaned Dataset:\n")
print(df)

# Save cleaned version
df.to_csv("data/cleaned/olympiacos_matches_clean.csv", index=False)

print("\nClean dataset saved.")