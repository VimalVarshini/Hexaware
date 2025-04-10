# Task 1: Print the pattern
# rows = 5
# for i in range(rows, 0, -1):
#     print("* " * i)


# Task 2: Print the pattern
# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# Task 3: Print the pattern
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         if j == 1 or j == i:
#             print(1, end=" ")
#         else:
#             print(2, end=" ")
#     print()


# Task 4: Print the pattern
# for i in range(5, 0, -1):
#     print((str(i) + " ") * i)

# Task 5: Print the pattern
# count = 1
# for i in range(1, 5):
#     for j in range(i):
#         print(count, end=" ")
#         count += 1
#     print()


# Task 6: Sum of even and odd numbers
# even_sum = 0
# odd_sum = 0
#
# for _ in range(10):
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         even_sum += num
#     else:
#         odd_sum += num
#
# print("Sum of even numbers:", even_sum)
# print("Sum of odd numbers:", odd_sum)


# Task 7: Fibonacci Series
# def fibonacci(n):
#     fib_series = [0, 1]
#     for _ in range(n - 2):
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series
#
# num = int(input("Enter the number of terms: "))
# print("Fibonacci Series:", fibonacci(num))


# Task 8: Simple Calculator
# while True:
#     print("\nSimple Calculator")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 5:
#         break
#
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#
#     if choice == 1:
#         print("Result:", num1 + num2)
#     elif choice == 2:
#         print("Result:", num1 - num2)
#     elif choice == 3:
#         print("Result:", num1 * num2)
#     elif choice == 4:
#         print("Result:", num1 / num2 if num2 != 0 else "Cannot divide by zero")
#     else:
#         print("Invalid choice, please try again!")


# Task 9: Palindrome
# def is_palindrome(s):
#     return s == s[::-1]
#
# string = input("Enter a string: ").upper()
#
# if is_palindrome(string):
#     print(f"{string} is a palindrome")
# else:
#     print(f"{string} is not a palindrome")
