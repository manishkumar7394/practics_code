'''# 🟢 Level 1: Python Basics (1–30)
# 	1.	Print "Hello World" in Python.'''
# print("hello world")
'''
# 	2.	Print your name and age in one line.'''
# name= "manish paswan" 
# age = 24
# print(f"my name is {name}, and my age{age}")

'''# 	3.	Create two variables and print their sum.'''
# a = 50
# b= 100
# print(f"sum = {a+b}")

'''# 	4.	Take input from user and print it.'''

# user_details= input("Enter your sort details")
# print(user_details)

'''# 	5.	Convert user input string into integer.'''
# user= (input("enter data"))
# convert = int(user)
# print(type(convert))
'''
# 	6.	Swap two numbers. exchenge '''
# first_name = "manish"
# last_name = "paswan"
# first_name,last_name= last_name,first_name
# print(first_name,last_name)
'''
# 	7.	Check if a number is even or odd.'''
# number = int(input('enter number' ))
# if number %2==0 :
#     print("even")
# else:
#     print("odd")

'''# 	8.	Find the largest of two numbers.'''
# num1= 50
# num2= 34
# if num1 >num2:
#     print(f"largest num1 = {num1}")
# else:
#     print(f"largest num2 = {num2}")

'''# 	9.	Find the largest of three numbers.'''
# a= 12
# b= 34
# c= 22
# print(max(a,b,c))                # this is simple method 
# if a >b and a>c:
#     print(f"largest value a {a}")
# elif b>c and b>a:
#     print(f"largest values b {b}")
# else:
#     print(f"largest vlue c {c}")

'''
# 	10.	Check if a number is positive, negative, or zero.'''
# user= int(input("enter first num"))

# if user >0:
#     print(f"this num is positive {user}")
# elif user <0:
#     print(f"this num is nagetive : {user}")
# else:
#     print(f"this value is zero:{user}")

'''# 	11.	Calculate the area of a circle.'''
# area = pi* r2     (pi * (r*r))
# pi = 3.14
# r= redius 
# r = 5
# area= 3.14* r*r
# print("area of circle :", area)
'''
# 	12.	Calculate the simple interest.'''
# si = p*r*t/100          #p = principle(orginal money), r= rate, t= time
# p =10000
# r= 15
# t = 2
# si = (p*r*t)/100
# print("simple intrest:",si)

'''# 	13.	Convert Celsius to Fahrenheit.'''
# c= 25
# F = (C \times 9/5) + 32                 #c= celsius , f = fahrenhiet ,1c = 33.8f
# print("fahrenhiet :",f)
'''
# 	14.	Convert kilometers to miles.
	# 1 Kilometer ≈ 0.621371 Miles'''
# km = 10
# miles = km* 0.621371
# print("miles:",miles)

'''# 	15.	Find the square of a number.'''
# n = 5
# Square = n * n
# print("square:", Square)
'''
# 	16.	Find the cube of a number.'''
# n = 5 
# cube = n*n*n
# print("cube:",cube)
'''
# 	17.	Calculate the average of three numbers.'''
# a = 10
# b= 20
# c= 343
# avg= (a+b+c)/3
# print("avg:",avg)


'''# 	18.	Check if a number is divisible by 5.'''
# num = 1
# if num %5== 0:
#     print(f"this num is divisible by 5:")
# else:
#     print(f"this is not divisible by 5:") 

'''# 	19.	Find the remainder of two numbers.'''
# a= 11
# b= 2
# remainder = a%b
# print("remainder:", remainder)						#remainder = 1 

'''# 	20.	Print ASCII value of a character.'''
# A =65
# S= 32
# I= 23
# character  = 'I'
# print("ASCII value:",ord (character))

'''# 	21.	Find the datatype of a variable.'''
# num = 445
# print(type(num))
'''# 	22.	Convert float to integer.'''
# num= 10.5
# int = int(num)
# print(type(int))
'''# 	23.	Convert integer to string.'''
# value = 23
# str = str(value)
# print(type(str))
'''# 	24.	Check if a number is multiple of 3.'''
# num = 9

