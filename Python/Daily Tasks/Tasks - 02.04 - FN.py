# Task 1: Calculate the Mean
# def calculate_mean():
#     numbers = list(map(float, input("Enter numbers: ").split()))
#     return sum(numbers) / len(numbers) if numbers else 0
#
# print("Mean:", calculate_mean())

# Task 2: Search for an Element
# def search_element():
#     numbers = list(map(int, input("Enter numbers: ").split()))
#     target = int(input("Enter the number to search: "))
#     return numbers.index(target) if target in numbers else -1
#
# index = search_element()
# if index != -1:
#     print(f"Element found at index {index}")
# else:
#     print("Element not found")

# Task 3: Find Maximum Element
# def max_element_from_lists():
#     list1 = list(map(int, input("Enter first list numbers: ").split()))
#     list2 = list(map(int, input("Enter second list numbers: ").split()))
#     combined = list1 + list2
#     max_val = max(combined)
#
#     if max_val in list1:
#         index = list1.index(max_val)
#         list_name = "List 1"
#     else:
#         index = list2.index(max_val)
#         list_name = "List 2"
#
#     return max_val, index, list_name
#
#
# max_val, idx, lst = max_element_from_lists()
# print(f"Max Value: {max_val}, Index: {idx}, List: {lst}")

# Task 4: Find Second Largest Number
# def second_largest():
#     numbers = list(map(int, input("Enter numbers: ").split()))
#     unique_numbers = list(set(numbers))  # Remove duplicates
#     unique_numbers.sort(reverse=True)
#     return unique_numbers[1] if len(unique_numbers) > 1 else None
#
# result = second_largest()
# print("Second Largest:", result if result is not None else "Not enough unique numbers")

# Task 5: Create a Nested Tuple
# def input_marks():
#     marks = tuple(tuple(map(int, input(f"Enter marks for student {i+1}: ").split())) for i in range(5))
#     return marks
#
# marks_tuple = input_marks()
# print("Marks Tuple:", marks_tuple)

# Task 6: Extract Even and Odd Values from Dictionary & Find Their Sum
# def even_odd_values():
#     d = {}
#     n = int(input("Enter number of dictionary elements: "))
#     for _ in range(n):
#         key = input("Enter key: ")
#         value = int(input("Enter value: "))
#         d[key] = value
#
#     evens = [v for v in d.values() if v % 2 == 0]
#     odds = [v for v in d.values() if v % 2 != 0]
#     return evens, odds, sum(evens), sum(odds)
#
# evens, odds, sum_evens, sum_odds = even_odd_values()
# print("Even Values:", evens, "Sum:", sum_evens)
# print("Odd Values:", odds, "Sum:", sum_odds)

# Task 7: Find the Highest Two Values in a Dictionary
# def top_two_values():
#     d = {}
#     n = int(input("Enter number of dictionary elements: "))
#     for _ in range(n):
#         key = input("Enter key: ")
#         value = int(input("Enter value: "))
#         d[key] = value
#
#     sorted_values = sorted(d.values(), reverse=True)
#     return sorted_values[:2] if len(sorted_values) > 1 else sorted_values
#
# print("Top Two Values:", top_two_values())

# Task 8: Display Product Information from a Dictionary
# def display_product_info():
#     products = {}
#     n = int(input("Enter number of products: "))
#
#     for _ in range(n):
#         name = input("Enter product name: ")
#         brand = input("Enter brand: ")
#         price = float(input("Enter price: "))
#         products[name] = {'Brand': brand, 'Price': price}
#
#     for key, value in products.items():
#         print(f"Product: {key}, Brand: {value['Brand']}, Price: {value['Price']}")
#
#
# display_product_info()

