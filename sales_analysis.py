import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
data = pd.read_excel('Sales Data - New.xlsx')

# Calculate total sales for each product line
data['TOTALSALES'] = data['QUANTITYORDERED'] * data['PRICEEACH']
product_line_sales = data.groupby('PRODUCTLINE')['TOTALSALES'].sum()

# Plot the sales by product line
plt.figure(figsize=(10, 6))
product_line_sales.sort_values().plot(kind='bar')
plt.title('Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.show()

# Convert ORDERDATE to datetime format
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])

# Calculate monthly sales
monthly_sales = data.resample('M', on='ORDERDATE')['TOTALSALES'].sum()

# Plot the sales performance over time
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line')
plt.title('Sales Performance Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()

# Calculate total sales for each deal size
deal_size_sales = data.groupby('DEALSIZE')['TOTALSALES'].sum()

# Calculate the percentage contribution
deal_size_percentage = (deal_size_sales / deal_size_sales.sum()) * 100

# Plot the sales by deal size
plt.figure(figsize=(10, 6))
deal_size_sales.sort_values().plot(kind='bar')
plt.title('Sales by Deal Size')
plt.xlabel('Deal Size')
plt.ylabel('Total Sales')
plt.show()

# Print the percentage contribution

