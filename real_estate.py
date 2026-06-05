import pandas as pd

df = pd.read_csv("real_estate.csv")

print("Real Estate Market Trends")

print("\nDataset:")
print(df.head())

print("\nAverage Property Price:")
print(df["Price"].mean())

print("\nProperties by Location:")
print(df["Location"].value_counts())

print("\nAverage Area:")
print(df["Area_sqft"].mean())
