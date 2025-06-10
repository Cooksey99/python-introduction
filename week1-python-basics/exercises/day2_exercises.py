"""
Day 2 Exercises: Variables and Data Types
=========================================

Complete each function by writing code that demonstrates
variable creation, data types, and type conversion.

Each function should return the expected value as specified.
"""

def exercise_1():
    """
    Create variables for personal information and return them as a dictionary.
    
    Returns:
        dict: Dictionary with keys: 'first_name', 'last_name', 'age', 'height_feet', 'is_student', 'favorite_number'
        Example: {'first_name': 'Alice', 'last_name': 'Smith', 'age': 25, 'height_feet': 5.6, 'is_student': True, 'favorite_number': 42}
    """
    # Your code here:
    pass

def exercise_2():
    """
    Create variables of different types and return information about them.
    
    Returns:
        dict: Dictionary with 'values' (list of the variables) and 'types' (list of their type names as strings)
        Example: {'values': ['hello', 42, 3.14, True], 'types': ['str', 'int', 'float', 'bool']}
    """
    # Your code here:
    pass

def exercise_3():
    """
    Demonstrate good and bad variable naming.
    
    Returns:
        dict: Dictionary with 'good_names' and 'bad_names' lists
        Example: {'good_names': ['user_name', 'total_score'], 'bad_names': ['x', '1st_name']}
    """
    # Your code here:
    pass

def exercise_4():
    """
    Create number variables and perform math operations.
    
    Returns:
        dict: Dictionary with the original numbers and calculation results
        Keys: 'num1', 'num2', 'sum', 'difference', 'product', 'quotient', 'remainder', 'power'
    """
    # Your code here:
    pass

def exercise_5():
    """
    Demonstrate type conversion between different data types.
    
    Returns:
        dict: Dictionary showing original values and their conversions
        Keys: 'string_to_int', 'int_to_float', 'float_to_string', 'int_to_bool', 'string_to_bool'
        Example: {'string_to_int': ('123', 123), 'int_to_float': (42, 42.0), ...}
    """
    # Your code here:
    pass

def exercise_6():
    """
    Work with string variables and demonstrate string operations.
    
    Returns:
        dict: Dictionary with string operations results
        Keys: 'original', 'uppercase', 'lowercase', 'length', 'first_char', 'last_char'
    """
    # Your code here:
    pass

def exercise_7():
    """
    Create and manipulate boolean variables.
    
    Returns:
        dict: Dictionary with boolean operations
        Keys: 'bool1', 'bool2', 'and_result', 'or_result', 'not_result'
    """
    # Your code here:
    pass

def exercise_8():
    """
    Demonstrate multiple assignment (assigning multiple variables at once).
    
    Returns:
        tuple: Three variables assigned in one line
        Example: (10, 20, 30) from x, y, z = 10, 20, 30
    """
    # Your code here:
    pass

def exercise_9():
    """
    Demonstrate variable swapping without using a temporary variable.
    
    Returns:
        dict: Dictionary showing before and after values
        Example: {'before': (5, 10), 'after': (10, 5)}
    """
    # Your code here:
    pass

def exercise_10():
    """
    Create a user profile using all data types learned.
    
    Returns:
        dict: Complete user profile with various data types
        Keys: 'username', 'age', 'height', 'is_premium', 'hobbies' (list), 'settings' (dict)
    """
    # Your code here:
    pass

# Test runner
if __name__ == "__main__":
    print("=== Day 2 Exercises: Variables and Data Types ===")
    print()
    
    exercises = [
        ("Exercise 1", exercise_1, "Personal information variables"),
        ("Exercise 2", exercise_2, "Type checking"),
        ("Exercise 3", exercise_3, "Variable naming"),
        ("Exercise 4", exercise_4, "Numbers and math"),
        ("Exercise 5", exercise_5, "Type conversion"),
        ("Exercise 6", exercise_6, "String variables"),
        ("Exercise 7", exercise_7, "Boolean logic"),
        ("Exercise 8", exercise_8, "Multiple assignment"),
        ("Exercise 9", exercise_9, "Variable swapping"),
        ("Exercise 10", exercise_10, "User profile"),
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
    print("python -m pytest tests/test_day2.py -v")