"""
Day 4 Tests: Numbers and Math Operations
========================================

Tests for Day 4 concepts: arithmetic, math functions, and numerical calculations.
"""

import pytest
import math
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_basic_arithmetic():
    """Test basic arithmetic operations"""
    # Addition
    assert 5 + 3 == 8
    assert 10.5 + 2.5 == 13.0
    
    # Subtraction
    assert 10 - 4 == 6
    assert 5.5 - 2.5 == 3.0
    
    # Multiplication
    assert 6 * 7 == 42
    assert 2.5 * 4 == 10.0
    
    # Division
    assert 20 / 4 == 5.0
    assert 15 / 2 == 7.5
    
    # Floor division
    assert 15 // 2 == 7
    assert 20 // 6 == 3
    
    # Modulo
    assert 10 % 3 == 1
    assert 15 % 4 == 3
    
    # Exponentiation
    assert 2 ** 3 == 8
    assert 5 ** 2 == 25

def test_order_of_operations():
    """Test order of operations (PEMDAS)"""
    assert 2 + 3 * 4 == 14  # Not 20
    assert (2 + 3) * 4 == 20
    assert 10 - 4 / 2 == 8.0  # Not 3
    assert 2 ** 3 * 4 == 32  # 8 * 4
    assert 10 % 3 + 2 == 3  # 1 + 2

def test_number_types():
    """Test integer and float operations"""
    # Integer operations
    assert type(5 + 3) == int
    assert type(10 - 4) == int
    assert type(6 * 7) == int
    
    # Float operations
    assert type(10 / 2) == float  # Division always returns float
    assert type(5.0 + 3) == float
    assert type(10 * 0.5) == float

def test_math_functions():
    """Test common math module functions"""
    # Square root
    assert math.sqrt(16) == 4.0
    assert math.sqrt(25) == 5.0
    
    # Power functions
    assert math.pow(2, 3) == 8.0
    
    # Rounding functions
    assert math.ceil(4.3) == 5
    assert math.floor(4.8) == 4
    assert round(4.5) == 4  # Banker's rounding
    assert round(5.5) == 6
    
    # Absolute value
    assert abs(-10) == 10
    assert abs(5) == 5
    
    # Min/Max
    assert min(3, 7, 2, 9, 1) == 1
    assert max(3, 7, 2, 9, 1) == 9

def test_trigonometric_functions():
    """Test trigonometric functions"""
    # Test with known values
    assert math.sin(0) == 0
    assert math.cos(0) == 1
    assert abs(math.sin(math.pi/2) - 1) < 0.0001  # Close to 1
    assert abs(math.cos(math.pi)) < 0.0001  # Close to -1
    
    # Degrees to radians
    assert math.radians(180) == math.pi
    assert math.degrees(math.pi) == 180

def test_compound_interest_calculation():
    """Test compound interest formula"""
    def compound_interest(principal, rate, time, n=12):
        # A = P(1 + r/n)^(nt)
        amount = principal * (1 + rate/n) ** (n * time)
        return round(amount, 2)
    
    # Test cases
    assert compound_interest(1000, 0.05, 1) == 1051.16
    assert compound_interest(1000, 0.05, 2) == 1104.94
    assert compound_interest(5000, 0.08, 5) == 7449.23

