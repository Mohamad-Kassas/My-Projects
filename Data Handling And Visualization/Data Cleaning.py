import pandas as pd
import seaborn as sns

# Loading df
df = pd.read_csv(
    "https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/bengaluru-house-prices/Bengaluru_House_Prices.csv")

# Head
df.head()

# Checking Null Values
df.isnull().sum()

columns = ["area_type", "availability", "location", "size", 'society', "total_sqft", "bath", "balcony", "price"]
for i in columns:
    null = df[i].isnull().sum()
    print("Column: " + i + "     Null values: ", null)

# Percentage Null Values
columns = ["area_type", "availability", "location", "size", 'society', "total_sqft", "bath", "balcony", "price"]
for i in columns:
    null = df[i].isnull().sum()
    percentage_null = ((null / 13320) * 100).round(3)
    print("Column: " + i + "   Percentage of null values: ", percentage_null)

# CLEANING DATAFRAME
# Removing Null Rows From Location
df[df["location"].isnull() == True]
df["location"].isnull().sum()
correct_location = df[df["location"].isnull() == False]

# Removing Null Rows From Size
correct_location[correct_location["size"].isnull() == True]
correct_location["size"].isnull().sum()
correct_loc_size = correct_location[correct_location["size"].isnull() == False]

# Removing Null Rows From Total Square Feet
correct_loc_size["total_sqft"].isnull().sum()

# Removing Options With More Than 5 Bathrooms
correct_loc_size[correct_loc_size["bath"] > 5]
correct_bath_loc_size = correct_loc_size[correct_loc_size["bath"] <= 5]

# Reviewing Percentage Missing Values
columns = ["area_type", "availability", "location", "size", 'society', "total_sqft", "bath", "balcony", "price"]
for i in columns:
    null = correct_bath_loc_size[i].isnull().sum()
    percentage_null = ((null / 13320) * 100).round(3)
    print("Column: " + i + "   Null Values: ", null, "   Percentage of null values: ", percentage_null)

# Deleting Columns With More Than 15% Null
correct_bath_loc_size.drop("society", inplace=True, axis=1)

# Cleaning Other Columns With Any% Null
correct_bath_loc_size["balcony"].describe()
sns.boxplot(correct_bath_loc_size["balcony"])
correct_bath_loc_size["balcony"].mode()
null_balcony = correct_bath_loc_size[correct_bath_loc_size["balcony"].isnull() == True].index
correct_bath_loc_size.loc[null_balcony, "balcony"] = 2

# Converting Data Types In df
# Converting Values in Bath and Balcony to int
bb = ["bath", "balcony"]
for i in bb:
    correct_bath_loc_size[i] = correct_bath_loc_size[i].astype(int)

print(correct_bath_loc_size["bath"].dtype)
print(correct_bath_loc_size["balcony"].dtype)
