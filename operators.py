# 2️⃣ Comparison Operators (True / False dete hain)
 a = 10
 b = 5
print(a>b) true
print(a<b)  false
print(a==b) equal chech false
print(a!=b)  not equal True
print(a>=b) 
print(a<= b)

# 🟢 3️⃣ Logical Operators
# # Ye conditions combine karte hain.
 age = 25
 print(age> 18 and age<30) #output is true 
 print(age>18 or age>60)
 print(not(age>18))  #false
# 🔥 Simple meaning:
# 	•	and → dono condition true
# 	•	or → koi ek true
# 	•	not → ulta kar deta hai
# 🟢 4️⃣ Assignment Operators
 x = 5
 x -= 2
 print(x)

# 🧠 Mini Practice (Ab tum karo)
# Program banao jo:
# 	•	User se number le
# 	•	Check kare:
# 	•	Agar number 100 se bada hai → print “Big number”
# 	•	Agar 50 se bada hai → print “Medium number”
# 	•	Warna → print “Small number”

 number = int(input("enter number"))
 if number > 100:
     print(f"{number} big number")
	 elif number > 50: 
     print(f"{number} medium number")
else :
     print(f" {number} small number")

# 🔥 Ab Thoda Twist (Mini Challenge Level 2)
# Program banao jo:
# 	•	User se 3 numbers le
# 	•	Sabse bada number print kare
 num_1 = int(input("enter first number"))
 num_2 = int(input("enter second number"))
 num_3 = int(input("enter last third number"))

 if num_1 > num_2 and num_1 > num_3 :
     print(f"{num_1} is largest number")
	 elif num_2 > num_1 and num_2 > num_3 :
    print(f" {num_2} is largest number")
 else :
     print(f"{num_3} is largest number")

'''   🔹 2️⃣ If Else Practice
	6.	Ek number lo aur check karo:
	•	positive
	•	negative
	•	zero '''
 num = int(input("enter the numbers"))
 if num > 1:
     print(f"the num is positive {num}")
 elif num < -1 :
     print(f"num is nagative {num}")
 else :
     print(f"the num is zero {num}")

'''# 7.	Ek number lo aur check karo even hai ya odd.'''

 number =  int(input("enter the number"))
 num = number
 if num % 2 == 0:                  #it means jo number hm use krnge wo 2 se pura divide ho jai

     print("Even")
 else :
     print("odd")

'''	8.	Student ke marks lo:
	•	90+ → Grade A
	•	75–89 → Grade B
	•	50–74 → Grade C
	•	below 50 → Fail'''


 user_num = int(input("enter your marks"))
 marks = user_num
if marks >= 90:
    print("grade A")
elif marks >= 75:
     print("grade B")
elif marks >= 50 :
     print("grade c")
else :
     print("fail")

'''9.	Teen numbers me sabse bada number find karo.'''

num1 = int(input("enter first num"))
num2 = int(input("Enter sec num"))
num3 = int(input("Enter third num"))
if num1 > num2 :
    print(f"its largest num1 {num1} ")
elif num2 >num3:
    print(f"its largest num2 {num2} ")
else :
    print(f"its largest num3 {num3} ")

'''10.	Password check karo:
Agar password == “admin123” to “Login Successful” print karo, warna “Wrong Password”.'''
 password = "admin123"
user = input("Enter your pass")
 if user == password:
     print("loning successfully")
else :
     print("wrong try again")
