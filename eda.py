import pandas as pd

print("EDA FILE IS RUNNING CORRECTLY\n")

df = pd.read_csv("books_data.csv", encoding="utf-8-sig")

print(df.head())

print("\nRATING COUNT")
print(df["Rating"].value_counts())

df["Price"] = df["Price"].str.replace("Â£", "").str.replace("£", "").astype(float)

print("\nAVERAGE PRICE:", df["Price"].mean())
print("MAX PRICE:", df["Price"].max())
print("MIN PRICE:", df["Price"].min())