import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from numpy import median

df = pd.read_csv(
    "https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/iot-devices/IoT-device.csv")

# Checking for null values
df.isnull().sum()

# Dropping unecessary columns
df = df.drop(columns=["room_id/id", "id"])

# Convert date values to datetime
df["noted_date"] = pd.to_datetime(df["noted_date"])
df.info()

# Sorting df
df = df.sort_values(by="noted_date")

# Adding Date Columns
df["year"] = df["noted_date"].dt.year
df["month"] = df["noted_date"].dt.month
df["day"] = df["noted_date"].dt.day
df["day_name"] = df["noted_date"].dt.day_name()
df["hours"] = df["noted_date"].dt.hour
df["minutes"] = df["noted_date"].dt.minute

# LINE PLOTS AND BOX PLOTS
# Indoor Temperature Records
in_temp_df = df[df["out/in"] == "In"]
plt.figure(figsize=(20, 6))
plt.plot(in_temp_df["noted_date"], in_temp_df["temp"], color="red")
plt.grid(True)
plt.show()

# Outdoor Temprature Records
out_temp_df = df[df["out/in"] == "Out"]
plt.figure(figsize=(20, 6))
plt.plot(out_temp_df["noted_date"], out_temp_df["temp"], color="red")
plt.grid(True)
plt.show()

# Comparison
plt.figure(figsize=(20, 6))
plt.plot(out_temp_df["noted_date"], out_temp_df["temp"], color="red")
plt.plot(in_temp_df["noted_date"], in_temp_df["temp"], color="blue")
plt.grid(True)
plt.show()

# Box Plot Comparison
plt.figure(figsize=(20, 6))
sns.boxplot(x="out/in", y="temp", data=df)
plt.grid(True)
plt.show()

# Monthly Distribution BoxPlots
months_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
plt.figure(figsize=(20, 6))
sns.boxplot(x="month", y="temp", data=df)
plt.xticks(ticks=np.arange(12), labels=months_name)
plt.grid(True)
plt.show()

# Grouping and Aggregating df
group_month = df.groupby(by=["out/in", "month"], sort=True)
agg_df = group_month.agg(func={"temp": ["median", "min", "max"]})

# Line Plot Monthyl Median Indoor Temperatures
plt.figure(figsize=(20, 6))
plt.plot(months_name, agg_df[("temp", "median")][:12].values)
plt.grid()
plt.show()

# Line Plot Monthyl Median Outdoor Temperatures
plt.figure(figsize=(20, 6))
plt.plot(months_name, agg_df[("temp", "median")][12:].values)
plt.grid()
plt.show()

# Comparison
plt.figure(figsize=(20, 6))
plt.plot(months_name, agg_df[("temp", "median")][12:].values, color="orange", label="Outdoor Temperature")
plt.plot(months_name, agg_df[("temp", "median")][:12].values, color="green", label="Indoor Temperature")
plt.legend()
plt.grid()
plt.show()

# Bar Plot Comparison
plt.figure(figsize=(20, 6))
sns.barplot(x="month", y="temp", hue="out/in", data=df, estimator=median)
plt.grid()
plt.show()

# Max Min Temperatures For Each Day In Each Month
group_month_day = df.groupby(by=["month", "day"]).agg(func={"temp": ["max", "min"]})

# Hottest Days
hottest_days = []
for i in range(1, 13):
    grp_df = df.groupby(by="month").get_group(i)
    max_temp = grp_df.loc[grp_df['temp'] == grp_df['temp'].max(), 'temp'].unique()[0]
    max_temp_day = grp_df.loc[grp_df['temp'] == grp_df['temp'].max(), 'day'].unique()[0]
    hottest_days.append((i, max_temp, max_temp_day))

# Coldest Days
coldest_days = []
for i in range(1, 13):
    grp_df = df.groupby(by="month").get_group(i)
    max_temp = grp_df.loc[grp_df['temp'] == grp_df['temp'].min(), 'temp'].unique()[0]
    max_temp_day = grp_df.loc[grp_df['temp'] == grp_df['temp'].min(), 'day'].unique()[0]
    coldest_days.append((i, max_temp, max_temp_day))


# Heat Index Function
def heat_index(temp_series):
    heat_index_list = []
    for temp in temp_series:
        if temp <= 32:
            heat_index_list.append('Green')
        elif (temp > 32) and (temp <= 41):
            heat_index_list.append('Yellow')
        elif (temp > 41) and (temp <= 54):
            heat_index_list.append('Orange')
        else:
            heat_index_list.append('Red')
    return pd.Series(data=heat_index_list, index=temp_series.index)


# Adding Heat Index In df
df["heat_index"] = heat_index(df["temp"])

# Heat Index Distribution
group_heat_index = df.groupby(by=['heat_index', 'out/in'])
heat_index_agg = group_heat_index.agg(func={'temp': ['max', 'count']})
