# Day 4: Numbers and Math Operations

## 🎯 Learning Objectives

By the end of Day 4, you will be able to:
- Perform arithmetic operations with integers and floats
- Use Python's math operators and understand operator precedence
- Import and use the math module for advanced operations
- Handle number formatting and rounding
- Work with random numbers
- Build calculation-based programs and utilities

## 📚 Core Concepts

### Basic Arithmetic Operators
```python
a, b = 10, 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor division: 3
print(a % b)    # Modulo (remainder): 1
print(a ** b)   # Exponentiation: 1000
```

### Number Types
```python
integer = 42           # int
floating = 3.14159     # float
scientific = 1.5e3     # 1500.0 (scientific notation)
negative = -25         # negative numbers
```

### Math Module
```python
import math

print(math.pi)         # 3.141592653589793
print(math.sqrt(16))   # 4.0
print(math.ceil(4.2))  # 5 (round up)
print(math.floor(4.8)) # 4 (round down)
```

## 🔧 Hands-On Examples

### Example 1: Calculator Functions
```python
print("=== Basic Calculator ===")

# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform all operations
print(f"\nResults for {num1} and {num2}:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} × {num2} = {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1} ÷ {num2} = {num1 / num2:.2f}")
    print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
    print(f"Remainder: {num1} % {num2} = {num1 % num2}")
else:
    print("Cannot divide by zero!")

print(f"Exponentiation: {num1} ^ {num2} = {num1 ** num2}")
```

### Example 2: Advanced Math with Math Module
```python
import math

number = float(input("Enter a number: "))

print(f"\nMath operations for {number}:")
print(f"Square root: √{number} = {math.sqrt(abs(number)):.3f}")
print(f"Sine: sin({number}) = {math.sin(number):.3f}")
print(f"Cosine: cos({number}) = {math.cos(number):.3f}")
print(f"Natural log: ln({number}) = {math.log(abs(number)) if number > 0 else 'undefined'}")
print(f"Log base 10: log₁₀({number}) = {math.log10(abs(number)) if number > 0 else 'undefined'}")
print(f"Ceiling: ⌈{number}⌉ = {math.ceil(number)}")
print(f"Floor: ⌊{number}⌋ = {math.floor(number)}")

# Constants
print(f"\nMath constants:")
print(f"π (pi) = {math.pi:.6f}")
print(f"e = {math.e:.6f}")
```

### Example 3: Financial Calculator
```python
print("=== Compound Interest Calculator ===")

principal = float(input("Initial amount ($): "))
rate = float(input("Annual interest rate (%): ")) / 100
time = float(input("Number of years: "))
compounds_per_year = int(input("Compounds per year (12 for monthly): "))

# A = P(1 + r/n)^(nt)
amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time)
interest_earned = amount - principal

print(f"\nResults:")
print(f"Initial investment: ${principal:,.2f}")
print(f"Final amount: ${amount:,.2f}")
print(f"Interest earned: ${interest_earned:,.2f}")
print(f"Total return: {(interest_earned/principal)*100:.1f}%")
```

### Example 4: Random Number Games
```python
import random

print("=== Random Number Features ===")

# Random integers
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Random floats
temperature = random.uniform(-10.0, 35.0)
print(f"Random temperature: {temperature:.1f}°C")

# Random choice from list
colors = ["red", "blue", "green", "yellow", "purple"]
chosen_color = random.choice(colors)
print(f"Random color: {chosen_color}")

# Guess the number game
secret = random.randint(1, 100)
print("\nGuessing game started! (Number between 1-100)")
attempts = 0

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    
    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    
    if attempts >= 7:
        print(f"Game over! The number was {secret}")
        break
```

## 🏋️ Practice Exercises

### Exercise 1: Unit Converter
```python
# Create a program that converts between:
# - Miles to kilometers (1 mile = 1.60934 km)
# - Fahrenheit to Celsius (C = (F-32) * 5/9)
# - Pounds to kilograms (1 lb = 0.453592 kg)
# Let user choose conversion type and input value
```

