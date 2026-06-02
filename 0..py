import pandas as pd
# df = pd.read_excel('/Users/vikas/Documents/amazon_sales_20k.xlsx')


# 🟢 Level 1: Basic Understanding
# 	1.	Import pandas and create a DataFrame from a dictionary.
# daf = pd.DataFrame({
#     'name': ['Manish','aman','mukesh'],
#     'age':  [23,20,25]

# })
# print(daf.head())
# 	2.	Load a CSV/Excel file into pandas.
# df = pd.read_excel('/Users/vikas/Documents/amazon_sales_20k.xlsx')
df = pd.read_excel("/Users/vikas/Documents/amazon_sales_20k.xlsx")

# 	3.	Display first 5 rows of dataset.
# print(df.head())
# 	4.	Display last 5 rows.
# print(df.tail())
# print(df.tail())
# 	5.	Check shape of dataset (rows & columns).
# print(df.shape)
# 	6.	Get column names.
# print(df.columns)
# 	7.	Get summary info of dataset (info()).
# print(df.info())

# 🟡 Level 2: Selection & Filtering
# 	8.	Select a single column.
# print(df['Brand'])

# 	9.	Select multiple columns.
# print(df[['Category','OrderDate']].head(2))

# 	10.	Filter rows where a column value > 100.
# print(df[df['UnitPrice']>500])

# 	11.	Filter rows where city = “Delhi”.
# filtered_df = df[df['ShipCity'].str.lower() == 'delhi']
# print(filtered_df)

# df[df['ShipCity'].str.lower() == 'delhi'].shape

# 	12.	Apply multiple conditions (AND / OR).

# 	13.	Select rows using .iloc (index based).
# 	14.	Select rows using .loc (label based).
# print(df.head(2))

# print(df.head())  
import pandas as pd

# pd.set_option('display.max_columns', None)  # सभी columns दिखाने के लिए
# pd.set_option('display.width', None)        # line break न हो

print(df.head(3))  # सिर्फ 3 rows