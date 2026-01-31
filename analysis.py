import pandas as pd
import json
import sqlite3

# STEP 1: Load orders.csv
orders = pd.read_csv("orders.csv")
print("Orders data loaded")
# print(orders.head())

# STEP 2: Load users.json
with open("users.json", "r") as f:
    users = pd.DataFrame(json.load(f))

print("\nUsers data loaded")
# print(users.head())

# STEP 3: Load restaurants.sql
conn = sqlite3.connect(":memory:")

with open("restaurants.sql", "r") as f:
    conn.executescript(f.read())

restaurants = pd.read_sql("SELECT * FROM restaurants", conn)

print("\nRestaurants data loaded")
# print(restaurants.head())

# STEP 4: Merge datasets (LEFT JOIN)
final_df = (
    orders
    .merge(users, on="user_id", how="left")
    .merge(restaurants, on="restaurant_id", how="left")
)

# print("\nFinal merged dataset")
# print(final_df.head())

# STEP 5: Save final dataset
final_df.to_csv("final_food_delivery_dataset.csv", index=False)
print("\n✅ final_food_delivery_dataset.csv created successfully")


# 1. Which city has the highest total revenue (total_amount) from Gold members?
df=pd.read_csv("final_food_delivery_dataset.csv")
gold_city_revenue = (
    df[df["membership"] == "Gold"]
    .groupby("city")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)
print("\n")
print(f"Gold members' total revenue by city: {gold_city_revenue.index[0]}")


# 2. Which cuisine has the highest average order value across all orders?
avg_order_value_by_cuisine = (
    df.groupby("cuisine")["total_amount"]
    .mean()
    .sort_values(ascending=False)
)
print("\n")
print(f"Average order value by cuisine: {avg_order_value_by_cuisine.index[0]}")


# 3. How many distinct users placed orders worth more than ₹1000 in total (sum of all their orders)?
user_total_spend=df.groupby("user_id")["total_amount"].sum()
count_users=(user_total_spend>1000).sum()
print("\n")
print(f"Number of distinct users with total orders > ₹1000: {count_users}")


# 4. Which restaurant rating range generated the highest total revenue?
df['rating_range']=pd.cut(
    df['rating'],
    bins=[3,3.5,4,4.5,5],
    labels=["3.0-3.5","3.6-4.0","4.1-4.5","4.6-5.0"]
)
rating_revenue = (
    df.groupby("rating_range")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)
print("\n")
print(f"Rating range with highest revenue: {rating_revenue.index[0]}")


# 5. Among Gold members, which city has the highest average order value?
gold_city_average_revenue = (
    df[df["membership"] == "Gold"]
    .groupby("city")["total_amount"]
    .mean()
    .sort_values(ascending=False)
)
print("\n")
print(f"Among Gold members, {gold_city_average_revenue.index[0]} city has the highest average order value")


# 6. What percentage of total orders were placed by Gold members? (Rounded to nearest integer)
percentage_gold_orders = round((df["membership"]=="Gold").mean() * 100)                         
print("\n")
print(f"Percentage of total orders placed by Gold members: {percentage_gold_orders}%")


# 7. Which restaurant has the highest average order value but less than 20 total orders?
restaurant_stats = df.groupby("restaurant_name_y").agg(
    avg_order_value=("total_amount", "mean"),
    total_orders=("order_id", "count")
)
    # Filter restaurants with < 20 orders
filtered = restaurant_stats[restaurant_stats["total_orders"] < 20]
    # Get restaurant with highest average order value
result = filtered.sort_values("avg_order_value", ascending=False).head(1)
print("\n")
print(f"Restaurant with highest average order value but less than 20 total orders: {result.index[0]}")


# 8. Which combination contributes the highest revenue?
combo_revenue = (
    df.groupby(["membership", "cuisine"])["total_amount"]
    .sum()
    .sort_values(ascending=False)
)
print(f"Combination with highest revenue: {combo_revenue.index[0]}")


# 9. During which quarter of the year is the total revenue highest?
df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)
    # Extract quarter
df["quarter"] = df["order_date"].dt.to_period("Q")
    # Total revenue per quarter
quarter_revenue = (
    df.groupby("quarter")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)
print(f"Quarter with highest revenue: {quarter_revenue.index[0]}")


# 10. How many total orders were placed by users with Gold membership?
gold_orders = df[df["membership"] == "Gold"].shape[0]
total_orders = df.shape[0]
print(f"Total orders: {total_orders}")
print("\n")
print(f"Total orders placed by Gold members: {gold_orders}")    


# 11. What is the total revenue (rounded to nearest integer) generated from orders placed in Hyderabad city?
hyderabad_revenue = (
    df[df["city"] == "Hyderabad"]["total_amount"]
    .sum()
)
print("\n")
print(f"Total revenue from Hyderabad city: {round(hyderabad_revenue)}")     


# 12. How many distinct users placed at least one order?
distinct_users = df["user_id"].nunique()
print("\n")
print(f"Number of distinct users who placed at least one order: {distinct_users}") 


# 13. What is the average order value (rounded to 2 decimals) for Gold members?
gold_aov = (
    df[df["membership"] == "Gold"]["total_amount"]
    .mean()
)
print(f"Average order value for Gold members: {round(gold_aov, 2)}")


# 14. How many orders were placed for restaurants with rating ≥ 4.5?
high_rating_orders = df[df["rating"] >= 4.5].shape[0]
print(f"Number of orders placed for restaurants with rating ≥ 4.5: {high_rating_orders}")


# 15. How many orders were placed in the top revenue city among Gold members only?
gold_chennai_orders = df[
    (df["membership"] == "Gold") &
    (df["city"] == "Chennai")
].shape[0]
print(f"Number of orders placed in the top revenue city among Gold members: {gold_chennai_orders}")

# 16. The total number of rows in the final merged dataset is __________.
total_rows = df.shape[0]
print(f"\nTotal number of rows in the final merged dataset: {total_rows}")  

