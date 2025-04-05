# bonkers_code.py

def add_numbers(a, b):
    # This function correctly adds two numbers
    return a + b

def multiply_numbers(a, b):
    # This function is supposed to multiply two numbers, but it has a mistake
    result = a + b  # Oops, this should be a * b
    return result

def check_even_odd(number):
    # This function correctly checks if a number is even or odd
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def find_largest(numbers):
    # This function is supposed to find the largest number in a list, but it has a logical error
    largest = numbers[0]
    for num in numbers[1:]:
        if num < largest:  # Logical error: should be if num > largest
            largest = num
    return largest

def print_hello():
    # This function prints a greeting, but it's missing a critical part
    print("Hello, ")  # Missing the name or target of the greeting

def divide_numbers(a, b):
    # This function correctly divides two numbers but doesn't handle division by zero
    return a / b

def buggy_loop(n):
    # This function contains a buggy loop that may not terminate correctly
    i = 0
    while i < n:
        print(i)
        # Oops, forgot to increment i, this will result in an infinite loop

def process_list(my_list):
    # This function processes a list but has inconsistent naming and indentation
    for item in my_list:
     if item % 2 == 0:
      print("Even number:", item)
        elif item % 2 != 0:  # This elif is redundant, should just be else
       print("Odd number:", item)

def concat_strings(str1, str2):
    # This function concatenates two strings but has a stylistic issue
    return str1 + " " + str2  # Should use f-string for better readability

def factorial(n):
    # This function calculates the factorial of a number but has a mistake
    if n == 0:
        return 0  # Mistake: factorial of 0 should be 1
    else:
        return n * factorial(n-1)

def calculate_sum(lst):
    # This function calculates the sum of a list, but it doesn't check for the type of elements
    total = 0
    for item in lst:
        total += item  # What if the list contains non-numeric items?
    return total

def redundant_function():
    # This function does nothing useful
    pass

def broken_function():
    # This function is broken and won't even run
    print("This function is broken"

def loop_with_bug(my_list):
    # This function contains a bug in a loop
    for i in range(len(my_list)):
        if my_list[i] > 10:
            print("Found a number greater than 10:", my_list[i])
            break
        print("Current number:", my_list[i])  # This print is indented incorrectly