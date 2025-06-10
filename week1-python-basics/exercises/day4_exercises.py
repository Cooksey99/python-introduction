"""
Day 4 Exercises: Numbers and Math Operations
===========================================

Complete each function by writing code that demonstrates
mathematical operations, calculations, and numerical programming.

Each function should return the expected value as specified.
"""

import math
import random

def exercise_1():
    """
    Basic calculator operations with two numbers.
    
    Returns:
        dict: Dictionary with calculation results
        Keys: 'num1', 'num2', 'addition', 'subtraction', 'multiplication', 'division', 'floor_division', 'modulo', 'exponentiation'
        Use num1=15.5, num2=4.2
    """
    # Your code here:
    pass

def exercise_2():
    """
    Advanced math functions using the math module.
    
    Returns:
        dict: Dictionary with advanced math results
        Keys: 'number', 'sqrt', 'sin', 'cos', 'log', 'log10', 'ceil', 'floor', 'factorial'
        Use number=16.7 (use int(number) for factorial)
    """
    # Your code here:
    pass

def exercise_3():
    """
    Compound interest calculator.
    
    Returns:
        dict: Dictionary with compound interest calculation
        Keys: 'principal', 'rate', 'time', 'compounds_per_year', 'final_amount', 'interest_earned', 'total_return_percent'
        Use: principal=1000, annual_rate=5.5%, time=10 years, monthly compounding
    """
    # Your code here:
    pass

def exercise_4():
    """
    Number pattern generators: Fibonacci, primes, and perfect squares.
    
    Returns:
        dict: Dictionary with number patterns up to n=20
        Keys: 'fibonacci', 'primes', 'perfect_squares'
    """
    # Your code here:
    pass

def exercise_5():
    """
    Statistics calculator for a list of numbers.
    
    Returns:
        dict: Dictionary with statistical calculations
        Keys: 'numbers', 'count', 'sum', 'mean', 'median', 'min', 'max', 'range', 'std_dev'
        Use numbers: [85, 92, 78, 96, 88, 84, 90, 87, 91, 83]
    """
    # Your code here:
    pass

def exercise_6():
    """
    Unit converter for temperature, distance, and weight.
    
    Returns:
        dict: Dictionary with conversion results
        Keys: 'temperature', 'distance', 'weight'
        Each containing original value and converted values
    """
    # Your code here:
    pass

def exercise_7():
    """
    Loan payment calculator using the standard loan formula.
    
    Returns:
        dict: Dictionary with loan calculation results
        Keys: 'loan_amount', 'annual_rate', 'years', 'monthly_payment', 'total_paid', 'total_interest'
        Use: loan_amount=250000, annual_rate=6.5%, years=30
    """
    # Your code here:
    pass

def exercise_8():
    """
    Random number generators and operations.
    
    Returns:
        dict: Dictionary with random number results
        Keys: 'dice_rolls', 'dice_average', 'math_problems', 'lottery_numbers'
        Generate 10 dice rolls, 3 math problems, and 6 lottery numbers (1-49)
    """
    # Your code here:
    pass

def exercise_9():
    """
    Number base conversions.
    
    Returns:
        dict: Dictionary with base conversion results
        Keys: 'decimal', 'binary', 'octal', 'hexadecimal'
        Convert the number 255 to different bases
    """
    # Your code here:
    pass

def exercise_10():
    """
    Mathematical puzzle solver.
    
    Returns:
        dict: Dictionary with puzzle solutions
        Keys: 'puzzle1_solution', 'puzzle2_sum', 'puzzle3_palindrome'
        Solve: 1) Two numbers that multiply to 24 and add to 10
               2) Sum of multiples of 3 or 5 below 100
               3) Largest palindrome from product of two 2-digit numbers
    """
    # Your code here:
    pass

# Test runner
if __name__ == "__main__":
    print("=== Day 4 Exercises: Numbers and Math ===")
    print()
    
    exercises = [
        ("Exercise 1", exercise_1, "Basic calculator operations"),
        ("Exercise 2", exercise_2, "Advanced math functions"),
        ("Exercise 3", exercise_3, "Compound interest calculator"),
        ("Exercise 4", exercise_4, "Number pattern generators"),
        ("Exercise 5", exercise_5, "Statistics calculator"),
        ("Exercise 6", exercise_6, "Unit converter"),
        ("Exercise 7", exercise_7, "Loan payment calculator"),
        ("Exercise 8", exercise_8, "Random number operations"),
        ("Exercise 9", exercise_9, "Number base conversions"),
        ("Exercise 10", exercise_10, "Mathematical puzzle solver"),
    ]
    
    for name, func, description in exercises:
        print(f"{name}: {description}")
        try:
            result = func()
            if result is not None:
                print(f"  ✓ Result: {result}")
            else:
                print(f"  ✗ Not implemented (returns None)")
        except Exception as e:
            print(f"  ✗ Error: {e}")
        print()
    
    print("=== Run the tests to check your work ===")
    print("python -m pytest tests/test_day4.py -v")