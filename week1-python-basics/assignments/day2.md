# Day 2: Variables and Data Types

## 🎯 Learning Objectives

By the end of Day 2, you will be able to:
- Create and use variables to store data
- Understand Python's main data types (strings, integers, floats, booleans)
- Perform variable assignment and reassignment
- Use meaningful variable names following Python conventions
- Check data types using built-in functions
- Convert between different data types

## 📚 Core Concepts

### Variables
Variables are containers that store data values. Think of them as labeled boxes where you can put information and retrieve it later.

```python
name = "Alice"
age = 25
height = 5.6
is_student = True
```

### Data Types
- **String (str)**: Text data in quotes - `"Hello"` or `'Hello'`
- **Integer (int)**: Whole numbers - `42`, `-10`, `0`
- **Float (float)**: Decimal numbers - `3.14`, `-2.5`, `0.0`
- **Boolean (bool)**: True or False values - `True`, `False`

## 🔧 Hands-On Examples

### Example 1: Basic Variables
```python
# String variables
first_name = "John"
last_name = "Doe"
city = "New York"

# Integer variables
age = 28
siblings = 2
favorite_number = 7

# Float variables
height = 5.9
weight = 165.5
gpa = 3.8

# Boolean variables
is_employed = True
has_car = False
likes_python = True

print("Name:", first_name, last_name)
print("Age:", age)
print("Height:", height, "feet")
print("Employed:", is_employed)
```

### Example 2: Variable Reassignment
```python
score = 0
print("Initial score:", score)

score = 10
print("After first level:", score)

score = score + 5  # Add to existing value
print("After bonus:", score)

score += 3  # Shorthand for score = score + 3
print("Final score:", score)
```

### Example 3: Type Checking
```python
name = "Alice"
age = 25
height = 5.6
is_student = True

print("name is type:", type(name))
print("age is type:", type(age))
print("height is type:", type(height))
print("is_student is type:", type(is_student))
```

### Example 4: Type Conversion
```python
# Converting strings to numbers
age_str = "25"
age_num = int(age_str)
print("String '25' as integer:", age_num)

price_str = "19.99"
price_num = float(price_str)
print("String '19.99' as float:", price_num)

# Converting numbers to strings
score = 100
score_str = str(score)
print("Score as string:", score_str)

# Converting to boolean
print("Boolean of 1:", bool(1))
print("Boolean of 0:", bool(0))
print("Boolean of 'hello':", bool("hello"))
print("Boolean of '':", bool(""))
```

## 💡 Variable Naming Best Practices

### Good Variable Names
```python
user_name = "alice123"
total_price = 29.99
is_logged_in = True
max_attempts = 3
```

### Poor Variable Names (Avoid These)
```python
x = "alice123"          # Not descriptive
TotalPrice = 29.99      # Wrong case convention
is-logged-in = True     # Can't use hyphens
2names = ["Alice", "Bob"]  # Can't start with number
```

### Naming Rules
- Use lowercase with underscores: `first_name`, `total_count`
- Start with letter or underscore, not number
- No spaces or special characters (except underscore)
- Case sensitive: `Name` and `name` are different
- Use descriptive names that explain the purpose

## 🏋️ Practice Exercises

### Exercise 1: Personal Profile
Create variables for your personal information and display them:
```python
# Create variables for:
# - Your full name (first and last name separately)
# - Your age
# - Your height in feet (decimal)
# - Whether you're a student
# - Your favorite number

# Then print them in a formatted way
```

### Exercise 2: Shopping Cart
```python
# Create variables for a shopping scenario:
# - Item name (string)
# - Item price (float)
# - Quantity (integer)
# - Has discount (boolean)
# - Calculate total price (price * quantity)

# Print a receipt-style output
```

### Exercise 3: Type Exploration
```python
# Create one variable of each type
# Print both the value and its type using type()
# Try converting between types and observe results
```

### Exercise 4: Variable Math
```python
# Create numeric variables and practice operations:
num1 = 10
num2 = 3

# Calculate and store:
# - Sum
# - Difference  
# - Product
# - Division (float result)
# - Integer division
# - Remainder (modulo)

# Print results with descriptive labels
```

### Exercise 5: Dynamic Variables
```python
# Start with initial values, then modify them:
bank_balance = 1000
print("Starting balance:", bank_balance)

# Deposit money (add to balance)
# Withdraw money (subtract from balance)
# Apply interest (multiply by 1.02)
# Print balance after each operation
```

### Challenge: Data Type Converter
```python
# Create a program that takes various inputs and converts them:
# - Convert "123" to integer
# - Convert "45.67" to float
# - Convert 0 and 1 to boolean
# - Convert numbers back to strings
# - Handle conversion errors gracefully
```

## ✅ Self-Check Questions

1. What are the four main data types in Python?
2. How do you check the type of a variable?
3. What's the difference between `=` and `==`?
4. Can you change a variable's value after creating it?
5. What makes a good variable name?
6. How do you convert a string to an integer?

## 🛠️ Common Mistakes & Solutions

**Mistake 1: Using reserved words**
```python
# Wrong
print = "Hello"  # 'print' is a built-in function

# Right
message = "Hello"
```

**Mistake 2: Inconsistent naming**
```python
# Wrong - inconsistent style
firstName = "John"
last_name = "Doe"

# Right - consistent snake_case
first_name = "John"
last_name = "Doe"
```

**Mistake 3: Type conversion errors**
```python
# This will cause an error:
# age = int("twenty-five")

# This works:
age = int("25")
```

## 🚀 Tomorrow's Preview

Day 3 will cover string operations and user input - you'll learn to manipulate text and make your programs interactive!

**Test your understanding with `python -m pytest tests/test_day2.py -v`**