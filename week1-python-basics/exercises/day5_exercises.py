"""
Day 5 Exercises: Lists Basics
============================

Complete each function by writing code that demonstrates
list creation, manipulation, and algorithms.

Each function should return the expected value as specified.
"""

import random

def exercise_1():
    """
    Create different types of lists and analyze them.
    
    Returns:
        dict: Dictionary with list information
        Keys: 'movies', 'numbers', 'mixed', 'empty', 'lengths', 'first_last'
        Create lists for: top 5 movies, numbers 1-10, mixed data types, empty list
    """
    # Your code here:
    pass

def exercise_2():
    """
    Shopping list manager with basic operations.
    
    Returns:
        dict: Dictionary with shopping list operations
        Keys: 'initial_list', 'after_additions', 'after_removal', 'final_list'
        Start empty, add ["Milk", "Bread", "Eggs"], remove "Bread", add ["Apples", "Cheese"]
    """
    # Your code here:
    pass

def exercise_3():
    """
    Grade analyzer: calculate statistics from grades.
    
    Returns:
        dict: Dictionary with grade analysis
        Keys: 'grades', 'average', 'highest', 'lowest', 'grade_counts', 'sorted_asc', 'sorted_desc'
        Use grades: [85, 92, 78, 95, 88, 73, 91, 82, 87, 90]
    """
    # Your code here:
    pass

def exercise_4():
    """
    List methods practice: demonstrate all major list methods.
    
    Returns:
        dict: Dictionary with method results
        Keys: 'original', 'after_append', 'after_insert', 'after_remove', 'after_pop', 'index_result', 'count_result'
        Start with: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    """
    # Your code here:
    pass

def exercise_5():
    """
    Number list operations and analysis.
    
    Returns:
        dict: Dictionary with number analysis
        Keys: 'numbers', 'sum', 'average', 'evens', 'odds', 'divisible_by_3', 'greater_than_50', 'doubled', 'second_largest'
        Use 10 random numbers between 1-100
    """
    # Your code here:
    pass

def exercise_6():
    """
    2D lists (matrix) operations.
    
    Returns:
        dict: Dictionary with matrix operations
        Keys: 'matrix', 'row_sums', 'col_sums', 'main_diagonal_sum', 'anti_diagonal_sum'
        Create 3x3 matrix with numbers 1-9
    """
    # Your code here:
    pass

def exercise_7():
    """
    Word list processing and analysis.
    
    Returns:
        dict: Dictionary with word analysis
        Keys: 'sentence', 'words', 'word_count', 'longest_word', 'shortest_word', 'length_counts', 'unique_words', 'vowel_words'
        Use sentence: "The quick brown fox jumps over the lazy dog and the cat"
    """
    # Your code here:
    pass

def exercise_8():
    """
    List algorithms implementation.
    
    Returns:
        dict: Dictionary with algorithm results
        Keys: 'test_list', 'linear_search', 'find_max', 'reverse_list', 'remove_duplicates', 'merge_sorted'
        Use test_list: [64, 34, 25, 12, 22, 11, 90]
    """
    # Your code here:
    pass

def exercise_9():
    """
    Advanced list operations.
    
    Returns:
        dict: Dictionary with advanced operations
        Keys: 'nested_list', 'flattened', 'grouped_by_even_odd', 'rotated_list'
        Use nested_list: [[1, 2], [3, [4, 5]], 6, [7, 8, 9]]
    """
    # Your code here:
    pass

def exercise_10():
    """
    List comprehensions and filtering.
    
    Returns:
        dict: Dictionary with comprehension results
        Keys: 'squares', 'even_squares', 'filtered_words', 'word_lengths', 'matrix_flatten'
        Demonstrate various list comprehension patterns
    """
    # Your code here:
    pass

# Test runner
if __name__ == "__main__":
    print("=== Day 5 Exercises: Lists ===")
    print()
    
    exercises = [
        ("Exercise 1", exercise_1, "List creation and analysis"),
        ("Exercise 2", exercise_2, "Shopping list manager"),
        ("Exercise 3", exercise_3, "Grade analyzer"),
        ("Exercise 4", exercise_4, "List methods practice"),
        ("Exercise 5", exercise_5, "Number list operations"),
        ("Exercise 6", exercise_6, "2D lists (matrix) operations"),
        ("Exercise 7", exercise_7, "Word list processing"),
        ("Exercise 8", exercise_8, "List algorithms"),
        ("Exercise 9", exercise_9, "Advanced list operations"),
        ("Exercise 10", exercise_10, "List comprehensions"),
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
    print("python -m pytest tests/test_day5.py -v")