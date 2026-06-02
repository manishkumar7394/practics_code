'''🔹 1️⃣ List
Sabse important 🔥
Multiple values ek variable me store karna.
numbers = [10, 20, 30, 40]
salary = [15000, 20000, 25000]
skills = ["Excel", "SQL", "Python"]
print(salary)

🔹 2️⃣ Tuple
List jaisa hi hota hai
Bas change nahi kar sakte (immutable).


🔹 3️⃣ Dictionary ⭐ (Very Important)
Key-value format me data store karna.

student = {
    "name": "manish",
    "age":  24,
    "city": "lucknow"
}

🔹 4️⃣ Set - - unique values store krta hai'''

# 🟢 Indexing (Bahut Important 🔥) - List me numbering 0 se start hoti hai 
skills = ["excell","sql","python"]
# print(skills[0])        #excell
# print(skills[1])        #sql
# print(skills[2])        #python

# negative index
# print(skills[-1])       #means last value python

# 🟢 List Change Karna
# skills[1] = "power bi"
# print(skills)               #['Excel', 'Power BI', 'Python']


'''🔥 Mini Practice
Ek list banao jisme:
	•	Tumhare 5 favourite numbers ho
	•	Fir:
	•	First number print karo
	•	Last number print karo'''
# number= [73,94,8,35,68]
# print(number[0])
# print(number[-1])

# total = sum(number)
# count = len(number)

# average = total / count

# print("Sum:", total)
# print("Average:", average)
'''Ab tum khud ek program likho jo:
	•	User se 5 numbers input le
	•	Unko list me store kare
	•	Fir sum aur average print kare'''

numbers = []                            #empty list banayi

for i in range(5):
    num = int(input("Enter number: "))          #loop 5 bar chalega
    numbers.append(num)                     #list me value add karta hai

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

# .append() ek time me sirf ek value add karta hai.
# Agar multiple values add karni ho to extend() use karte hain.
# numbers= [1,2]
# numbers.extend([3,4,5])
# print(numbers)
# numbers.append(3)
# print(numbers)
# numbers = [1,2,3]
# numbers.append("45")
# print(numbers)

# numbers = [1,2,3]
# numbers.extend([45])
# numbers.append([6,7])
# print(numbers)

# numbers = [10,20,30,40,50]
# print(numbers[1:4])               [start : end]
# output = [20, 30, 40]

# numbers = [10,20,30,40,50]
# print(numbers[:3])                  [0,3]   output [10,20,30]

# numbers = [10,20,30,40,50]
# print(numbers[-3:])                👉 Start = -3 → 30 se start
# #                                     👉 End = last tak.              output    = [30,40,50]

# 🔥 Reverse kab hota hai?
# Reverse ke liye step -1 dena padta hai:
# print(number[::-1])         output =    [50, 40, 30, 20, 10]

# numbers = [10,20,30,40,50]
# print(numbers[-4:-1])               output = [ 20,30,40]
# numbers = [10,20,30,40,50]
# print(numbers[-1:-4])

'''
Greattt 😎🔥
Chalo start karte hain List Methods – Level 2 💚

Aaj 3 important methods karenge:
✔ pop()
✔ remove()
✔ insert()
# 🔹 1️⃣ pop()

👉 pop() index ke basis par element delete karta hai
👉 Aur deleted value return bhi karta hai'''
# example
# numbers = [10,20,30,40]
# numbers.pop()
# print(numbers)         # output = [10,20,30] Default last element delete hota hai.
# agar index de 
# numbers.pop(1)
# print (numbers)             #Index 1 → 20 delete ho gaya.
'''
🔹 2️⃣ remove()

👉 remove() value ke basis par delete karta hai
👉 Index nahi, value deni hoti hai'''
# numbers = [10,20,30,40]
# numbers.remove(30)
# print(numbers)                      #[10, 20, 40]       Agar value nahi mili to error aayega.

'''🔹 3️⃣ insert()
👉 insert(index, value)
👉 Kisi specific position par value add karta hai'''

# numbers = [10,20,30,40,50]
# numbers.insert(0, 15)                 #  output = [15, 10, 20, 30, 40, 50]
# print(numbers)

# 🧠 Difference Yaad Rakhna
# Method              Kaise kaam karta hai
# pop()               index se delete
# remove()            value se delete.  remove() sirf pehli occurrence delete karta hai(First matching value)

# insert()            index par add

# my test ...
'''numbers = [10,20,30,40,50]
numbers.pop(2)
numbers.remove(40)
numbers.insert(1,99)
print(numbers)
output = [10, 99, 20, 50]'''
# numbers = [10,20,30,20,40]
# numbers.remove(20)
# print(numbers)              output= [10, 30, 20, 40]

# Agar hume saare 20 remove karne ho to kya karein?
# Socho… 💪
# numbers = [10,20,30,40,50]
# while 20 in numbers:
#     numbers.remove(20)
# print(numbers)                  output [10, 30, 40, 50]

'''🔹 1️⃣ sort()  (Permanent change karta hai)'''
# numbers = [50,10,40,20,30]
# numbers.sort()
# print(numbers)          output =[10, 20, 30, 40, 50]
'''🔹 2️⃣ Descending Order'''
# numbers.sort(reverse=True)
# print(numbers)                  output = [50, 40, 30, 20, 10]

'''🔹 3️⃣ sorted()  (Original list change nahi karta)'''
# numbers = [50,10,40,20,30]                 # 👉 sorted() new list banata hai
                                            #👉 Original list safe rehti hai
# new_list = sorted(numbers)
# print(new_list)
# print(numbers)              output [10, 20, 30, 40, 50]
#                                     [50, 10, 40, 20, 30]            

'''🔥 Ab tumhara test 👀'''
# numbers = [3,1,4,2]
# print(sorted(numbers))
# print(numbers)
# output = [1, 2, 3, 4]
#         [3, 1, 4, 2]

# test 2 
# numbers = [10,2,33,4]
# numbers.sort()
# print(numbers)

'''🔹 5️⃣ List Practice
	21.	5 numbers ki list banao aur unka sum nikaalo.'''
# numbers = [73,94,8,35,78]
# print(sum(numbers))

'''	# 22.	List me sabse bada aur sabse chhota number find karo.'''
# print(min(numbers))
# print(max(numbers))
'''	# 23.	Ek list me se duplicate remove karo.'''
# numbers = [10, 5, 20, 5, 3, 10]
# numbers = list(set(numbers))
# print(numbers)

'''	#duplicate dekhne ke liye method 1'''
# numbers = [10, 5, 20, 5, 3, 10]

# if len(numbers) != len(set(numbers)):
#     print("Duplicates present")
# else:
#     print("No duplicates")
'''    #medthod 2'''
# numbers = [10, 5, 20, 5, 3, 10]

# seen = set()
# duplicates = set()

# for num in numbers:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)
# print("Duplicate numbers:", list(duplicates))

'''# 24.	List ko ascending order me sort karo.'''
# numbers = [10, 5, 20, 5, 3, 10]
# numbers.sort()
# print(numbers)
'''# 25.	List me sirf even numbers ka new list banao.'''