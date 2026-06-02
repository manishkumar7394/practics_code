import pandas as pd 
employee = pd.read_csv("Employee_ID,Name,Department,Salary,Bonus,Joining_Date,Performance,City,Age
101,Amit,HR,40000,5000,2020-01-15,Good,Delhi,28
102,Ravi,IT,60000,8000,2019-03-10,Excellent,Mumbai,32
103,Sita,Finance,50000,6000,2021-07-23,Average,Delhi,26
104,Neha,IT,75000,10000,2018-11-05,Excellent,Bangalore,35
105,Arjun,HR,42000,4000,2022-02-20,Good,Delhi,24
106,Pooja,Finance,52000,7000,2020-06-30,Good,Mumbai,29
107,Vikas,IT,68000,9000,2019-09-17,Average,Bangalore,31
108,Anjali,HR,39000,3000,2021-12-01,Poor,Delhi,27
109,Rohit,Finance,58000,7500,2018-04-25,Excellent,Mumbai,36
110,Kiran,IT,72000,8500,2020-08-14,Good,Bangalore,30")

print(employee.head(5))


