'''Loop ka matlab hai:

👉 Ek kaam ko baar-baar repeat karna bina code ko 10 baar likhe.
Example:
Agar tumhe 1 se 5 tak print karna hai, bina loop ke:
print(1)
print(2)
print(3)
print(4)
print(5)        #its wrong way'''

'''# # 🟢 1️⃣ For Loop'''

# for i in range (1,10):
#     print(i)
'''
# 🟢 2️⃣ While Loop'''
# num = 10
# while num <= 30:
#     print(num)
#     num += 3
# Program banao jo:
# 	•	1 se 10 tak numbers print kare
# 	•	Har number ke baad “Manish” print kare

# for i in range (1, 11):
#     print(f"{i} Manish")
'''# 🚀 Next Mini Challenge'''
# Program banao jo:
# 	•	1 se 10 tak numbers print kare
# # 	•	Sirf even numbers print kare
# num = 2
# while num <= 10:
#     print(num)
#     num += 2
'''
# ''''🔥 Ab Thoda Level Up'''''''
# Program banao jo:
# 	•	User se ek number le
# 	•	1 se lekar us number tak table print kare

# number= int(input("enter number"))
# for i in range (1, 11):
#     print(f"{number}*{i}= {number*i}")

# # 🔹 Reverse Table (10 se 1 tak)
# number= int(input("enter a number"))
# for i in range (10, 0, -1 ):
#     print(f"{number}*{i} = {number*i}")

'''# 🔥 Ab Tumhara Challenge'''
# Program banao jo:
# 	•	1 se 20 tak numbers print kare
# 	•	Sirf odd numbers print kare

# number = int(input ("enter your number"))
# for i in range (1,21):
#     if i % 2 !=0:
#         print(i)

'''# 🟢 1️⃣ Break kya hota hai - break loop ko turant rok deta hai.
# for i in range (1,11):
#     if i == 5:
#         break
#     print(i)'''
# output
# 1
# 2
# 3
# 4       Jaise hi i == 5 hua → loop band ❌

'''# 🟢 2️⃣ Continue kya hota hai?
# for i in range (1,11) :
#     if i == 5:
#         continue
#     print(i)'''
#     output 1,2,3,4,6,7,8,9,10
#     yaha 5 skip ho gya 

#  Mini Challenge
# Program banao jo:
# 	•	1 se 20 tak numbers print kare
# 	•	Jab number 13 aaye → print “Unlucky” aur loop stop ho jaye
# number =int(input("enter the number"))
# for i in range (1,20):
#     if i ==13:
#         print("unlucky")
#         break
#     print(i)

'''🟢 Nested Loop Kya Hota Hai?
Jab ek loop ke andar doosra loop ho — use kehte hain nested loop.
for outer in range(....):
for inner in range (....):'''

#  simple example 
# for i in range (1,5):
#         for j in range (1,5):
#             print(i,j)
# 🧠 Samjho kaise chal raha hai

# Outer loop = 1
# → Inner loop 1 se 4 tak pura chalega

# Fir outer = 2
# → Inner phir 1 se 4

# Matlab inner loop har baar complete run karta hai.
'''# # 🔥 Practical Example (Table 1 to 3)'''
# for i in range (1,11):
#     print(f"table of {i}")
#     for j in range (1,11):
#         print(f"{i}*{j}= {i*j}")
#         print()

# 🟢 Pattern Printing (Star Pattern ⭐)
'''for i in range(1, 6):
    for j in range(i):
        print("*", end=" ") #end=" " iska mtlb line break nii hoga same line me print hoga
    print()
 output is
* 
* * 
* * * 
* * * * 
* * * * * '''


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print("*", end= " ")
#     print()

''' 	•	Outer loop → rows control karta hai
	•	Inner loop → columns / pattern control karta hai
	•	range(i) → har row me i baar print'''

# reverse: pattern
# for i in range(6,0,-1):
#     for j in range(6- i):
#         print(i,end= " ")
#     print()

'''# tringle pattern  
    *
   * *
  * * *
 * * * *
* * * * *
            '''
# for i in range(1, 6):
#     # Print spaces
#     for space in range(5 - i):
#         print(" ", end = "")
#     # Print stars
#     for star in range(i):
#         print("* ", end= "")
#     print()

'''🔹 3️⃣ Loops Practice
	11.	1 se 20 tak even numbers print karo.'''
# for i in range (1,21):
#     if i % 2 == 0 :
#         print (i)

	# 12.	1 se 10 tak numbers ka sum nikaalo.
'''total = 0

for i in range(1, 11):
    total = total + i

print("Sum is:", total)'''

# 13.	5 ka table print karo.
# table = int(input("Enter table number :"))
# for i in range(1,11):
#     print(f"{table}*{i} = {table*i}")


'''	14.	1 se 50 tak jitne numbers 3 se divisible hain wo print karo.'''
# num = 50
# for i in range(1,51):         #1
#     if i %3 == 0:
#         print(i)
# for i in range(1,51,3):          #2
#     print(i)

	# 15.	Ek number lo aur uska factorial nikaalo.
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i 
# print("factorial is:",fact)
