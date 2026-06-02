'''🔹 Dictionary kya hoti hai?

👉 Dictionary me data key : value pair me store hota hai.
👉 Curly brackets {} use hote hain.
example:
'''
student = {
    "name": "manish",
    "age":  24,
    "course":   "python"
}
# print(student)          #output = {'name': 'manish', 'age': 24, 'course': 'python'}
'''
🔹 Value kaise access karein?
List me index use hota tha.
Dictionary me key use hoti hai.'''

# print(student["name"])          #output= "manish"

#value chenge kaise kre ?
# student["age"] = 20
# print(student)
# output
# {'name': 'manish', 'age': 20, 'course': 'python'}
# new key add 
# student["city"]= "kanpur"
# print(student)

'''# 🔹 Important Methods
# 1.keys
print(studnet.keys())                   saari keys show krega

2️⃣ values()
print(student.values())                 show all values

3️⃣ items()
print(student.items())                  key + values dono pair me dikhaiga'''

# test 1
# student = {
#     "name" : "rahul",
#     "age":  21
# }

# student["age"] = 25
# student["city"] = "delhi"
# print(student)
# output
# {'name': 'rahul', 'age': 25, 'city': 'delhi'}

# test 2
# student = {
#     "name": "Manish",
#     "marks": 80
# }
# print(student.get("age"))
# output is none

# test 3
# student= {
#     "name": "Amit",
#     "marks": 90
# }
# student.pop("marks")
# print(student)
# output is that {'name': 'Amit'}

# test 4
# student = {
#     "name": "Amit",
#     "marks": 90
# }

# value = student.pop("marks")
# print(value)
# print(student)
# output 
# 90
# {'name': 'Amit'}