# if num % 3 == 0:
#     print("Number is multiple of 3")
# else:
#     print("Number is not multiple of 3")
    
'''# 25.	Find the maximum of three numbers using max().'''
# a= 234
# b =23
# c = 33
# d= 243
# print(max(a,b,c,d))

'''# 	26.	Find the minimum of three numbers using min().'''
# print(min(a,b,c,d))

'''# 	27.	Print the length of a string.'''
# str = "manish paswan"
# print(len(str))
'''
# 	28.	Print first and last character of a string.'''
# text = "python"
# print("first charecter of:", text[0])
# print("second charecter of:", text[-1])
'''# 	29.	Concatenate two strings.'''
# str_1 = "manish"
# str_2 = "paswan"
# result = str_1 +" "+ str_2
# print(result)
'''# 	30.	Repeat a string 5 times.'''
# text = "Hello "

# print(text * 5)
# ⸻

'''# 🟡 Level 2: If-Else Practice (31–60)'''
'''# 	31.	Check if a number is even or odd using if-else.'''
# user= int(input("Enter a number"))
# if user %2== 0 :
#     print("even")
# else:
#     print("odd")

'''# 	32.	Check if a year is leap year.'''
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

'''# 	33.	Check if a person is eligible to vote.'''
# age = int(input("write your age"))
# if age>18:
#     print("Eligible to vote")
# else:
#     print("not eligible for that")
    
'''# 	34.	Check if a number is divisible by both 3 and 5.'''
# num = int(input("user"))
# if num %3== 0 and num%5==0 :
#     print("divigible for that")
# else:
#     print("not divigible")
    
'''# 	35.	Check the largest of three numbers using nested if.'''

# a= int(input("first num"))
# b =int(input("second num"))
# c = int(input("third num"))
# if a > b :
#     if a>c:
#         print("largest num ", a)
#     else:
#         print("largest num ",c)
# else:
#     if b>c:
#         print("largest num of:", b)
#     else:
#         print("largest num is :",c)

'''# 	36.	Check if a number is in range 1–100.'''
# num = int(input("enter a number :"))

# if 1<= num<= 100:
#     print("number is in range 1 to 100 :")
# else:
#     print("number is not in range:")

'''# 	37.	Create a simple calculator using if-else.'''
# num1= int(input("enter your 1 number :"))
# num2= int(input("enter your 2 number :"))
# operation = input("enter your op (+,-,*,/ , )")

# if operation == "+":
#     print("result:",num1+num2)
# elif operation == "-":
#     print("result:", num1 - num2)
# elif operation == "*":
#     print("result:", num1 * num2)
# elif operation == "/":
#     print("result:", num1 / num2)
# else :
#       print("invailid operarion")


'''# 	38.	Check if a character is vowel or consonant.'''
# char = input("enter character :")
# if char in "aeiouAEIOU":
#     print("it is a vowel")
# else:
#     print("it is a consonant")

'''# 	39.	Check if a number is positive or negative.'''
# num = int(input("enter a num"))
# if num >= 0 :
#     print("positive ")
# else :
#     print("nagative")

'''# 	40.	Check if a number is multiple of 7.'''
# num = int(input("Enter a number: "))

# if num % 7 == 0:
#     print("Number is a multiple of 7")
# else:
#     print("Number is not a multiple of 7")

'''# 	41.	Determine grade from marks.'''
# marks = int(input("enter a marks: "))
# if marks < 0 or marks >100 :
#       print("invailid marks")
# elif 70<=  marks <=100 :
#           print("grade 'A' ")
# elif marks > 50:
#     print("gread 'B' ")
# else :
#     print("gread 'C' ")

'''# 	42.	Check if a number is divisible by 2 but not by 5.'''
# num = int(input("enter a number :"))
# if num %2 == 0 and num %5 != 0:
#     print("this is divided by 2 but not 5 :")
# else :
#     print("this is not divid")
    
