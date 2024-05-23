# PYTHON - DATA ENGINEER WORKSHOP

# IMPORT MODULE
import pandas as pd
from pandas.tseries.offsets import MonthEnd
from sqlalchemy import create_engine, text

# EXTRACT
# From database to dataframe
engine = create_engine('sqlite:///dataset-day5.db') # Turn on database engine
query = text("""SELECT * FROM trans_table_full""")
df_order_txn = pd.read_sql(query, con=engine, parse_dates=['Order_Date', 'Ship_Date'])

# TRANSFORM
# Rename column name to lowercase and underscore (if necessary to separate word)
df_order_txn.columns = [c.lower().replace("-", "_") for c in df_order_txn.columns]

# Change date column (order_date, ship_date) type string to datetime
df_order_txn['order_date'] = pd.to_datetime(df_order_txn['order_date'], dayfirst=False, yearfirst=False)
df_order_txn['ship_date'] = pd.to_datetime(df_order_txn['ship_date'], dayfirst=False, yearfirst=False)

# Add ship_days column and compute days
df_order_txn["ship_days"] = (df_order_txn['ship_date'] - df_order_txn['order_date']).dt.days

# Convert datetime to end of month
df_order_txn['data_date'] = df_order_txn['order_date'] + MonthEnd(0)

# Sales Aggregation
df_sales = df_order_txn.groupby('data_date').agg({
    'sales' : ['max', 'sum'],
    'quantity' : ['mean', 'sum'],
    'discount' : ['sum'],
    'ship_days' : ['max', 'min']
})
df_sales.columns = [f'{agg}_{col}' for col, agg in df_sales.columns] # Rename column name
df_sales = df_sales.reset_index() # Set index value

# Sales by Region Aggregation
df_sales_by_region = df_order_txn.groupby(['data_date', 'region']).agg({
    'sales' : ['max', 'sum'],
    'quantity' : ['mean', 'sum'],
    'discount' : ['sum'],
    'ship_days' : ['max', 'min']
})
df_sales_by_region.columns = [f'{agg}_{col}' for col, agg in df_sales_by_region.columns] # Rename column name
df_sales_by_region = df_sales_by_region.reset_index() # Set index value

# Sales by Category Aggregation
df_sales_by_category = df_order_txn.groupby(['data_date', 'category']).agg({
    'sales' : ['max', 'sum'],
    'quantity' : ['mean', 'sum'],
    'discount' : ['sum'],
    'ship_days' : ['max', 'min']
})
df_sales_by_category.columns = [f'{agg}_{col}' for col, agg in df_sales_by_category.columns] # Rename column name
df_sales_by_category = df_sales_by_category.reset_index() # Set index value

# LOAD
# To database and csv
engine = create_engine('sqlite:///superstore.db') # Turn on database engine

# Order transection
df_order_txn.to_sql('order_txn', index=False, if_exists='replace', con=engine)
df_order_txn.to_csv('order_txn.csv', index=False)

# Sales
df_sales.to_sql('sales', index=False, if_exists='replace', con=engine)
df_sales.to_csv('sales.csv', index=False)

# Sales by Region
df_sales_by_region.to_sql('sales_by_region', index=False, if_exists='replace', con=engine)
df_sales_by_region.to_csv('sales_by_region.csv', index=False)

# Sales by Category
df_sales_by_category.to_sql('sales_by_category', index=False, if_exists='replace', con=engine)
df_sales_by_category.to_csv('df_sales_by_category.csv', index=False)
