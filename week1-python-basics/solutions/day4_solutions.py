"""
Day 4 Solutions: Numbers and Math Operations
===========================================

Complete solutions for mathematical operations, calculations, and numerical programming.
"""

import math
import random

print("=== Day 4 Solutions: Numbers and Math ===")
print()

# Exercise 1: Basic Calculator
print("Exercise 1: Calculator Functions")
num1, num2 = 15.5, 4.2
print(f"Numbers: {num1}, {num2}")

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} × {num2} = {num1 * num2}")
print(f"Division: {num1} ÷ {num2} = {num1 / num2:.3f}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulo: {num1} % {num2} = {num1 % num2:.3f}")
print(f"Exponentiation: {num1} ^ {num2} = {num1 ** num2:.3f}")

print()

# Exercise 2: Advanced Math Functions  
print("Exercise 2: Advanced Math")
number = 16.7
print(f"Working with: {number}")

print(f"Square root: √{number} = {math.sqrt(number):.3f}")
print(f"Sine: sin({number}) = {math.sin(number):.3f}")
print(f"Cosine: cos({number}) = {math.cos(number):.3f}")
print(f"Natural log: ln({number}) = {math.log(number):.3f}")
print(f"Log base 10: log₁₀({number}) = {math.log10(number):.3f}")
print(f"Ceiling: ⌈{number}⌉ = {math.ceil(number)}")
print(f"Floor: ⌊{number}⌋ = {math.floor(number)}")

# Factorial for integer part
int_part = int(number)
print(f"Factorial of {int_part}: {int_part}! = {math.factorial(int_part)}")

print()

# Exercise 3: Compound Interest Calculator
print("Exercise 3: Compound Interest")
principal = 1000
annual_rate = 5.5  # 5.5%
years = 10
compounds_per_year = 12  # Monthly

rate_decimal = annual_rate / 100
monthly_rate = rate_decimal / compounds_per_year
total_compounds = compounds_per_year * years

# A = P(1 + r/n)^(nt)
final_amount = principal * (1 + monthly_rate) ** total_compounds
interest_earned = final_amount - principal
total_return_percent = (interest_earned / principal) * 100

print(f"Principal: ${principal:,.2f}")
print(f"Annual Rate: {annual_rate}%")
print(f"Time: {years} years")
print(f"Compounding: {compounds_per_year} times per year")
print(f"Final Amount: ${final_amount:,.2f}")
print(f"Interest Earned: ${interest_earned:,.2f}")
print(f"Total Return: {total_return_percent:.1f}%")

print()

# Exercise 4: Number Pattern Generator
print("Exercise 4: Number Patterns")
n = 20

# Fibonacci sequence
print("Fibonacci sequence:")
fib = [0, 1]
while len(fib) < n and fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
fib = [x for x in fib if x <= n]
print(fib)

# Prime numbers
print("Prime numbers:")
primes = []
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(primes)

# Perfect squares
print("Perfect squares:")
squares = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
print(squares)

print()

# Exercise 5: Statistics Calculator
print("Exercise 5: Statistics Calculator")
numbers = [85, 92, 78, 96, 88, 84, 90, 87, 91, 83]
print("Numbers:", numbers)

count = len(numbers)
total = sum(numbers)
average = total / count
minimum = min(numbers)
maximum = max(numbers)
range_val = maximum - minimum

