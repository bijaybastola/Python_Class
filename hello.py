# print("Hello Github!")

# print("Hello World!")
# print("One", "Two")
# print("One", "Two", sep="-")
# print("HEllo", end="!!")

# name = input("Enter your name: ")
# print("Hello", name)

# age = int(input("Enter your age: "))
# height = float(input("Height in meters: "))
# print(age, height)

# print("""Hello

# World!""")

# item1 = 10
# item2 = 20
# item3 = 30

# total = (item1 * 2
#          + item2 * 3
#          + item3 * 4)
# print(total)

# total = 10+20+\
#         30+40+\
#         50
# print(total)

# print("Mon\"day", "tues\nday",
#       "Wednesday")

# test1 = float(input("Enter your test1 score: "))  
# test2 = float(input("Enter your test2 score: "))
# test3 = float(input("Enter your test3 score: "))

# print(test1)

# #calculate the avg score
# avearge = (test1 + test2 + test3) / 3
# print("Your average test score is :", avearge)

# student = "Jonny"
# print(f"Hello {student} !")


#Exercise No. 2

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# #Calculating sum of two numbers
# sum = num1 + num2
# #Calcualating their product
# product = num1 * num2

# print(f"Sum is: {sum:.1%} and product is : {product:.2f}")

# total_ratio = 0.8544
# print(f"{total_ratio:.1%}")

#Exercise 3.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# #Calcuate the BMI of a person
# bmi = weight / (height**2)
# print(f"Your BMI value is : {bmi:.2f}")

if height <= 0 or weight <= 0:
    print("Weight and height must be greater than zero.")
else:
    #Calcuate the BMI of a person
    bmi = weight / (height ** 2)
    print(f"Your BMI value is : {bmi:.2f}")