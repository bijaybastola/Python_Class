#Pratice 
#Greet the User by Name​

name = input("Enter your first and last name : ")
space = name.find(" ")
first_name = name[ : space]
last_name = name [space + 1: ]
print(f"Hi {first_name.capitalize()} {last_name.capitalize()}!")

#FUCNTONS
# print(round(34.4))

# def print_highest_mark(marks):
#     print(max(marks))

# def highest_mark(marks):
#     return max(marks)

# marks = [78, 92, 85]

# print_highest_mark(marks)
# top = highest_mark(marks)
# print(top + 5)

#METHODS

# s = "hello world"
# print(s.capitalize())
# print(s.find("world",0, 13))
# print(s.lower())
# print(s.upper())
# print(s.startswith("world", 6))
# print(s.split(' '))
# s = "Hello {name}, you are {age} years old."
# print(s.format(name = "Alice", age = 30))

