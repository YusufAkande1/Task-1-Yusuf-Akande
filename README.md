# Sales Data Analytics Project

## Project Overview
This project focuses on cleaning, analyzing, and extracting insights from a sales dataset using Excel, Python, and SQL.

The workflow covered:
- Data Cleaning & Preparation
- Exploratory Data Analysis (EDA)
- SQL Business Analysis
- Data Visualization

The goal of the project was to transform raw sales data into meaningful business insights that can support data-driven decision-making.

---

# Tools & Technologies Used

- Excel
- Python
- Pandas
- Matplotlib
- Seaborn
- PostgreSQL (pgAdmin)
- SQL

# Project Workflow

## 1. Data Cleaning & Preparation

The raw dataset was cleaned using Excel and Python.

### Tasks Performed
- Identified and handled missing values
- Removed duplicate records
- Corrected data formats
- Standardized text columns
- Validated numerical calculations

### Python Libraries Used
import pandas as pd

# Fill missing values
df["CouponCode"] = df["CouponCode"].fillna("NO COUPON")

# Remove duplicates
df = df.drop_duplicates()

# Clean text columns
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].str.strip()

## 2. Exploratory Data Analysis (EDA)

EDA was performed to understand trends, patterns, and relationships within the dataset.

### Analysis Conducted
- Top-selling products
- Revenue analysis
- Payment method analysis
- Monthly sales trends
- Order status distribution
- Customer spending behavior

# Example Visualization Code
top_products = df["Product"].value_counts().head(10)

top_products.plot(kind="bar")

plt.title("Top Selling Products")

plt.show()

## 3. SQL Business Analysis

PostgreSQL was used to perform business-focused analysis on the cleaned dataset.

### SQL Analysis Included
- Total revenue analysis
- Top-selling products
- Monthly revenue trends
- Payment method usage
- Customer purchase behavior
- Order status analysis

# Example SQL Query
SELECT 
    Product,
    SUM(TotalPrice) AS revenue
FROM sales_data
GROUP BY Product
ORDER BY revenue DESC;

## Key Insights
- Certain products generated significantly higher revenue
- Customer payment preferences were identified
- Sales varied across different months
- Revenue trends provided useful business insights
- Data cleaning improved data consistency and reliability

## Skills Demonstrated
- Data Cleaning
- Exploratory Data Analysis
- SQL Querying
- Data Visualization
- Business Insight Generation
- Python Programming
- PostgreSQL

## Future Improvements
- Build an interactive Power BI dashboard
- Add advanced SQL analysis
- Perform predictive analytics
- Automate reporting workflow

## Author
Yusuf Akande

Aspiring Data Analyst passionate about transforming raw data into actionable insights using Python, SQL, Excel, and Power BI.

Aspiring Data Analyst passionate about transforming raw data into actionable insights using Python, SQL, Excel, and Power BI.
import pandas as pd
import numpy as np
