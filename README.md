🍔 Food Delivery Data Analysis Project
📌 Project Overview

This project focuses on analyzing a food delivery platform dataset by integrating data from multiple real-world sources and extracting meaningful business insights. The goal is to understand user behavior, revenue trends, restaurant performance, and membership impact using data analysis techniques.

The project simulates an end-to-end data analytics workflow commonly used in industry.

📂 Datasets Used

The project uses three datasets in different formats:

orders.csv

Transactional data (order-level)

Includes order date, total amount, user ID, and restaurant ID

users.json

User master data

Includes user details such as city and membership type (Gold / Regular)

restaurants.sql

Restaurant master data stored in SQL format

Includes restaurant name, cuisine type, and rating

🔗 Data Integration

The datasets are merged using LEFT JOINs to ensure all orders are retained:

orders.user_id → users.user_id

orders.restaurant_id → restaurants.restaurant_id

📁 The merged output is saved as:

final_food_delivery_dataset.csv


This file acts as the single source of truth for all analysis.

🛠️ Tools & Technologies

Python

Pandas

SQLite

JSON handling

CSV processing

📊 Key Analysis & Insights

The project answers multiple analytical and business questions, including:

City-wise revenue analysis (especially for Gold members)

Average Order Value (AOV) by cuisine and membership type

User spending behavior and high-value users

Restaurant rating vs revenue contribution

Membership impact on order volume and revenue

Quarter-wise revenue trends and seasonality

High-value restaurants with low order counts

🧠 Sample Business Questions Answered

Which city generates the highest revenue from Gold members?

Which cuisine has the highest average order value?

What percentage of orders come from Gold users?

Which membership + cuisine combination contributes the most revenue?

During which quarter is revenue the highest?

How many users spent more than ₹1000 in total?

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install pandas

2️⃣ Project Structure
food_delivery_project/
│── orders.csv
│── users.json
│── restaurants.sql
│── analysis.py
│── final_food_delivery_dataset.csv
│── README.md

3️⃣ Run the Analysis
python analysis.py


This will:

Load all datasets

Merge them correctly

Generate the final dataset

Enable analysis and insights

📈 Key Learnings

Handling multiple data formats (CSV, JSON, SQL)

Performing SQL-style joins using Pandas

Creating a clean analytical dataset

Translating raw data into business insights

Applying real-world data analytics workflows