'''# 	43.	Find smallest among three numbers.n'''
# num = int(input("enter num :"))
# num1 = int(input("enter b num :"))
# num2 = int(input("enter c num :"))
# if num < num1 :
#     print("num a is smalest num:")
# elif num1 <num2 :
#     print("num 1 b is smalest num :")
# else :
#     print("c is smalest num :")

'''
# 	44.	Check if number is two-digit or three-digit.
# 	45.	Check if a character is uppercase or lowercase.'''

'''
# 	46.	Check if a number is palindrome.
# 	47.	Find absolute value of a number.
# 	48.	Check if triangle is valid.
# 	49.	Find type of triangle (equilateral, isosceles, scalene).
# 	50.	Check if a number is Armstrong number'''

'''# 	51.	Check if two numbers are equal.'''
# num = int(input("enter yr 1 numver "))
# num1 = int(input("enter yr 2 num"))

# if num == num1 :
#     print("this is equal num :")
# else :
#     print("not equals")
    

'''# 	52.	Find sign of multiplication result.'''
# 	53.	Check if a number is prime.

'''
# 	54.	Check if a number is divisible by 11.'''
# num = int(input("hello pls enter your randam number")) 
# if num %11== 0 :
#     print("yes its divisible")
# else :
#     print("not divisible")
'''
# 	55.	Find biggest among four numbers.'''
# manish = int(input("pls manish enter your num firstly: "))
# aman = int(input("hello mr.aman pls enter your num second:"))
# divya = int(input("hello divya pls enter your num third:"))
# vashu = int (input("hey vashu enter your num last :"))

# if manish >= aman and manish >= divya and manish > vashu:
#     print(f"manish is bigger num :")
# elif aman >= divya and aman >= vashu and aman >=  manish :
#     print("aman is bigger num :")
# elif divya>= vashu and divya >= manish and divya >= aman :
#     print("divya is bigger num :")
# else :
#     print("vashu is biger ")

'''# 	56.	Check if a number is perfect square.'''
'''
# 	57.	Check if age is teenager.'''

# age = int(input("enter your age:"))
# if 1<= age >= 100:
#     print(f"your age not vailid {age}")
# elif 18 <=  age <= 29 :
#     print(f"now you'r teenager {age}")
# elif age >= 30:
#     print(f"you are a become man : {age}")
# else :
#     print(f"you'r not teenager {age}")

'''# 	58.	Check if number ends with 5.
# 	59.	Compare two strings.
# 	60.	Check if string is empty.
'''

# ⸻

'''# 🔵 Level 3: Loops (61–100)'''
'''# 	61.	Print numbers from 1 to 10.'''
# for i in range(1,11):
#     print(i)

'''# 	62.	Print numbers from 10 to 1.'''
# for i in range(10,0,-1):
#     print(i)
'''# 	63.	Print even numbers from 1–50.'''
# for i in range(1,51):
#     if i %2== 0 :
#         print(i)
'''# 	64.	Print odd numbers from 1–50.'''
# for i in range(1,51):
#     if i %2!= 0:
#         print("odd",i)
'''# 	65.	Find sum of numbers from 1–100.'''
# total = 0
# for i in range(1,101):
#     total = total+i
# print("sum is that:", total)

'''# 	66.	Find factorial of a number.'''
# admin = int(input("enter a factorial number:"))
# fact = 1
# for i in range(1,admin+1):
#     fact =fact * i
#     print(fact)

'''# 	67.	Print multiplication table of a number.'''
# table = int(input("create a table :"))
# for i in range (1,11):
#     print(f"{table}*{i}= {table*i}")


'''# 	68.	Print Fibonacci series.'''
# n = int(input("Enter how many numbers: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

'''# 	69.	Count digits in a number.'''
# num = int(input("enter the num"))
# count= 0
# while num != 0:
#     num = num // 10
#     count += 1

# print("Total digits:", count)

