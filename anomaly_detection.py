import pandas as pd

df = pd.read_csv("../data/cleaned_data.csv")

threshold = df["amount"].mean() + 2 * df["amount"].std()
anomalies = df[df["amount"] > threshold]

print("Detected Anomalies:")
print(anomalies)
