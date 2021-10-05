import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/video-games-sales/video-game-sales.csv")

# Treating Null Values
df.isnull().sum()
df = df[df['Year'].isna() == False]
df = df[df['Publisher'].isna() == False]

# Converting Year Values to int
df["Year"] = df["Year"].astype("int")

# Yearly Total Units Sold
group_year = df.groupby(by="Year")
my_func = {
    col: "sum" for col in df.columns[-5:]
}
yearly_total_sales = group_year.agg(func=my_func)

# Lines Plots Yearly Total Sales Accross Regions
for col in yearly_total_sales.columns:
    plt.style.use("dark_background")
    plt.figure(figsize=(20, 6))
    plt.title(f"{col} yearly")
    plt.plot(yearly_total_sales.index, yearly_total_sales[col], "r-o")
    plt.grid(True)
    plt.show()

# Genre Wise Total Units Sold
group_genre = df.groupby(by="Genre")
my_func = {
    col: "sum" for col in df.columns[-5:]
}
genre_wise_total_sales = group_genre.agg(func=my_func)

# Lines Plots Genre Wise Total Sales Across Regions
for col in genre_wise_total_sales.columns:
    plt.style.use("dark_background")
    plt.figure(figsize=(20, 6))
    plt.title(col)
    plt.plot(genre_wise_total_sales.index, genre_wise_total_sales[col], "r-o")
    plt.grid(True)
    plt.show()

# Publisher Wise Total Units Sold
publisher = df.groupby(by="Publisher")
my_func = {
    col: "sum" for col in df.columns[-5:]
}
publisher_wise_total_sales = publisher.agg(func=my_func)
publisher_wise_total_sales["Global_Sales"].sort_values()

# Lines Plots Genre Wise Total Sales Across Regions
platform = df.groupby(by="Platform")
my_func = {
    col: "sum" for col in df.columns[-5:]
}
platform_wise_total_sales = platform.agg(func=my_func)
platform_wise_total_sales["Global_Sales"].sort_values()
