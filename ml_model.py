import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("../data/cleaned_data.csv")
X = df[["transactions"]]
y = df["amount"]

model = LinearRegression()
model.fit(X, y)

print("Model Coefficient:", model.coef_)
print("Model Intercept:", model.intercept_)
