import pandas as pd
data = {
    "Customer": ["Alice", "Bob", "Charlie", "Alice", "Bob", "David"],
    "Region": ["North", "South", "North", "South", "North", "South"],
    "Sales": [200, 150, 300, 400, 250, 100]
}

df = pd.DataFrame(data)

# Find top 3 customers by sales per region
data = {
    "Customer": ["Alice", "Bob", "Charlie", "David"],
    "Sales": [200, None, 300, None]
}

df = pd.DataFrame(data)

# Check missing values
# print(df.isnull().sum())
#
# # Fill missing sales with 0
# df["Sales"] = df["Sales"].fillna(0)
# print(df)

print(df.query("Customer=='Alice' & Sales>=200")[["Customer"]])