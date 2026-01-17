import pandas as pd

df = pd.read_csv("../data/raw_data.csv")

# Fill missing values
df["transactions"].fillna(df["transactions"].median(), inplace=True)

# Standardize department names
df["department"] = df["department"].str.upper()

df.to_csv("../data/cleaned_data.csv", index=False)
print("Data cleaning completed!")
