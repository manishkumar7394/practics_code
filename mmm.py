## Mean using a manual for loop

# data = [3, 5, 5, 5, 7, 9]
# Sum = 3 + 5 + 5 + 5 + 7 + 9 = 34
# Count = 6
# Mean = 34 / 6 = 5.666...
# total = 0 
# count = 0 

# for value in data:
#     total = total +value 
#     count =count + 1
#     mean = total/count
# print(f"mean : {mean}")
# print(f"count : {count}")
# print(f"sum all : {total}")

# Learning Point: We avoid naming our variable 'sum' because that shadows
# Python's built-in sum() function. Use 'total' instead — a good habit.
    
# Approach 2: Using sum() and len() — Pythonic One-Liner
# mean = sum(data)/ len(data)
# print(f"mean : {mean}")

# import statistics as st
# mean = st.mean(data)
# print(mean)

# tricky_data = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
# print(f"sum of this : {sum(tricky_data)/len(tricky_data)} ")

# print(f"sum this : {st.mean(tricky_data)}")

# import numpy as np
# data = np.array([32,43,354,32,32,11,456,68,90])
# print(f"mean : {data.mean():.4f}")
# line continuatino character "\"(backslash)

# Common Handy String Functions
myname = "     manish kumar      paswan      "
# print(myname.uppe())
# print(myname.lstrip())
# print(myname.rstrip())
# print(myname.strip)
# print(myn/ame)
# print(myname.strip())

'''
print(myname.strip().upper())
print(myname.strip().lower())
print(myname.strip().title())
print(myname.strip().capitalize())

'''
# print(myname.strip().replace(" ","_"))
# print(myname.strip().split())
# print(myname.strip().split()[0])
# print(myname.strip().split()[2])
# my_var,hii = " this is my first string variable        " ,"hrllo"          
# print(my_var,hii.upper())    # Remove leading and trailing whitespace
import numpy as np
import pandas as pd

data = pd.read_csv("/Users/vikas/Desktop/ex100_prac_tast.csv")
print(data.head())