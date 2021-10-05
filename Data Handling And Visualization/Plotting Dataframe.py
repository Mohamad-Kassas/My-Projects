import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv(
    "https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/project-3/sample_csv_file.csv")

# Head Of The Dataframe
dataframe.head()

# Shape
dataframe.shape

# Checking for null values
dataframe.isnull().sum()

# Cumulative Frequency
x1 = dataframe.iloc[:, 1]
x1 = np.array(x1)
cumulative = 0
cum = []
for i in range(len(x1)):
    cumulative = x1[i] + cumulative
    cum.append(cumulative)
cum = pd.Series(cum)
print(cum)

# Max, Min, Median
x1 = pd.Series(cum)
print("Median=", x1.median(), end="\n")
print("Maximum= ", x1.max(), end="\n")
print("Minimum= ", x1.min(), end="\n")
print("Mean= ", x1.mean(), end="\n")

# SCATTER AND LINE PLOTS:
# Scatter Plot Between y and x1
x1 = dataframe.iloc[:, 1]
plt.figure(figsize=(40, 20))
x_values_x1 = dataframe.iloc[:, 0]
y_values_y_1 = np.array(x1)
plt.scatter(x_values_x1, y_values_y_1)
plt.show()

# Line Plot between y and x1
plt.figure(figsize=(20, 6))
x_values_x1 = dataframe.iloc[:, 0]
y_values_y_1 = np.array(x1)
plt.plot(x_values_x1, y_values_y_1)
plt.show()

# Scatter Plot Between y and x2
x2 = dataframe.iloc[:, 2]
plt.figure(figsize=(20, 6))
x_values_x2 = dataframe.iloc[:, 0]
y_values_y_2 = np.array(x2)
plt.scatter(x_values_x2, y_values_y_2)
plt.show()

# Line Plot Between y and x2
x2 = dataframe.iloc[:, 2]
plt.figure(figsize=(20, 6))
x_values_x2 = dataframe.iloc[:, 0]
y_values_y_2 = np.array(x2)
plt.plot(x_values_x2, y_values_y_2)
plt.show()

# Scatter Plot Between y and x3
x3 = dataframe.iloc[:, 3]
plt.figure(figsize=(20, 6))
x_values_x3 = dataframe.iloc[:, 0]
y_values_y_3 = np.array(x3)
plt.scatter(x_values_x3, y_values_y_3)
plt.show()

# Line Plot Between y and x3
x3 = dataframe.iloc[:, 3]
plt.figure(figsize=(20, 6))
x_values_x3 = dataframe.iloc[:, 0]
y_values_y_3 = np.array(x3)
plt.plot(x_values_x3, y_values_y_3)
plt.show()

# Scatter Plot Between y and x4
x4 = dataframe.iloc[:, 4]
plt.figure(figsize=(40, 20))
x_values_x4 = dataframe.iloc[:, 0]
y_values_y_4 = np.array(x4)
plt.scatter(x_values_x4, y_values_y_4)
plt.show()

# Line Plot Between y and x4
x4 = dataframe.iloc[:, 4]
plt.figure(figsize=(40, 20))
x_values_x4 = dataframe.iloc[:, 0]
y_values_y_4 = np.array(x4)
plt.plot(x_values_x4, y_values_y_4)
plt.show()
