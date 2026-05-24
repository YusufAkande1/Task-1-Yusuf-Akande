# Data Cleaning & Preparation Project

## Project Overview
This project focuses on cleaning and preparing a raw dataset using Excel and Python. 

The goal of the project was to improve data quality by handling missing values, removing duplicates, correcting data formats, and preparing the dataset for further analysis.

Clean and reliable data is essential for accurate reporting, analysis, and business decision-making.

---
## Objectives

The main objectives of this project were to:

- Identify missing or null values
- Remove duplicate records
- Correct inconsistent data formats
- Standardize text values
- Prepare the dataset for analysis and visualization

---

## Tools & Technologies Used

- Excel
- Python
- Pandas
- PyCharm
- openpyxl

---

## Dataset Description

The dataset contains sales transaction information such as:

- Order ID
- Customer ID
- Product
- Quantity
- Unit Price
- Payment Method
- Order Status
- Coupon Code
- Referral Source
- Total Price

---

## Data Cleaning Process

### 1. Handling Missing Values

Missing values were identified using both Excel and Python.

#### Example:

```python
print(df.isnull().sum())

Missing values in the CouponCode column were replaced with:

df["CouponCode"] = df["CouponCode"].fillna("NO COUPON")
```
This improved consistency during analysis.

### 2. Removing Duplicates

Duplicate records were identified and removed to avoid inaccurate analysis.

#### Example:
```python
print(df.duplicated().sum())

#Removing duplicates:

df = df.drop_duplicates()
```
### 3. Correcting Data Formats

The dataset contained columns requiring proper formatting.

#### Date Formatting
```
df["Date"] = pd.to_datetime(df["Date"])
```
#### Numeric Formatting
Numeric columns such as:

Quantity
UnitPrice
TotalPrice

were validated for proper numerical data types.

### 4. Cleaning Text Data

Text columns were cleaned by removing extra spaces and standardizing formatting.

#### Example:
```
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].str.strip()
```
This improved consistency across categorical values.

### 5. Validation Checks

Additional checks were performed to ensure:

- No remaining missing values
- No duplicate records
- Correct data types
- Accurate numerical calculations
- Final Output

The cleaned dataset was exported as:

Data_Analytics.xlsx

The dataset is now ready for:

- Exploratory Data Analysis (EDA)
- SQL Analysis
- Power BI Dashboarding
- Machine Learning
- Skills Demonstrated
- Problem Solving
- Key Learning Outcomes

Through this project, I gained practical experience in:

- Handling real-world messy data
- Preparing datasets for analysis
- Using Python for data cleaning automation
- Improving data quality and consistency

## Author

Yusuf Akande

Aspiring Data Analyst passionate about data cleaning, data analysis, SQL, Python, and Power BI.
