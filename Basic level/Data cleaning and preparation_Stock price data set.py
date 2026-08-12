print("\033c")
import pandas as pd
df = pd.read_csv ('Stock Prices Data Set.csv')

#exploring the Data to see all columns
print(df)

#Checking for and calculating the percentage of missing values
print(df.isna().any())
df_sum_isnull = df.isna().sum()
print(df_sum_isnull)
perc_null = df_sum_isnull/len(df) * 100
print(perc_null)
#Calcalating the mean of the columns with missing values
open_mean = df['open'].mean()
print(open_mean)
high_mean = df['high'].mean()
print(high_mean)
low_mean = df['low'].mean()
print(low_mean)
#Checking for duplicates
duplicates = df.duplicated().any()
print(duplicates)

######Cleaning data 
 
# Fill missing values for just those 3 columns
cols = ['low', 'high', 'open']
df[cols] = df[cols].fillna(df[cols].median())

#droping duplicates
df_clean = df.drop_duplicates()
#convert string to datetime on date column
df['date'] = pd.to_datetime(df['date'])

#Creating new columns for Year, Month and date for Trend Analysis

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

df_clean.to_csv("Stock_prices_cleaned.csv", index =False)