'''# 	70.	Reverse a number.'''
# for i in range(10,0,-1):
#     print(i)
'''# # 	71.	Check if number is palindrome.'''
# num = int(input("Enter a number: "))
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")
    
'''# 	72.	Print all prime numbers between 1–100.'''

# 	73.	Find sum of digits of a number.
# 	74.	Find product of digits of a number.
# 	75.	Print pattern of stars.
# 	76.	Print triangle pattern.
# 	77.	Print square pattern.
# 	78.	Print pyramid pattern.
# 	79.	Print inverted pyramid.
# 	80.	Print multiplication tables from 1–10.
# 	81.	Find GCD of two numbers.
# 	82.	Find LCM of two numbers.
# 	83.	Print numbers divisible by 3 between 1–100.
# 	84.	Find largest digit in a number.
# 	85.	Find smallest digit in a number.
# 	86.	Count number of vowels in string.
# 	87.	Count consonants in string.
# 	88.	Print reverse of a string.
# 	89.	Check if string is palindrome.
# 	90.	Print ASCII values of characters.
# 	91.	Count spaces in a string.
# 	92.	Print numbers divisible by 7.
# 	93.	Print cubes of numbers from 1–10.
# 	94.	Print squares of numbers from 1–10.
# 	95.	Count words in a sentence.
# 	96.	Find sum of even numbers.
# 	97.	Find sum of odd numbers.
# 	98.	Print first n natural numbers.
# 	99.	Print sum of series 1+2+3+…+n.
# 	100.	Print multiplication table in reverse.

# ⸻


'''
# 🟣 Level 4: Data Structures (101–150)

# List
# 	101.	Create a list and print it.'''
# num= [12,34,45,56,678]
# print(num)

'''# 	102.	Find length of list.'''
num = [13,45,5,66,7,78]
# print(len(num))

'''# 	103.	Find maximum element in list.'''
# print(max(num))
'''# 	104.	Find minimum element in list.'''
# print(min(num))
'''# 	105.	Find sum of list elements.'''
# print(sum(num))

'''# 106.	Sort list in ascending )order.'''
# num = [13,45,5,66,7,78]
# num.sort()
# print(num)
'''# 	107.	Sort list in descending order.'''
# num = [13,45,5,66,7,78]
# num.sort(reverse=True)
# print(num)
'''# 	108.	Reverse a list.'''
# num = [13,45,5,66,7,78]
# num.reverse
# print(num)

'''# 	109.	Remove duplicates from list.'''
# num = [13,45,45,5,66,7,7,78]
# unique = list(set(num))
'''# 	110.	Find second largest element.'''
# num = [13,45,45,5,66,7,7,78]
# num = list(set(num))			#duplicate remove
# num.sort()
# print("second largest num:",num[-2])
'''
# 	111.	Merge two lists.'''
# num1 = [13,45,45,5,66,7,7,78]
# num2 = [12,34,5,46,68,98,22]
# new = num1 + num2			# num1.extend(num2)
# print(new)
'''# 	112.	Find common elements between two lists.'''
# num1 = [13,45,45,5,66,7,7,78]
# num2 = [12,34,5,46,68,98,22]
# common = []

# for i in num1:
#     if i in num2 and i not in common:
#         common.append(i)

# print(common)

'''# 	113.	Remove element from list.'''
# num1 = [13,45,45,5,66,7,7,78]
# num1.remove(13)
# print(num1)
'''# 	114.	Insert element at specific position.'''
# num1 = [13,45,45,5,66,7,7,78]
# num1.append(12)
# print(num1)

'''# 	115.	Find index of element.'''
# num1 = [13,45,45,5,66,7,7,78]
# position =num1.index(66)
# print(position)


