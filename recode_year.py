import pandas as pd

# Load the data
data = pd.read_csv("data_raw/races.csv")

# Recode the "year" column into "year_brackets"
data['year_brackets'] = pd.cut(
    data['year'],
    bins=[1950, 1965, 1980, float('inf')],
    labels=["1950-1965", "1966-1980", "1980-onwards"],
    right=True
)

# Save the modified DataFrame (optional)
data.to_csv("data_raw/races_recode.csv", index=False)

# Print the first few rows to verify
print(data.head())
