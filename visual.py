import pandas as pd
import matplotlib.pyplot as plt

print("VISUALIZATION TASK RUNNING...\n")

# Load dataset
df = pd.read_csv("books_data.csv", encoding="utf-8-sig")

# Clean price column
df["Price"] = df["Price"].str.replace("Â£", "").str.replace("£", "").astype(float)


# 1. Rating Distribution Chart
rating_counts = df["Rating"].value_counts()

plt.figure()
rating_counts.plot(kind="bar")
plt.title("Book Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()


# 2. Price Distribution
plt.figure()
df["Price"].plot(kind="hist", bins=10)
plt.title("Price Distribution of Books")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()


# 3. Top 10 Expensive Books
top_books = df.sort_values(by="Price", ascending=False).head(10)

plt.figure()
plt.barh(top_books["Title"], top_books["Price"])
plt.title("Top 10 Expensive Books")
plt.xlabel("Price")
plt.gca().invert_yaxis()
plt.show()
