"""
Day 2 Exercises: Variables and Data Types
=========================================

Complete each function by writing code that demonstrates
variable creation, data types, and type conversion.

Each function should return the expected value as specified.
"""

# Exercise 1: Personal information variables
def exercise_1():
    """
    Create variables for personal information and return them as a dictionary.
    
    Returns:
        dict: Dictionary with keys: 'first_name', 'last_name', 'age', 'height_feet', 'is_student', 'favorite_number'
        Example: {'first_name': 'Alice', 'last_name': 'Smith', 'age': 25, 'height_feet': 5.6, 'is_student': True, 'favorite_number': 42}
    """
    # TODO: Create variables for personal information
    # Your code here:
    first_name = 'Andrew'
    last_name = 'Cooksey'
    age = 26
    height_feet = 6
    is_student = False
    favorite_number = 42
    
    return {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'height_feet': height_feet,
        'is_student': is_student,
        'favorite_number': favorite_number
    }

# Exercise 2: Type checking
def exercise_2():
    """
    Create variables of different types and return information about them.
    
    Returns:
        dict: Dictionary with 'values' (list of the variables) and 'types' (list of their type names as strings)
        Example: {'values': ['hello', 42, 3.14, True], 'types': ['str', 'int', 'float', 'bool']}
    """
    # TODO: Create variables of different types and check their types
    # Your code here:
    string_var = 'hello'
    int_var = 42
    float_var = 3.14
    bool_var = True
    
    values = [string_var, int_var, float_var, bool_var]
    types = [type(string_var).__name__, type(int_var).__name__, type(float_var).__name__, type(bool_var).__name__]
    
    return {'values': values, 'types': types}

# Exercise 3: Variable naming
def exercise_3():
    """
    Demonstrate good and bad variable naming.
    
    Returns:
        dict: Dictionary with 'good_names' and 'bad_names' lists
        Example: {'good_names': ['user_name', 'total_score'], 'bad_names': ['x', '1st_name']}
    """
    # TODO: Demonstrate good and bad variable naming
    # Your code here:
    pass

# Exercise 4: Numbers and math
def exercise_4():
    """
    Create number variables and perform math operations.
    
    Returns:
        dict: Dictionary with the original numbers and calculation results
        Keys: 'num1', 'num2', 'sum', 'difference', 'product', 'quotient', 'remainder', 'power'
    """
    # TODO: Create number variables and perform math operations
    # Your code here:
    pass

# Exercise 5: Type conversion
def exercise_5():
    """
    Demonstrate type conversion between different data types.
    
    Returns:
        dict: Dictionary showing original values and their conversions
        Keys: 'string_to_int', 'int_to_float', 'float_to_string', 'int_to_bool', 'string_to_bool'
        Example: {'string_to_int': ('123', 123), 'int_to_float': (42, 42.0), ...}
    """
    # TODO: Demonstrate type conversion between different data types
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
    # TODO: Demonstrate multiple assignment
    # Your code here:
    pass

# Exercise 9: Variable swapping
def exercise_9():
    """
    Demonstrate variable swapping without using a temporary variable.
    
    Returns:
        dict: Dictionary showing before and after values
        Example: {'before': (5, 10), 'after': (10, 5)}
    """
    # TODO: Demonstrate variable swapping without temporary variable
    # Your code here:
    return {'before': (5, 10), 'after': (10, 5)}

# Exercise 10: User profile
def exercise_10():
    """
    Create a user profile using all data types learned.
    
    Returns:
        dict: Complete user profile with various data types
        Keys: 'username', 'age', 'height', 'is_premium', 'hobbies' (list), 'settings' (dict)
    """
    # TODO: Create a user profile using all data types learned
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