def test_statistics_calculations():
    """Test basic statistical calculations"""
    numbers = [10, 20, 30, 40, 50]
    
    # Mean
    assert sum(numbers) / len(numbers) == 30.0
    
    # Min/Max
    assert min(numbers) == 10
    assert max(numbers) == 50
    
    # Range
    assert max(numbers) - min(numbers) == 40
    
    # Median (for sorted odd-length list)
    assert numbers[len(numbers)//2] == 30
    
    # Median (for even-length list)
    even_numbers = [10, 20, 30, 40]
    median_even = (even_numbers[len(even_numbers)//2 - 1] + even_numbers[len(even_numbers)//2]) / 2
    assert median_even == 25.0

def test_number_patterns():
    """Test generation of number patterns"""
    # Fibonacci sequence
    def fibonacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    
    # Prime check
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    assert is_prime(2) == True
    assert is_prime(17) == True
    assert is_prime(4) == False
    assert is_prime(15) == False
    
    # Perfect squares
    def perfect_squares(n):
        return [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
    
    assert perfect_squares(20) == [1, 4, 9, 16]

def test_unit_conversions():
    """Test unit conversion functions"""
    # Temperature conversions
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32
    
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    
    # Distance conversions
    def miles_to_km(miles):
        return miles * 1.60934
    
    def km_to_miles(km):
        return km / 1.60934
    
    assert round(miles_to_km(1), 2) == 1.61
    assert round(km_to_miles(1.60934), 2) == 1.0

def test_loan_calculations():
    """Test loan payment calculations"""
    def monthly_payment(principal, annual_rate, years):
        monthly_rate = annual_rate / 12
        num_payments = years * 12
        
        if monthly_rate == 0:
            return principal / num_payments
        
        payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
                 ((1 + monthly_rate)**num_payments - 1)
        return round(payment, 2)
    
    # Test cases
    assert monthly_payment(10000, 0.05, 1) == 856.07
    assert monthly_payment(100000, 0.06, 30) == 599.55

def test_number_formatting():
    """Test number formatting techniques"""
    # Float precision
    pi = 3.141592653589793
    assert f"{pi:.2f}" == "3.14"
    assert f"{pi:.4f}" == "3.1416"
    
    # Currency formatting
    amount = 1234.56
    assert f"${amount:,.2f}" == "$1,234.56"
    
    # Percentage formatting
    rate = 0.0525
    assert f"{rate:.2%}" == "5.25%"
    
    # Scientific notation
    large_num = 1234567890
    assert f"{large_num:.2e}" == "1.23e+09"

def test_random_operations():
    """Test random number operations"""
    import random
    
    # Set seed for reproducible tests
    random.seed(42)
    
    # Random integer in range
    for _ in range(10):
        n = random.randint(1, 10)
        assert 1 <= n <= 10
    
    # Random float
    for _ in range(10):
        f = random.random()
        assert 0 <= f < 1
    
    # Random choice
    choices = [1, 2, 3, 4, 5]
    for _ in range(10):
        choice = random.choice(choices)
        assert choice in choices

def test_mathematical_constants():
    """Test mathematical constants"""
    # Pi
    assert abs(math.pi - 3.141592653589793) < 0.000001
    
    # Euler's number
    assert abs(math.e - 2.718281828459045) < 0.000001
    
    # Infinity
    assert math.inf > 1000000
    assert -math.inf < -1000000
    
    # Not a Number
    assert math.isnan(float('nan'))

def test_factorial_and_combinations():
    """Test factorial and combinatorial functions"""
    # Factorial
    assert math.factorial(0) == 1
    assert math.factorial(5) == 120
    assert math.factorial(10) == 3628800
    
    # Combinations and permutations
    def combinations(n, r):
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    
    def permutations(n, r):
        return math.factorial(n) // math.factorial(n - r)
    
    assert combinations(5, 2) == 10  # C(5,2)
    assert permutations(5, 2) == 20  # P(5,2)

def test_number_validation():
    """Test number validation functions"""
    def is_valid_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    assert is_valid_number("123") == True
    assert is_valid_number("123.45") == True
    assert is_valid_number("-123.45") == True
    assert is_valid_number("abc") == False
    assert is_valid_number("12.34.56") == False

def test_advanced_calculations():
    """Test more advanced mathematical calculations"""
    # Standard deviation
    def std_dev(numbers):
        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)
    
    test_data = [2, 4, 4, 4, 5, 5, 7, 9]
    assert abs(std_dev(test_data) - 2.0) < 0.1
    
    # Greatest Common Divisor
    assert math.gcd(48, 18) == 6
    assert math.gcd(100, 35) == 5
    
    # Least Common Multiple
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
    
    assert lcm(4, 6) == 12
    assert lcm(10, 15) == 30

if __name__ == "__main__":
    pytest.main([__file__, "-v"])