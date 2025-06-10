"""
Day 6 Exercises: Dictionaries Basics
===================================

Complete each function by writing code that demonstrates
dictionary operations and data management.

Each function should return the expected value as specified.
"""

def exercise_1():
    """
    Create and manipulate a personal profile dictionary.
    
    Returns:
        dict: Dictionary with personal profile operations
        Keys: 'original_profile', 'updated_profile', 'added_skills', 'profile_keys', 'profile_values'
        Include: name, age, city, email, phone, occupation
    """
    # Your code here:
    pass

def exercise_2():
    """
    Contact book management system.
    
    Returns:
        dict: Dictionary with contact book operations
        Keys: 'contacts', 'search_result', 'updated_contact', 'all_emails', 'contact_count'
        Create contacts with nested dictionaries (name, phone, email, address)
    """
    # Your code here:
    pass

def exercise_3():
    """
    Grade book system with multiple students and subjects.
    
    Returns:
        dict: Dictionary with grade book analysis
        Keys: 'gradebook', 'student_averages', 'subject_averages', 'overall_average', 'top_student'
        Include at least 3 students with 3 subjects each
    """
    # Your code here:
    pass

def exercise_4():
    """
    Inventory management system for a store.
    
    Returns:
        dict: Dictionary with inventory operations
        Keys: 'inventory', 'total_value', 'low_stock_items', 'electronics_items', 'expensive_items'
        Each item: {name: {price, quantity, category}}
    """
    # Your code here:
    pass

def exercise_5():
    """
    Word frequency counter for text analysis.
    
    Returns:
        dict: Dictionary with word frequency analysis
        Keys: 'text', 'word_frequencies', 'total_words', 'unique_words', 'most_common_word'
        Use text: "the quick brown fox jumps over the lazy dog the fox"
    """
    # Your code here:
    pass

def exercise_6():
    """
    Student database with comprehensive information.
    
    Returns:
        dict: Dictionary with student database operations
        Keys: 'students', 'cs_students', 'average_gpa', 'student_report', 'courses_by_student'
        Each student: {id: {name, age, major, gpa, courses: [list]}}
    """
    # Your code here:
    pass

def exercise_7():
    """
    Configuration manager with nested settings.
    
    Returns:
        dict: Dictionary with configuration operations
        Keys: 'config', 'database_host', 'api_timeout', 'updated_config', 'config_summary'
        Use nested structure: database, api, features sections
    """
    # Your code here:
    pass

def exercise_8():
    """
    Dictionary operations: merging, filtering, and transforming.
    
    Returns:
        dict: Dictionary with advanced operations
        Keys: 'dict1', 'dict2', 'merged', 'filtered_even', 'doubled_values', 'inverted'
        Demonstrate merge, filter, transform, and invert operations
    """
    # Your code here:
    pass

def exercise_9():
    """
    Recipe manager with ingredients and instructions.
    
    Returns:
        dict: Dictionary with recipe management
        Keys: 'recipes', 'recipe_count', 'ingredients_list', 'scaled_recipe', 'vegetarian_recipes'
        Include recipes with ingredients (with amounts) and instructions
    """
    # Your code here:
    pass

def exercise_10():
    """
    Data grouping and analysis operations.
    
    Returns:
        dict: Dictionary with grouping operations
        Keys: 'people', 'grouped_by_age', 'grouped_by_city', 'age_statistics', 'city_counts'
        Group list of people by different attributes
    """
    # Your code here:
    pass

# Test runner
if __name__ == "__main__":
    print("=== Day 6 Exercises: Dictionaries ===")
    print()
    
    exercises = [
        ("Exercise 1", exercise_1, "Personal profile dictionary"),
        ("Exercise 2", exercise_2, "Contact book management"),
        ("Exercise 3", exercise_3, "Grade book system"),
        ("Exercise 4", exercise_4, "Inventory management"),
        ("Exercise 5", exercise_5, "Word frequency counter"),
        ("Exercise 6", exercise_6, "Student database"),
        ("Exercise 7", exercise_7, "Configuration manager"),
        ("Exercise 8", exercise_8, "Dictionary operations"),
        ("Exercise 9", exercise_9, "Recipe manager"),
        ("Exercise 10", exercise_10, "Data grouping and analysis"),
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
    print("python -m pytest tests/test_day6.py -v")