# Median
sorted_nums = sorted(numbers)
if count % 2 == 0:
    median = (sorted_nums[count//2 - 1] + sorted_nums[count//2]) / 2
else:
    median = sorted_nums[count//2]

# Standard deviation
variance = sum((x - average) ** 2 for x in numbers) / count
std_dev = math.sqrt(variance)

print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")
print(f"Median: {median:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_val}")
print(f"Standard Deviation: {std_dev:.2f}")

print()

# Exercise 6: Unit Converter
print("Exercise 6: Unit Converter")

def temperature_converter():
    fahrenheit = 98.6
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"{fahrenheit}°F = {celsius:.1f}°C = {kelvin:.1f}K")

def distance_converter():
    miles = 26.2  # Marathon distance
    kilometers = miles * 1.60934
    meters = kilometers * 1000
    print(f"{miles} miles = {kilometers:.1f} km = {meters:.0f} meters")

def weight_converter():
    pounds = 150
    kilograms = pounds * 0.453592
    grams = kilograms * 1000
    print(f"{pounds} lbs = {kilograms:.1f} kg = {grams:.0f} grams")

temperature_converter()
distance_converter()
weight_converter()

print()

# Exercise 7: Loan Calculator
print("Exercise 7: Loan Calculator")
loan_amount = 250000  # $250k house
annual_rate = 6.5  # 6.5% APR
years = 30

monthly_rate = annual_rate / 100 / 12
num_payments = years * 12

# M = P * [r(1+r)^n] / [(1+r)^n - 1]
if monthly_rate > 0:
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
else:
    monthly_payment = loan_amount / num_payments

total_paid = monthly_payment * num_payments
total_interest = total_paid - loan_amount

print(f"Loan Amount: ${loan_amount:,.2f}")
print(f"Interest Rate: {annual_rate}% APR")
print(f"Loan Term: {years} years")
print(f"Monthly Payment: ${monthly_payment:,.2f}")
print(f"Total Paid: ${total_paid:,.2f}")
print(f"Total Interest: ${total_interest:,.2f}")

print()

# Exercise 8: Random Number Games
print("Exercise 8: Random Number Games")

# Dice rolling simulator
print("Dice Roller:")
dice_rolls = [random.randint(1, 6) for _ in range(10)]
print("10 dice rolls:", dice_rolls)
print("Average roll:", sum(dice_rolls) / len(dice_rolls))

# Random math quiz
print("\nMath Quiz Generator:")
for i in range(3):
    a, b = random.randint(1, 20), random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        answer = a + b
    elif operation == '-':
        answer = a - b
    else:
        answer = a * b
    print(f"Question {i+1}: {a} {operation} {b} = {answer}")

# Lottery numbers
print("\nLottery Numbers:")
lottery = random.sample(range(1, 50), 6)
lottery.sort()
print("Your lucky numbers:", lottery)

print()

# Challenge: Mathematical Puzzle Solver
print("Challenge: Math Puzzle Solver")

# Puzzle 1: Two numbers that multiply to 24 and add to 10
print("Puzzle 1: Two numbers that multiply to 24 and add to 10")
# Solve x + y = 10 and x * y = 24
# x = 4, y = 6 or x = 6, y = 4
for x in range(1, 10):
    y = 10 - x
    if x * y == 24:
        print(f"Solution: {x} and {y}")
        break

# Puzzle 2: Sum of multiples of 3 or 5 below 1000
print("Puzzle 2: Sum of multiples of 3 or 5 below 1000")
total = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
print(f"Sum: {total}")

# Puzzle 3: Largest palindrome from product of two 3-digit numbers
print("Puzzle 3: Largest palindrome from product of two 3-digit numbers")
largest_palindrome = 0
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > largest_palindrome:
                largest_palindrome = product
                print(f"Found: {i} × {j} = {product}")
                break
    if largest_palindrome > 0:
        break

print()
print("=== Day 4 Solutions Complete! ===")

"""
Teaching Notes for Mentors:
===========================

Key Concepts Demonstrated:
1. Arithmetic operators and precedence
2. Math module functions
3. Number formatting and precision
4. Financial calculations
5. Statistical analysis
6. Algorithm implementation
7. Random number generation

Important Mathematical Concepts:
- Floating-point precision limitations
- Order of operations (PEMDAS)
- Scientific notation
- Compound interest formula
- Statistical measures
- Number theory basics

Common Challenges:
1. Floating-point arithmetic precision
2. Division by zero handling
3. Integer vs float division
4. Understanding math module functions
5. Implementing mathematical algorithms

Real-World Applications:
- Financial calculators
- Statistical analysis
- Unit conversions
- Game development (dice, random events)
- Scientific computing
- Data analysis

Code Quality Features:
- Clear mathematical formulas in comments
- Appropriate number formatting
- Error handling for edge cases
- Efficient algorithm implementations
- Good variable naming for mathematical concepts
"""