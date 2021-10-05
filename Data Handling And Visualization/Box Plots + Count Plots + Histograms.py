import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cc_df = pd.read_csv("https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/uci-credit-card-fraud/UCI_Credit_Card.csv")

# Cleaning The Education Column
wrong_edu = cc_df[(cc_df["EDUCATION"]==6)].index
wrong_edu2 = cc_df[(cc_df["EDUCATION"]==0)].index
cc_df.loc[wrong_edu,"EDUCATION"] = 5
cc_df.loc[wrong_edu2,"EDUCATION"] = 5
cc_df["EDUCATION"].value_counts()

# University Graduates Percentage
for i in range(1,6):
  percentage = (((cc_df["EDUCATION"]==i).sum())*100)/30000
  print("Percentage of ",i," : ",round(percentage,2),"%")

# Count Plot
sns.countplot(data = cc_df, x = cc_df["EDUCATION"])
plt.grid()

# Male and Female Percentages
for i in range(1,3):
  percentage = (((cc_df["SEX"]==i).sum())*100)/30000
  print("Percentage of ",i," : ",round(percentage,2),"%")

# Count Plot
sns.countplot(data = cc_df, x = cc_df["SEX"])
plt.grid()


# Cleaning The Marital Status Column
wrong_mar = cc_df[(cc_df["MARRIAGE"]==0)].index
cc_df.loc[wrong_mar,"MARRIAGE"] = 3
cc_df["MARRIAGE"].value_counts()

# Married Percentages
for i in range(1,4):
  percentage = (((cc_df["MARRIAGE"]==i).sum())*100)/30000
  print("Percentage of ",i," : ",round(percentage,2),"%")

# Count Plot
sns.countplot(data = cc_df, x = cc_df["MARRIAGE"])
plt.grid()


# Cleaning The Repayment Column For September 2005
negative_pay0 = cc_df[cc_df["PAY_0"]==-1].index
negative_pay0_2 = cc_df[cc_df["PAY_0"]==-2].index
cc_df.loc[negative_pay0,"PAY_0"] = 0
cc_df.loc[negative_pay0_2,"PAY_0"] = 0
cc_df["PAY_0"].value_counts()

# Percentages Of Repayment Status in September 2005
for i in range(0,9):
  percentage = (((cc_df["PAY_0"]==i).sum())*100)/30000
  print("Percentage of ",i," : ",round(percentage,2),"%")

# Count Plot
sns.countplot(data = cc_df, x = cc_df["PAY_0"])
plt.grid()


# Cleaning The Repayment Column For August 2005
negative_pay2 = cc_df[cc_df["PAY_2"]==-1].index
negative_pay2_2 = cc_df[cc_df["PAY_2"]==-2].index
cc_df.loc[negative_pay2,"PAY_2"] = 0
cc_df.loc[negative_pay2_2,"PAY_2"] = 0
cc_df["PAY_2"].value_counts()

# Percentages Of Repayment Status in August 2005
for i in range(0,9):
  percentage = (((cc_df["PAY_2"]==i).sum())*100)/30000
  print("Percentage of ",i," : ",round(percentage,2),"%")

# Count Plot
sns.countplot(data = cc_df, x = cc_df["PAY_2"])
plt.grid()


# Bill Statements and Previous Repayment Box Plot and Histgorams
# Bill Statements:
bill_amt_cols = ["BILL_AMT1",	"BILL_AMT2",	"BILL_AMT3",	"BILL_AMT4",	"BILL_AMT5",	"BILL_AMT6"]
# Box Plot
for i in range(len(bill_amt_cols)):
  plt.figure(figsize = (20,6))
  sns.boxplot(cc_df[bill_amt_cols[i]])
  plt.show()
# Histogram
for i in range(len(bill_amt_cols)):
  plt.figure(figsize = (20,6))
  plt.hist(cc_df[bill_amt_cols[i]])
  plt.show()

# Previous Payments:
pay_amt_cols = ["PAY_AMT2",	"PAY_AMT3",	"PAY_AMT4",	"PAY_AMT5",	"PAY_AMT6"]
# Box Plot
for i in range(len(pay_amt_cols)):
  plt.figure(figsize = (20,6))
  sns.boxplot(cc_df[pay_amt_cols[i]])
  plt.show()

# Histogram
for i in range(len(pay_amt_cols)):
  plt.figure(figsize = (20,6))
  plt.hist(cc_df[pay_amt_cols[i]])
  plt.show()


# Box Plot And Histogram For The Age Column
# Box Plot
plt.figure(figsize=(20,6))
sns.boxplot(cc_df["AGE"])
plt.show()
# Histogram
plt.figure(figsize=(20,6))
plt.hist(cc_df["AGE"])
plt.show()


# Box Plot And Histogram For The Limit Balance Column
# Box Plot
plt.figure(figsize=(20,6))
sns.boxplot(cc_df["LIMIT_BAL"])
plt.show()
# Histogram
plt.figure(figsize=(20,6))
plt.hist(cc_df["LIMIT_BAL"])
plt.show()
# More Detailed Histogram
plt.figure(figsize=(20,6))
plt.hist(cc_df["LIMIT_BAL"],bins=50)
plt.show()