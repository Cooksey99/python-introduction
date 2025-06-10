"""
Day 2 Solutions: Variables and Data Types
========================================

Complete solutions for Day 2 exercises demonstrating proper variable usage,
data types, and type conversion in Python.
"""

print("=== Day 2 Solutions: Variables and Data Types ===")
print()

# Exercise 1: Personal Information Variables
print("Exercise 1: Personal Information")

# Create variables for personal information
first_name = "Sarah"
last_name = "Johnson"
age = 25
height_feet = 5.6
is_student = True
favorite_number = 42

# Print each variable with descriptive labels
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)
print("Height:", height_feet, "feet")
print("Is Student:", is_student)
print("Favorite Number:", favorite_number)

print()

# Exercise 2: Type Checking
print("Exercise 2: Type Checking")

# Create one variable of each main type
my_string = "Hello World"
my_integer = 42
my_float = 3.14159
my_boolean = True

# Print each variable's value and type
print("Value:", my_string, "Type:", type(my_string))
print("Value:", my_integer, "Type:", type(my_integer))
print("Value:", my_float, "Type:", type(my_float))
print("Value:", my_boolean, "Type:", type(my_boolean))

print()

# Exercise 3: Variable Reassignment
print("Exercise 3: Variable Reassignment")

# Create score variable and track changes
score = 0
print("Initial score:", score)

score = 10
print("After setting to 10:", score)

score = score + 5
print("After adding 5:", score)

score = score * 2
print("After multiplying by 2:", score)

score += 3  # Shorthand operator
print("After += 3:", score)

print()

# Exercise 4: Type Conversion
print("Exercise 4: Type Conversion")

# Given string numbers
age_str = "25"
price_str = "19.99"

# Convert to appropriate types
age_int = int(age_str)
price_float = float(price_str)
age_back_to_str = str(age_int)

# Print all converted values
print("Original age string:", age_str, "Type:", type(age_str))
print("Converted to int:", age_int, "Type:", type(age_int))
print("Original price string:", price_str, "Type:", type(price_str))
print("Converted to float:", price_float, "Type:", type(price_float))
print("Age back to string:", age_back_to_str, "Type:", type(age_back_to_str))

print()

# Exercise 5: Shopping Calculator
print("Exercise 5: Shopping Calculator")

# Create shopping variables
item_name = "Laptop"
price_per_item = 999.99
quantity = 2
tax_rate = 0.08  # 8%
has_discount = True
discount_amount = 50.00

# Calculate totals
subtotal = price_per_item * quantity
print("Subtotal:", subtotal)

# Apply discount if applicable
if has_discount:
    discount_total = subtotal - discount_amount
else:
    discount_total = subtotal

tax_amount = discount_total * tax_rate
final_total = discount_total + tax_amount

# Print receipt
print("\n=== RECEIPT ===")
print(f"Item: {item_name}")
print(f"Price per item: ${price_per_item:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
if has_discount:
    print(f"Discount: -${discount_amount:.2f}")
print(f"After discount: ${discount_total:.2f}")
print(f"Tax ({tax_rate*100:.0f}%): ${tax_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")

print()

# Exercise 6: String and Number Combination
print("Exercise 6: String and Number Combination")

# Dream car variables
car_make = "Tesla"
car_model = "Model 3"
car_year = 2024
car_price = 45000.00
is_electric = True

# Create formatted description
description = f"I want a {car_year} {car_make} {car_model} that costs ${car_price:.2f}. Electric: {is_electric}"
print(description)

# Alternative formatting approaches
description2 = "I want a " + str(car_year) + " " + car_make + " " + car_model + " that costs $" + str(car_price) + ". Electric: " + str(is_electric)
print("Alternative format:", description2)

print()

# Exercise 7: Data Type Exploration
print("Exercise 7: Data Type Exploration")

values_to_check = [42, 3.14, "hello", True, 0, "", 0.0, False]

for i, value in enumerate(values_to_check):
    var_name = f"value_{i}"
    print(f"{var_name} = {repr(value)} | Type: {type(value).__name__}")

print()

# Exercise 8: Boolean Logic
print("Exercise 8: Boolean Operations")

# Use age from previous exercises
age = 25
full_name = first_name + " " + last_name

# Create boolean variables based on comparisons
is_adult = age >= 18
is_teenager = 13 <= age <= 19
has_long_name = len(full_name) > 10
is_even_age = age % 2 == 0

# Print each boolean with descriptive message
print(f"Is adult (age >= 18): {is_adult}")
print(f"Is teenager (13-19): {is_teenager}")
print(f"Has long name (> 10 chars): {has_long_name}")
print(f"Has even age: {is_even_age}")

print()

# Challenge Exercise: Variable Swap
print("Challenge: Variable Swap")

a = 10
b = 20
print("Before swap: a =", a, ", b =", b)

# Method 1: Tuple unpacking (recommended)
a, b = b, a

print("After swap: a =", a, ", b =", b)

# Alternative methods for educational purposes:
print("\nAlternative swap methods:")

# Reset values
a, b = 10, 20

# Method 2: Using arithmetic
print("Method 2 - Arithmetic:")
print("Before:", a, b)
a = a + b  # a = 30
b = a - b  # b = 10  
a = a - b  # a = 20
print("After:", a, b)

# Method 3: Using XOR (for integers only)
a, b = 10, 20
print("Method 3 - XOR:")
print("Before:", a, b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After:", a, b)

print()
print("=== Day 2 Solutions Complete! ===")

"""
Teaching Notes for Mentors:
===========================

Key Learning Objectives Demonstrated:
1. Variable creation and naming conventions
2. Understanding of Python's main data types
3. Type checking using type() function
4. Type conversion between strings and numbers
5. Variable reassignment and shorthand operators
6. Boolean logic and comparisons
7. String formatting and concatenation

Important Concepts to Emphasize:
- Variables are labels that point to values
- Python is dynamically typed (variables can change types)
- Type conversion is explicit in Python 3
- Boolean values are capitalized (True/False)
- Shorthand operators (+=, -=, *=, /=) for cleaner code

Common Student Mistakes to Watch For:
1. Using reserved words as variable names
2. Forgetting quotes around strings
3. Mixing up assignment (=) and comparison (==)
4. Not handling type conversion errors
5. Inconsistent variable naming styles

Extensions for Advanced Students:
- Explore more data types (complex numbers, None)
- Learn about variable scoping
- Practice with type annotations
- Understand mutable vs immutable types
- Explore the id() function and memory addresses

Assessment Opportunities:
- Check variable naming conventions
- Verify understanding of type differences
- Test problem-solving with the shopping calculator
- Observe debugging skills with the swap challenge

Code Quality Notes:
- Solutions use meaningful variable names
- Consistent formatting and spacing
- Appropriate comments for clarity
- Multiple approaches shown where educational
"""