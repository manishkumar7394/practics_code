import pandas as pd

df = pd.read_csv("/Users/vikas/Documents/emp_data.csv")
# print(df.head())

# print(df.info)


#  Basic
# 	1.	Show first 5 rowsˀ
# print(df.head(5))

# 	2.	Show only Name and Salary
# print(df[df['Name','Salary']])
# print(df[['Name', 'Salary']])
# 	3.	Filter employees with Salary > 40000
# print(df['Salary']> 40000)
# 	4.	Count total employees
# print(df['EmployeeID'].count())

# 🟡 Intermediate
# 	5.	Find average salary
# print(df['Salary'].mean())

# 	6.	Find highest salary employee
# print(df['salary'].max())

# 	7.	Group by Department and find average salary
# 	8.	Sort data by Salary (descending)
# 	9.	Find employees whose Performance = “Excellent”

# ⸻

# 🔴 Advanced
# 	10.	Create new column: TotalPay = Salary + Bonus
# 	11.	Find department with highest average salary
# 	12.	Convert JoiningDate to datetime
# 	13.	Find employees who joined after 2020
# 	14.	Get top 3 highest paid employees
# 	15.	Find duplicate departments count

df.describe()

