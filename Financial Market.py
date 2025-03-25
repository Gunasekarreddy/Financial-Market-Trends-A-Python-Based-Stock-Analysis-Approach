
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('nifty_500.csv')

# Display the first few rows of the dataset
df.head()

# Data Cleaning

# Check for missing values
print(df.isnull().sum())

# Fill missing values with appropriate methods (e.g., fill with 0 or mean)
df.fillna(0, inplace=True)

# Convert columns to appropriate data types if necessary
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
df['Previous Close'] = pd.to_numeric(df['Previous Close'], errors='coerce')
df['Last Traded Price'] = pd.to_numeric(df['Last Traded Price'], errors='coerce')
df['Change'] = pd.to_numeric(df['Change'], errors='coerce')
df['Percentage Change'] = pd.to_numeric(df['Percentage Change'], errors='coerce')
df['Share Volume'] = pd.to_numeric(df['Share Volume'], errors='coerce')
df['Value (Indian Rupee)'] = pd.to_numeric(df['Value (Indian Rupee)'], errors='coerce')
df['52 Week High'] = pd.to_numeric(df['52 Week High'], errors='coerce')
df['52 Week Low'] = pd.to_numeric(df['52 Week Low'], errors='coerce')
df['365 Day Percentage Change'] = pd.to_numeric(df['365 Day Percentage Change'], errors='coerce')
df['30 Day Percentage Change'] = pd.to_numeric(df['30 Day Percentage Change'], errors='coerce')

# Data Manipulation

# Calculate the average of the 'Open', 'High', and 'Low' prices
df['Average Price'] = (df['Open'] + df['High'] + df['Low']) / 3

# Create a new column for the difference between the 52 Week High and 52 Week Low
df['52 Week Range'] = df['52 Week High'] - df['52 Week Low']

# Group by 'Industry' and calculate the mean of 'Last Traded Price'
industry_mean_price = df.groupby('Industry')['Last Traded Price'].mean().reset_index()

# Sort the DataFrame by 'Percentage Change' in descending order
df_sorted = df.sort_values(by='Percentage Change', ascending=False)

# Data Visualization

# Set the style for seaborn
sns.set(style="whitegrid")

# Plot the distribution of 'Last Traded Price'
plt.figure(figsize=(10, 6))
sns.histplot(df['Last Traded Price'], bins=30, kde=True)
plt.title('Distribution of Last Traded Price')
plt.xlabel('Last Traded Price')
plt.ylabel('Frequency')
plt.show()

# Plot the top 10 companies with the highest 'Percentage Change'
top_10_percentage_change = df_sorted.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='Company Name', y='Percentage Change', data=top_10_percentage_change)
plt.title('Top 10 Companies with Highest Percentage Change')
plt.xlabel('Company Name')
plt.ylabel('Percentage Change')
plt.xticks(rotation=45)
plt.show()

# Plot the average 'Last Traded Price' by 'Industry'
plt.figure(figsize=(12, 8))
sns.barplot(x='Industry', y='Last Traded Price', data=industry_mean_price)
plt.title('Average Last Traded Price by Industry')
plt.xlabel('Industry')
plt.ylabel('Average Last Traded Price')
plt.xticks(rotation=90)
plt.show()

# Plot a scatter plot between '52 Week High' and '52 Week Low'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='52 Week High', y='52 Week Low', data=df)
plt.title('Scatter Plot of 52 Week High vs 52 Week Low')
plt.xlabel('52 Week High')
plt.ylabel('52 Week Low')
plt.show()

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()