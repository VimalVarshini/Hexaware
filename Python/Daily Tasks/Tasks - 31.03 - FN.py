# Task 1 : Accept the temparature in celsius and convert the same in farenheit.
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Temperature in Fahrenheit: {fahrenheit}")

# Task 2 : Write a python program to find the area of a cube.
# side = float(input("Enter the side length of the cube: "))
# area_cube = 6 * side * side
# print(f"Surface area of the cube: {area_cube}")

# Task 3 : Write a python program to find the area of a cylinder.
# import math
# radius = float(input("Enter the radius of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))
# area_cylinder = 2 * math.pi * radius * (radius + height)
# print(f"Surface area of the cylinder: {area_cylinder}")

# Task 4 : Write a python program to enter a number and display its hex and octal equivalant values and its square root.
# import math
# num = int(input("Enter a number: "))
# print(f"Hexadecimal: {hex(num)}, Octal: {oct(num)}, Square root: {math.sqrt(num)}")

# Task 5 : Write a python program to print the digit at one's place of a number
# num = int(input("Enter a number: "))
# print(f"Digit at one's place: {num % 10}")

# Task 6 : Write a python program to print the memory location of two variables and find if the variables are using similar memory space or not.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(f"Memory address of a: {id(a)}, Memory address of b: {id(b)}")
# print("Both variables share the same memory location" if a is b else "Variables have different memory locations")

# Task 7 : Write a program to input the radius of the sphere and calculate its volume
# import math
# radius = float(input("Enter the radius of the sphere: "))
# volume = (4/3) * math.pi * radius ** 3
# print(f"Volume of the sphere: {volume}")

# Task 8 : Write a python program to calculate the amount payable after the simple interest.
# p = float(input("Enter principal amount: "))
# r = float(input("Enter annual interest rate (in %): "))
# t = float(input("Enter time in years: "))
# simple_interest = (p * r * t) / 100
# total_amount = p + simple_interest
# print(f"Total amount after Simple Interest: {total_amount}")

# Task 9 : Write a python program to calculate amount payable after compound interest.
# p = float(input("Enter principal amount: "))
# r = float(input("Enter annual interest rate (in %): "))
# t = float(input("Enter time in years: "))
# n = int(input("Enter number of times interest applied per year: "))
# compound_interest = p * (1 + (r / (100 * n)))**(n * t)
# print(f"Total amount after Compound Interest: {compound_interest}")