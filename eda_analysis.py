import pandas as pd

df = pd.read_csv("../data/cleaned_data.csv")

print("Department Summary (mean of transactions and amount):")
print(df.groupby("department")[["transactions", "amount"]].mean())

print("\nMonthly Trends (sum of amount):")
print(df.groupby("month")["amount"].sum())
