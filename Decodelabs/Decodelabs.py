# IMPORT LIBRARY
import pandas as pd

# LOAD DATASET
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# PREVIEW DATASET
print(df.head())
print(df.info())

# CHECK FOR MISSING VALUES
print(df.isnull().sum())

# FILL MISSING COUPONCODE WITH VALUES
df["CouponCode"] = df["CouponCode"].fillna("NO COUPON")

# CONFIRM MISSING VALUES ARE GONE
print(df.isnull().sum())

# CHECK FOR DUPLICATES
print(df.duplicated().sum)

df = df.drop_duplicates()

# CHECK DATA TYPE
print(df.dtypes)

# CHECK NUMERICAL COLUMNS
num_cols = ["Quantity",
            "UnitPrice",
            "ItemsInCart",
            "TotalPrice"
            ]
print(df[num_cols].dtypes)

# CLEAN TEXT COLUMNS
text_cols = df.select_dtypes(include="object").columns

for col in text_cols:
    df[col] = df[col].str.strip()

# STANDARDIZE TEXT FORMATTING
for col in text_cols:
    df[col] = df[col].str.title()

# VALIDATE TOTAL PRICE
# To check if Quantity * UnitPrice = TotalPrice

df["CalculatedTotal"] = (
    df["Quantity"] * df["UnitPrice"]
)
# Compare Values
print(
    df[
        ["Quantity",
         "UnitPrice",
         "TotalPrice",
         "CalculatedTotal"]
    ].head()
)

# SAVE CLEANED DATASET
df.to_excel("Data_Analytics.xlsx",
            index=False)

print("Data cleaning completed successfully.")