# Tuple
'''# 	116.	Create a tuple.'''
# num = (23,34,45,56,23)
# print(num)
'''# 	117.	Convert tuple to list.'''
# num = (23,34,45,56,23)
# newlist = list(num)
# print(newlist)
'''# 	118.	Find length of tuple.'''
# num = (23,34,45,56,23)
# print(len(num))
'''# 	119.	Find maximum element in tuple.'''
# num = (23,34,45,56,23)
# print(max(num))
'''# 	120.	Unpack tuple values.'''
# num = (12,35,5)
# a, b, c = num
# print(a)
# print(b)
# print(c)



'''# Set
# 	121.	Create a set.'''
# num = {23,34,57,3,24,57}
# print(num)
'''# 	122.	Add element to set.'''
# num = {23,34,3,24,57}
# num.add(33)
# print(num)

'''# 	123.	Remove element from set.'''
# num = {23,34,57,3,24,57}
# num.remove(57)
# print(num)

'''# 	124.	Find union of two sets.'''
# -
'''# 	125.	Find intersection of two sets.'''
# num = {23,34,57,3,24,57}
# num1 = {2,34,54,6,43,33}
# intersection = num.intersection(num1)
# print(intersection)


'''# Dictionary
# 	126.	Create dictionary.'''
# detail = {
#     "name": "manish paswan",
# 	"age": 24,
#     "dob": "10-12-2002",
#     "add": "lucknow"
# }
# print(detail)
'''# 	127.	Access dictionary values.'''
# details = {"name": "manish paswan", "age":24,"city": "lucknow"}
# print(details["age"])

'''# 	128.	Add new key-value pair.'''
# details = {
#     "name": "manish paswan", "age": 24
# }
# details["city"] = "lucknow"
# print(details)
'''# 	129.	Update dictionary value.'''
# details = {
#     "name": "manish paswan", "age": 24}
# details["age"] = 20
# print(details)
'''# 	130.	Delete dictionary key.'''
# details = {"name": "manish paswan", "age":24,"city": "lucknow"}
# del details["city"]
# print(details)

'''# 	131.	Print all keys.'''
# details = {"name": "manish paswan", "age":24,"city": "lucknow"}
# print(details.keys())

'''# 	132.	Print all values.'''
# details = {"name": "manish paswan", "age":24,"city": "lucknow"}
# print(details.values())

'''# 	133.	Print key-value pairs.'''
# details = {"name": "manish paswan", "age":24,"city": "lucknow"}
# for key, value in details.items():
#     print(key, value)
    
'''# 	134.	Count number of keys.'''
# details = {"name": "manish paswan", "age":24,"city": "lucknow"}
# print(len(details))
'''# 	135.	Merge two dictionaries.'''
# d1 = {"a":1, "b":2}
# d2 = {"c":3, "d":4}

# d1.update(d2)
# print(d1)

'''# More Practice
# 	136.	Find duplicate elements in list.'''
# num = [23,34,54,43,3,4,34,43]
# duplicate = []
# for i in num:
#     if num.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)
# print("Duplicate elements:", duplicate)

'''# 	137.	Remove duplicates from list.'''
# num = [23,34,54,43,3,4,34,43]
# unique = list(set(num))
# print("Remove duplicates from list",unique)

'''# 	138.	Count frequency of elements in list.'''
# num = [23,34,54,43,3,4,34,43]

# freq = {}

# for i in num:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

'''# print(freq)'''

'''# 	139.	Find common elements in two lists.'''
# num = [11,23,11,45,50,23]
# num1= [11,12,13,44,23,45]


# 	140.	Rotate list elements.
# 	141.	Flatten nested list.
# 	142.	Check if list is sorted.
# 	143.	Find missing number in list.
# 	144.	Find intersection of lists.
# 	145.	Convert list to dictionary.
# 	146.	Convert dictionary to list.
# 	147.	Sort dictionary by keys.
# 	148.	Sort dictionary by values.
# 	149.	Reverse dictionary.
# 	150.	Count characters in string using dictionary.

'''# ⸻

# 🔴 Level 5: Advanced Python (151–200)'''
'''# 	151.	Create a function to add two numbers.'''
# def add (a,b):
#     return a+b
# print(add(5,3))
# print(add(23,243))
# print(add(2330,234))

