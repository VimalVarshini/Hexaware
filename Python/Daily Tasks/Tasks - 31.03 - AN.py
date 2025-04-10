# Task 1 : Calculate the tax
# income = float(input("Enter taxable income: "))
# if income <= 150000:
#     tax = 0
# elif income <= 300000:
#     tax = 0.1 * (income - 150000)
# elif income <= 500000:
#     tax = 15000 + 0.2 * (income - 300000)
# else:
#     tax = 55000 + 0.3 * (income - 500000)
# print(f"Total tax payable: {tax}")

# Task 2 : Calculate the roots of a quadratic equation.
# import math
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# d = b**2 - 4*a*c
# if d > 0:
#     root1 = (-b + math.sqrt(d)) / (2*a)
#     root2 = (-b - math.sqrt(d)) / (2*a)
#     print(f"Real and distinct roots: {root1}, {root2}")
# elif d == 0:
#     root = -b / (2*a)
#     print(f"Equal roots: {root}")
# else:
#     real_part = -b / (2*a)
#     imag_part = math.sqrt(abs(d)) / (2*a)
#     print(f"Imaginary roots: {real_part} ± {imag_part}i")

# Task 3: Calculate total, average, and grade
# sub1 = float(input("Enter marks for subject 1: "))
# sub2 = float(input("Enter marks for subject 2: "))
# sub3 = float(input("Enter marks for subject 3: "))
# total = sub1 + sub2 + sub3
# average = total / 3
# if average >= 80:
#     grade = "A"
# elif average >= 70:
#     grade = "B"
# elif average >= 60:
#     grade = "C"
# else:
#     grade = "Fail"
# print(f"Total: {total}, Average: {average}, Grade: {grade}")

# Task 4: Bonus calculation
# salary = float(input("Enter salary: "))
# service = int(input("Enter years of service: "))
# if service >= 10:
#     bonus = 0.1 * salary
# elif service >= 5:
#     bonus = 0.05 * salary
# elif service >= 3:
#     bonus = 0.03 * salary
# else:
#     bonus = 0
# print(f"Bonus amount: {bonus}, Total salary: {salary + bonus}")

# Task 5: Arithmetic operations
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /): ")
# match operation:
#     case "+":
#         print(f"Result: {num1 + num2}")
#     case "-":
#         print(f"Result: {num1 - num2}")
#     case "*":
#         print(f"Result: {num1 * num2}")
#     case "/":
#         print(f"Result: {num1 / num2 if num2 != 0 else 'Division by zero error'}")
#     case _:
#         print("Invalid operation")

# Task 6: Calculate area
# import math
# choice = int(input("Enter choice (1: Circle, 2: Triangle, 3: Rectangle): "))
# match choice:
#     case 1:
#         radius = float(input("Enter radius: "))
#         print(f"Area of Circle: {math.pi * radius ** 2}")
#     case 2:
#         a = float(input("Enter side a: "))
#         b = float(input("Enter side b: "))
#         c = float(input("Enter side c: "))
#         s = (a + b + c) / 2
#         area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#         print(f"Area of Triangle: {area}")
#     case 3:
#         length = float(input("Enter length: "))
#         breadth = float(input("Enter breadth: "))
#         print(f"Area of Rectangle: {length * breadth}")
#     case _:
#         print("Invalid choice")


# Task 7: Sum of numbers from m to n
# m = int(input("Enter start number: "))
# n = int(input("Enter end number: "))
# print(f"Sum from {m} to {n}: {sum(range(m, n+1))}")

# Task 8: Armstrong number
# num = int(input("Enter a number: "))
# sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
# print(f"{num} is an Armstrong number" if sum_of_cubes == num else f"{num} is not an Armstrong number")

# Task 9: Convert decimal to binary
# decimal = int(input("Enter a decimal number: "))
# print(f"Binary equivalent: {bin(decimal)[2:]}")

# Task 10: Palindrome
# num = input("Enter a number: ")
# print(f"{num} is a Palindrome" if num == num[::-1] else f"{num} is Not a Palindrome")