"""
Day 3 Exercises: String Operations and User Input
================================================

Complete each function by writing code that demonstrates
string manipulation, formatting, and text processing.

Each function should return the expected value as specified.
"""

def exercise_1():
    """
    Basic string operations: create and manipulate strings.
    
    Returns:
        dict: Dictionary with string operation results
        Keys: 'original', 'length', 'uppercase', 'lowercase', 'title_case', 'first_char', 'last_char'
        Example: {'original': 'Hello World', 'length': 11, 'uppercase': 'HELLO WORLD', ...}
    """
    # Your code here:
    pass

def exercise_2():
    """
    String searching and checking operations.
    
    Returns:
        dict: Dictionary with search results for the string "Python Programming"
        Keys: 'contains_python', 'starts_with_py', 'ends_with_ing', 'find_gram', 'count_o'
    """
    # Your code here:
    pass

def exercise_3():
    """
    String slicing and indexing practice.
    
    Returns:
        dict: Dictionary with slicing results from "Hello, World!"
        Keys: 'first_5', 'last_6', 'middle', 'every_2nd', 'reverse'
    """
    # Your code here:
    pass

def exercise_4():
    """
    String splitting and joining operations.
    
    Returns:
        dict: Dictionary with split/join results
        Keys: 'sentence', 'words', 'rejoined', 'csv_data', 'csv_list'
        Use sentence: "Python is a powerful programming language"
    """
    # Your code here:
    pass

def exercise_5():
    """
    String cleaning and formatting.
    
    Returns:
        dict: Dictionary with cleaned string results
        Keys: 'original', 'stripped', 'no_spaces', 'replace_spaces', 'clean_name'
        Use messy input: "  John    Doe  \n\t  "
    """
    # Your code here:
    pass

def exercise_6():
    """
    String formatting with f-strings, .format(), and % formatting.
    
    Returns:
        dict: Dictionary with formatted strings
        Keys: 'f_string', 'format_method', 'percent_format'
        Use: name="Alice", age=25, score=95.5
    """
    # Your code here:
    pass

def exercise_7():
    """
    Text analysis: analyze a given sentence.
    
    Returns:
        dict: Dictionary with analysis results for "The quick brown fox jumps over the lazy dog"
        Keys: 'char_count', 'word_count', 'vowel_count', 'consonant_count', 'unique_words'
    """
    # Your code here:
    pass

def exercise_8():
    """
    Name processing: clean and format full names.
    
    Returns:
        dict: Dictionary with name processing results
        Keys: 'cleaned_name', 'first_name', 'last_name', 'initials', 'formal_name'
        Use input: "  alice marie JOHNSON  "
    """
    # Your code here:
    pass

def exercise_9():
    """
    Email validation: check if email addresses are valid.
    
    Returns:
        dict: Dictionary with validation results for multiple emails
        Keys: 'valid_emails', 'invalid_emails'
        Test: ["user@example.com", "invalid.email", "test@domain.org", "bad@", "@domain.com"]
    """
    # Your code here:
    pass

def exercise_10():
    """
    Password strength checker: analyze password strength.
    
    Returns:
        dict: Dictionary with password analysis
        Keys: 'password', 'length_ok', 'has_upper', 'has_lower', 'has_digit', 'has_special', 'strength'
        Test password: "MySecure123!"
    """
    # Your code here:
    pass

def exercise_11():
    """
    Text encryption: implement a simple Caesar cipher.
    
    Returns:
        dict: Dictionary with encryption results
        Keys: 'original', 'encrypted', 'decrypted', 'shift'
        Use text: "HELLO" with shift of 3
    """
    # Your code here:
    pass

def exercise_12():
    """
    Word frequency counter: count word occurrences in text.
    
    Returns:
        dict: Dictionary with word frequencies
        Use text: "the quick brown fox jumps over the lazy dog the fox"
        Return: {'the': 3, 'fox': 2, 'quick': 1, ...}
    """
    # Your code here:
    pass

# Test runner
if __name__ == "__main__":
    print("=== Day 3 Exercises: String Operations ===")
    print()
    
    exercises = [
        ("Exercise 1", exercise_1, "Basic string operations"),
        ("Exercise 2", exercise_2, "String searching and checking"),
        ("Exercise 3", exercise_3, "String slicing and indexing"),
        ("Exercise 4", exercise_4, "String splitting and joining"),
        ("Exercise 5", exercise_5, "String cleaning and formatting"),
        ("Exercise 6", exercise_6, "String formatting methods"),
        ("Exercise 7", exercise_7, "Text analysis"),
        ("Exercise 8", exercise_8, "Name processing"),
        ("Exercise 9", exercise_9, "Email validation"),
        ("Exercise 10", exercise_10, "Password strength checker"),
        ("Exercise 11", exercise_11, "Caesar cipher encryption"),
        ("Exercise 12", exercise_12, "Word frequency counter"),
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
    print("python -m pytest tests/test_day3.py -v")