'''# 	152.	Create function to check prime number.'''
# def check_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return "not prime"
#         return "prime"
# print(check_prime(5))

'''# 	153.	Write recursive function for factorial'''
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

'''# 	154.	Write recursive Fibonacci function.'''
# def fibonacci(n):
#     if n <= 1:
#         return n 
#     return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci (6))

'''# 	155.	Write lambda function for square'''
# square = lambda x: x*x
# print(square(5))
# 	156.	Use map() to square list numbers.

# 	157.	Use filter() to get even numbers.

# 	158.	Use reduce() to find sum.

# 	159.	Create generator function.

# 	160.	Create decorator function.

'''# File Handling'''
# 	161.	Create file and write text.
# 	162.	Read file content.
# 	163.	Append data to file.
# 	164.	Count lines in file.
# 	165.	Count words in file.

'''# Exception Handling'''
# 	166.	Handle divide by zero error.
# 	167.	Handle file not found error.
# 	168.	Create custom exception.
# 	169.	Use try-except-finally.
# 	170.	Handle multiple exceptions.

'''# OOP'''
'''# 	171.	Create a class and object.'''
# class students:
#     name = "manish paswan"
#     age = 24
#     city = "baskhari"
# s1= students()							#object
# print(s1.name)
# print(s1.age)
# print(s1.city)

'''# 	172.	Create class with constructor.'''
# class students :
#     def __init__(self, name, age ,city):
#         self.name= name
#         self.age = age
#         self.city= city
# s1 = students("manish" , 24,"lucknow")
# s2 = students("abhay", 22,"ambedkar nagar")
# print(s1.name)
# print(s2.city)

'''# 	173.	Implement inheritance.'''
# class Animal:
#     def speak(self):
#         print("animal speaks")
    
# class dog(Animal):
#     def bark(self):
#         print("dog barks")


# d = dog()
# d.speak()
# d.bark()


    
'''
# 	174.	Implement multiple inheritance.'''
# class Animal:
#     def speak(self):
#         print("animal speaks")
    
# class dog(Animal):
#     def bark(self):
#         print("dog barks")
# class cat (Animal):
#     def maauu(self):
#         print("cat maauu")
# c = cat()
# d = dog()
# d.speak()
# d.bark()
# c.maauu()

'''# 	175.	Implement method overriding.'''

'''
# 	176.	Implement encapsulation.'''
# class Bank:

#     def __init__(self, balance):
#         self.__balance = balance

#     def show(self):
#         print(self.__balance)

# b = Bank(15000)

# b.show()

'''# 	177.	Implement polymorphism.'''
# class cat:
#     def sound(self):
#         print("meow")
# class dog:
#     def sound(self):
#         print("bark")

# for animal in (cat(), dog()):
#     animal.sound()
    
'''# 	178.	Create abstract class.'''
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("dog barks")
# d= Dog()
# d.sound()



'''# 	179.	Create class method.'''
# class student:
#     school = "abc school"
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
    
# student.show_school()
'''# 	180.	Create static method.'''
# class Math:

#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Math.add(5,3))

'''# Advanced Logic
# 	181.	Find second largest number without sort.'''
# 	182.	Check if two strings are anagrams.
# 	183.	Find longest word in sentence.
# 	184.	Find most frequent element in list.
# 	185.	Implement binary search.
# 	186.	Implement bubble sort.
# 	187.	Implement selection sort.
# 	188.	Implement insertion sort.
# 	189.	Implement stack using list.
# 	190.	Implement queue using list.
# 	191.	Reverse words in sentence.
# 	192.	Find duplicate characters in string.
# 	193.	Count frequency of characters.
# 	194.	Remove spaces from string.
# 	195.	Find first non-repeating character.
# 	196.	Find intersection of two lists.
# 	197.	Find missing number in array.
# 	198.	Implement linear search.
# 	199.	Convert list to string.
# 	200.	Create simple command-line calculator.