"""
Day 1 Exercises: Environment Setup and Hello World
==================================================

Complete each function by writing the required code.
Each function should return the expected value as specified.

Instructions:
1. Complete each exercise function below
2. Run this file to test your solutions: python day1_exercises.py
3. Check your work with automated tests: python -m pytest tests/test_day1.py -v

Tips:
- Read the function docstring to understand what's expected
- The function should return the specified value
- Use print() if you want to see output, but return the required value
- Don't worry about making mistakes - they're part of learning!
"""

def exercise_1():
    """
    Return the string "Hello, Python!"
    
    Returns:
        str: The exact string "Hello, Python!"
    """
    # Your code here:
    return "Hello, Python!"

def exercise_2():
    """
    Return a list containing your name, age, and favorite hobby as strings.
    
    Returns:
        list: [name, age_as_string, hobby]
        Example: ["Alice", "25", "Reading"]
    """
    # Your code here:
    arr = ["Alice", "25", "Reading"]
    return arr

def exercise_3():
    """
    Return your favorite number (as an integer) and a sentence about it.
    
    Returns:
        tuple: (favorite_number, sentence_with_number)
        Example: (42, "My favorite number is 42")
    """
    # Your code here:
    
    tup = (42, "My favorite number is 42")
    return tup

def exercise_4():
    """
    Return a sentence that combines text and numbers.
    
    Returns:
        str: A sentence like "I have 2 cats and 1 dog"
    """
    # Your code here:
    return "I have 2 cats and 1 dog"

def exercise_5():
    """
    Return a multi-line string containing ASCII art (at least 3 lines).
    
    Returns:
        str: ASCII art as a multi-line string
        Example: "  *  \n *** \n*****"
    """
    # Your code here:
    return "  *  \n *** \n*****"

def exercise_6():
    """
    Return a 4-line story as a single string with newlines.
    
    Returns:
        str: A story with exactly 4 lines separated by \n
        Example: "Line 1\nLine 2\nLine 3\nLine 4"
    """
    # Your code here:
    return "Line 1\nLine 2\nLine 3\nLine 4"

def exercise_7():
    """
    Return a list of three strings demonstrating different quote usage:
    - One string using single quotes
    - One string using double quotes  
    - One string containing both single and double quotes
    
    Returns:
        list: [single_quote_string, double_quote_string, mixed_quote_string]
        Example: ['Hello world', "Python is great", "She said 'Hello!' to me"]
    """
    # Your code here:
    return ['Hello world', "Python is great", "She said 'Hello!' to me"]


def exercise_8():
    """
    Return a string that would be a good comment for a print statement.
    
    Returns:
        str: A helpful comment explaining what a print statement does
        Example: "This prints a message to the console"
    """
    # Your code here:
    return "This prints a message to the console"

# Test runner - you can run this file to see your results
if __name__ == "__main__":
    print("=== Day 1 Exercises: Hello World and Print Statements ===")
    print()
    
    exercises = [
        ("Exercise 1", exercise_1, "Should return 'Hello, Python!'"),
        ("Exercise 2", exercise_2, "Should return [name, age, hobby] as strings"),
        ("Exercise 3", exercise_3, "Should return (number, sentence)"),
        ("Exercise 4", exercise_4, "Should return sentence with text and numbers"),
        ("Exercise 5", exercise_5, "Should return ASCII art (3+ lines)"),
        ("Exercise 6", exercise_6, "Should return 4-line story"),
        ("Exercise 7", exercise_7, "Should return 3 strings with different quotes"),
        ("Exercise 8", exercise_8, "Should return a helpful comment"),
    ]
    
    for name, func, description in exercises:
        print(f"{name}: {description}")
        try:
            result = func()
            if result is not None:
                print(f"  ✓ Result: {repr(result)}")
            else:
                print(f"  ✗ Not implemented (returns None)")
        except Exception as e:
            print(f"  ✗ Error: {e}")
        print()
    
    print("=== Run the tests to check your work ===")
    print("python -m pytest tests/test_day1.py -v")
