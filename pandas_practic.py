import pandas as pd

# From a dictionary (most common)
df = pd.DataFrame({
    'Name'  :   ['manish','ujwal','ramesh','priya','kriti','abinav','aman'],
    'Age'   :   [23,22,22,25,22,20,28]  ,
    'city'  :   ['baskhari','kanpur','sultanpur','basti','balia','gonda','lucknow'],
    'num.'   :   [7394083568,7860131126,9621683567,9554948956,8052384712,7860192011,3445783298],
    'email '  : [ 'manishk@gmail.com','ujawal@gmail.com','rameshk@gmail.com','priya@gmail.com','kriti@gmail.com','aman@gmail.com','abinav@gmail.com']

    })
df["salary"] = [1000,1200,1100,1400,1200,1212,1223]
# print(df)
# print("====header top 5 ======")                          #first 5 row
# print(df.head())                                         
# print("====tail bottum 5 ======")                         #last 3 roq
# print(df.tail(3))
# print("====shape ======")
# print(df.shape)
# print("====type ======")
# print(f"\n {df.describe()}")
# print('=======info=======')
# print(df.info())
# print('columns =====')
# print(df.columns)                     #show only column name
# print(df[["Name", "Age"]])            #check multiple columns
# print(df["Name"])                        #check single column

# print(df.iloc[1])                   #single person detail chekc
# print(df.loc[0])

# data filtering 
# print(df[df["Age"]<=23])
# print(df[df["city"] == "kanpur"])

# print(df.columns)
# print(df.shape)
# print(df["Age"])

# print(df[['Name','Age']])
# print(df.iloc[2])
# print(df[df['Age']>25])
# df["salary"] = [1000,1200,1100,1400,1200,1212,1223]
# print(df)
# df['salary'] = [1000, 2000]
# df['bonus'] = df['salary'] * 0.1
# print(df.drop('Age', axis= 1, inplace= True))                   #delet colum , axis= 1 used for colun and row axis =0
# print(df)
# print(df.rename(columns= {'Age': 'year'},inplace=True))           #rename the column name
# 13.	Check for missing values.
# print(df.isnull())
# 14.	Fill missing values with 0.
# print(df.fillna(0))
# 15.	Get summary statistics of numeric columns.
# print(df.describe())

# 🟡 ⚡ Level 2: Intermediate (Q16–Q30)
# 	16.	Sort the DataFrame by age.
# print(df.sort_values('Age'))

# 	17.	Sort in descending order.
# print(df.sort_values('salary',ascending=False))

# 	18.	Find unique values in city.
# print(df['city'].unique())    #show only distinct values 

# 	19.	Count occurrences of each city.
# print(df['city'].value_counts())

# 	20.	Find the average of age.
# print(df['Age'].mean())

# 	21.	Filter records where age > 20 AND city = "Delhi".
# print(df[(df["Age"]>24) & (df['city']== "basti")])

# 	22.	Remove duplicate rows.
# print(df.duplicated())
# print(df.drop_duplicates(inplace=True))
# print(df.drop_duplicates(subset = ['Age'])) 
# print(df.drop_duplicates())

# 	23.	Reset the index.
# print(df.reset_index())
# df.reset_index(drop=True, inplace=True)
# print(df)

# 	24.	Double the age column using apply().
# print(df['Age'].apply(lambda x:x*2))
# df['Age'] = df['Age'] * 2

# 	25.	Convert a string column to uppercase.
# print(df['Name'].str.upper())
# print(df['Name'].str.lower())
# print(df['Name'].str.title())
# print(df['Name'].str.capitalize())


# 	26.	Merge two DataFrames using an inner join.
import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'salary': [1000, 2000, 3000]
})

# result = pd.merge(df1, df2, on='id')
# print(result)

# 	27.	Perform a left join between two DataFrames.

# result = pd.merge(df1,df2,on= 'id',how = 'left')
# print(result)

# 	28.	Concatenate two DataFrames.
df3 = pd.DataFrame ({
    'name ' : ['a','b','c'],
    'age'   : [23,34,19]

})
df4 = pd.DataFrame ({
    'name': ['manish','aman','priya'],
    'age': [20,23,19]

})
# result = pd.concat([df3, df4], ignore_index= True)
# print(result)

# 	29.	Get top 3 values of a column.
print(df['Age'].nlargest(1))                                        #1
print(df['Age'].nsmallest(1))                                          #smalast value
print(df.sort_values(by='Age',ascending=False).head(3))             #2

# 	30.	Get a random sample of 5 rows.
print(df.sample(5))



# 🔵 🚀 Level 3: Advanced (Q31–Q50)
# 	31.	Use groupby to find average age per city.


# 	32.	Use groupby to calculate total salary per city.

# 	33.	Perform multiple aggregations (mean, max).
# 	34.	Create a pivot table (city vs salary).
# 	35.	Replace specific values in a column.
# 	36.	Extract year from a date column.
# 	37.	Calculate rolling mean (window = 3).
# 	38.	Calculate cumulative sum.
# 	39.	Generate a correlation matrix.
# 	40.	Sort by multiple columns.
# 	41.	Create a conditional column (if age > 25 → “Adult”).
# 	42.	Check if a column contains a substring.
# 	43.	Fill missing values using forward fill.
# 	44.	Save DataFrame to a CSV file.
# 	45.	Read a CSV file and display top 10 rows.
# 	46.	Change column datatype (int → float).
# 	47.	Convert index into a column.
# 	48.	Create a multi-index DataFrame.
# 	49.	Use groupby with filter (salary > 5000 groups).
# 	50.	Apply a custom function to the DataFrame.