### Exercise 2: Geometry Calculator
```python
import math

# Create functions to calculate:
# - Circle area and circumference (given radius)
# - Rectangle area and perimeter (given length, width)
# - Triangle area using Heron's formula (given 3 sides)
# - Pythagorean theorem (given 2 sides of right triangle)
```

### Exercise 3: Statistics Calculator
```python
# Get a series of numbers from user (until they enter 'done')
# Calculate and display:
# - Count of numbers
# - Sum and average
# - Minimum and maximum
# - Range (max - min)
# - Standard deviation (if you're feeling ambitious!)
```

### Exercise 4: Loan Calculator
```python
# Calculate monthly mortgage payments
# Formula: M = P * [r(1+r)^n] / [(1+r)^n - 1]
# Where:
# M = Monthly payment
# P = Principal (loan amount)
# r = Monthly interest rate
# n = Number of payments

# Get loan amount, annual rate, and years from user
# Display monthly payment and total amount paid
```

### Exercise 5: Number Base Converter
```python
# Convert numbers between different bases:
# - Decimal to binary
# - Decimal to hexadecimal
# - Binary to decimal
# - Hexadecimal to decimal
# Use Python's built-in functions: bin(), hex(), int()
```

### Challenge: Scientific Calculator
```python
import math

# Build a calculator that can handle:
# - Basic operations (+, -, *, /, **, %)
# - Trigonometric functions (sin, cos, tan)
# - Logarithms (natural and base 10)
# - Square root and nth root
# - Factorial
# - User-friendly menu system
```

## 💡 Operator Precedence (Order of Operations)

Python follows mathematical order of operations (PEMDAS):

1. **Parentheses** `()`
2. **Exponents** `**`
3. **Multiplication/Division/Modulo** `*`, `/`, `//`, `%` 
4. **Addition/Subtraction** `+`, `-`

```python
result = 2 + 3 * 4 ** 2    # 2 + 3 * 16 = 2 + 48 = 50
result = (2 + 3) * 4 ** 2  # 5 * 16 = 80
result = 2 + (3 * 4) ** 2  # 2 + 12² = 2 + 144 = 146
```

## 🔢 Number Formatting

```python
number = 1234.5678

print(f"{number:.2f}")      # 1234.57 (2 decimal places)
print(f"{number:,.2f}")     # 1,234.57 (with commas)
print(f"{number:10.2f}")    # "   1234.57" (10 characters wide)
print(f"{number:>10.2f}")   # "   1234.57" (right aligned)
print(f"{number:<10.2f}")   # "1234.57   " (left aligned)
print(f"{number:^10.2f}")   # " 1234.57  " (centered)

# Percentages
ratio = 0.845
print(f"{ratio:.1%}")       # 84.5%

# Scientific notation
big_number = 12345678
print(f"{big_number:.2e}")  # 1.23e+07
```

## ✅ Self-Check Questions

1. What's the difference between `/` and `//` division?
2. How do you calculate a number raised to a power?
3. What does the modulo operator `%` return?
4. How do you import the math module?
5. How do you round a number to 2 decimal places?
6. What's the order of operations in Python?

## 🛠️ Common Mistakes

**Mistake 1: Integer division confusion**
```python
# Python 3 behavior
print(7 / 2)    # 3.5 (true division)
print(7 // 2)   # 3 (floor division)
```

**Mistake 2: Floating point precision**
```python
# Floating point numbers aren't always exact
print(0.1 + 0.2)  # 0.30000000000000004

# Better for money calculations:
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
```

**Mistake 3: Division by zero**
```python
# Always check for zero before dividing
if denominator != 0:
    result = numerator / denominator
else:
    print("Cannot divide by zero!")
```

## 🚀 Tomorrow's Preview

Day 5 introduces lists - you'll learn to store and manipulate collections of data, opening up many new programming possibilities!

**Test your understanding with `python -m pytest tests/test_day4.py -v`**