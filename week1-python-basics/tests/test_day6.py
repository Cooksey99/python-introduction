"""
Day 6 Tests: Dictionary Operations and Data Management
======================================================

Tests for Day 6 concepts: dictionary creation, manipulation, and data structures.
"""

import pytest
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_dictionary_creation():
    """Test basic dictionary creation and initialization"""
    # Empty dictionary
    empty_dict = {}
    assert len(empty_dict) == 0
    assert empty_dict == {}
    
    # Dictionary with initial values
    person = {"name": "Alice", "age": 30, "city": "NYC"}
    assert len(person) == 3
    assert person["name"] == "Alice"
    
    # Using dict() constructor
    person2 = dict(name="Bob", age=25, city="LA")
    assert person2["name"] == "Bob"
    
    # From list of tuples
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    dict_from_pairs = dict(pairs)
    assert dict_from_pairs == {"a": 1, "b": 2, "c": 3}

def test_dictionary_access():
    """Test dictionary access methods"""
    student = {"name": "John", "grade": 85, "subject": "Math"}
    
    # Direct access
    assert student["name"] == "John"
    assert student["grade"] == 85
    
    # get() method (safe access)
    assert student.get("name") == "John"
    assert student.get("missing") is None
    assert student.get("missing", "default") == "default"
    
    # Key error for missing keys
    with pytest.raises(KeyError):
        student["missing_key"]

def test_dictionary_modification():
    """Test dictionary modification operations"""
    data = {"a": 1, "b": 2}
    
    # Add new key-value pair
    data["c"] = 3
    assert data == {"a": 1, "b": 2, "c": 3}
    
    # Update existing value
    data["a"] = 10
    assert data["a"] == 10
    
    # Update multiple values
    data.update({"b": 20, "d": 4})
    assert data["b"] == 20
    assert data["d"] == 4
    
    # Delete key
    del data["c"]
    assert "c" not in data
    
    # pop() - remove and return value
    popped = data.pop("d")
    assert popped == 4
    assert "d" not in data

def test_dictionary_methods():
    """Test dictionary methods"""
    colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
    
    # keys()
    keys = list(colors.keys())
    assert set(keys) == {"red", "green", "blue"}
    
    # values()
    values = list(colors.values())
    assert "#FF0000" in values
    assert "#00FF00" in values
    
    # items()
    items = list(colors.items())
    assert ("red", "#FF0000") in items
    assert len(items) == 3
    
    # clear()
    temp_dict = colors.copy()
    temp_dict.clear()
    assert len(temp_dict) == 0
    assert len(colors) == 3  # Original unchanged

def test_dictionary_membership():
    """Test membership testing in dictionaries"""
    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    
    # Key membership
    assert "apples" in inventory
    assert "grapes" not in inventory
    
    # Value membership (requires values())
    assert 10 in inventory.values()
    assert 99 not in inventory.values()

def test_nested_dictionaries():
    """Test nested dictionary operations"""
    students = {
        "student1": {
            "name": "Alice",
            "grades": {"math": 85, "science": 92},
            "age": 20
        },
        "student2": {
            "name": "Bob", 
            "grades": {"math": 78, "science": 88},
            "age": 21
        }
    }
    
    # Access nested values
    assert students["student1"]["name"] == "Alice"
    assert students["student1"]["grades"]["math"] == 85
    assert students["student2"]["age"] == 21
    
    # Modify nested values
    students["student1"]["grades"]["english"] = 90
    assert students["student1"]["grades"]["english"] == 90
    
    # Add new nested structure
    students["student3"] = {"name": "Carol", "grades": {}, "age": 19}
    assert students["student3"]["name"] == "Carol"

def test_dictionary_comprehensions():
    """Test dictionary comprehensions"""
    # Basic comprehension
    squares = {x: x**2 for x in range(5)}
    assert squares == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    
    # With condition
    even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
    assert even_squares == {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
    
    # From existing dictionary
    prices = {"apple": 1.20, "banana": 0.50, "orange": 0.80}
    expensive = {k: v for k, v in prices.items() if v > 1.00}
    assert expensive == {"apple": 1.20}
    
    # Transform values
    doubled_prices = {k: v * 2 for k, v in prices.items()}
    assert doubled_prices["apple"] == 2.40

def test_dictionary_operations():
    """Test dictionary operations and functions"""
    grades = {"Alice": 85, "Bob": 92, "Carol": 78, "David": 88}
    
    # Length
    assert len(grades) == 4
    
    # Max/Min by value
    highest_grade = max(grades.values())
    lowest_grade = min(grades.values())
    assert highest_grade == 92
    assert lowest_grade == 78
    
    # Max/Min by key
    best_student = max(grades, key=grades.get)
    assert best_student == "Bob"
    
    # Sum values
    total_grades = sum(grades.values())
    assert total_grades == 343

def test_dictionary_merging():
    """Test dictionary merging operations"""
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"b": 20, "e": 5}  # Has conflicting key
    
    # Merge with update()
    merged = dict1.copy()
    merged.update(dict2)
    assert merged == {"a": 1, "b": 2, "c": 3, "d": 4}
    
    # Merge with conflicts (last one wins)
    merged.update(dict3)
    assert merged["b"] == 20  # Overwritten
    assert merged["e"] == 5
    
    # Merge with dict() and **
    combined = {**dict1, **dict2}
    assert combined == {"a": 1, "b": 2, "c": 3, "d": 4}

def test_word_frequency():
    """Test word frequency counting with dictionaries"""
    text = "the quick brown fox jumps over the lazy dog the fox"
    words = text.split()
    
    # Count word frequencies
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    assert frequency["the"] == 3
    assert frequency["fox"] == 2
    assert frequency["quick"] == 1
    assert len(frequency) == 9  # unique words
    
    # Alternative using dict comprehension
    word_set = set(words)
    freq_comp = {word: words.count(word) for word in word_set}
    assert freq_comp["the"] == 3

def test_grouping_data():
    """Test grouping data with dictionaries"""
    students = [
        {"name": "Alice", "grade": "A", "subject": "Math"},
        {"name": "Bob", "grade": "B", "subject": "Math"},
        {"name": "Carol", "grade": "A", "subject": "Science"},
        {"name": "David", "grade": "B", "subject": "Math"},
        {"name": "Eve", "grade": "A", "subject": "Science"}
    ]
    
    # Group by grade
    by_grade = {}
    for student in students:
        grade = student["grade"]
        if grade not in by_grade:
            by_grade[grade] = []
        by_grade[grade].append(student["name"])
    
    assert by_grade["A"] == ["Alice", "Carol", "Eve"]
    assert by_grade["B"] == ["Bob", "David"]
    
    # Group by subject
    by_subject = {}
    for student in students:
        subject = student["subject"]
        if subject not in by_subject:
            by_subject[subject] = []
        by_subject[subject].append(student["name"])
    
    assert by_subject["Math"] == ["Alice", "Bob", "David"]
    assert by_subject["Science"] == ["Carol", "Eve"]

def test_configuration_management():
    """Test configuration management with nested dictionaries"""
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {
                "username": "admin",
                "password": "secret"
            }
        },
        "api": {
            "base_url": "https://api.example.com",
            "timeout": 30
        }
    }
    
    # Access nested configuration
    assert config["database"]["host"] == "localhost"
    assert config["database"]["credentials"]["username"] == "admin"
    assert config["api"]["timeout"] == 30
    
    # Safe nested access
    def get_config_value(config, path):
        keys = path.split('.')
        value = config
        try:
            for key in keys:
                value = value[key]
            return value
        except KeyError:
            return None
    
    assert get_config_value(config, "database.host") == "localhost"
    assert get_config_value(config, "database.port") == 5432
    assert get_config_value(config, "missing.key") is None

def test_inventory_management():
    """Test inventory management system"""
    inventory = {
        "laptop": {"price": 999.99, "quantity": 15, "category": "electronics"},
        "desk": {"price": 299.99, "quantity": 10, "category": "furniture"},
        "phone": {"price": 599.99, "quantity": 25, "category": "electronics"}
    }
    
    # Calculate total inventory value
    total_value = sum(item["price"] * item["quantity"] for item in inventory.values())
    assert abs(total_value - 32999.60) < 0.01  # Account for floating point precision
    
    # Find items by category
    electronics = {k: v for k, v in inventory.items() if v["category"] == "electronics"}
    assert len(electronics) == 2
    assert "laptop" in electronics
    assert "phone" in electronics
    
    # Find low stock items (quantity < 20)
    low_stock = {k: v for k, v in inventory.items() if v["quantity"] < 20}
    assert "laptop" in low_stock
    assert "desk" in low_stock
    assert "phone" not in low_stock

def test_grade_book_system():
    """Test grade book system with complex operations"""
    gradebook = {
        "Alice": {"Math": 85, "Science": 92, "English": 78},
        "Bob": {"Math": 79, "Science": 88, "English": 85},
        "Carol": {"Math": 95, "Science": 90, "English": 92}
    }
    
    # Calculate student averages
    student_averages = {}
    for student, grades in gradebook.items():
        average = sum(grades.values()) / len(grades)
        student_averages[student] = average
    
    assert abs(student_averages["Alice"] - 85.0) < 0.1
    assert abs(student_averages["Carol"] - 92.33) < 0.1
    
    # Calculate subject averages
    subjects = ["Math", "Science", "English"]
    subject_averages = {}
    for subject in subjects:
        total = sum(gradebook[student][subject] for student in gradebook)
        average = total / len(gradebook)
        subject_averages[subject] = average
    
    assert abs(subject_averages["Math"] - 86.33) < 0.1
    assert abs(subject_averages["Science"] - 90.0) < 0.1
    
    # Find top student
    top_student = max(student_averages, key=student_averages.get)
    assert top_student == "Carol"

def test_contact_management():
    """Test contact management system"""
    contacts = {
        "Alice Smith": {
            "phone": "555-0001",
            "email": "alice@email.com",
            "address": "123 Main St",
            "birthday": "1990-05-15"
        },
        "Bob Jones": {
            "phone": "555-0002", 
            "email": "bob@email.com",
            "address": "456 Oak Ave",
            "birthday": "1985-08-22"
        }
    }
    
    # Search by name
    def search_contact(contacts, name):
        return contacts.get(name)
    
    alice = search_contact(contacts, "Alice Smith")
    assert alice["phone"] == "555-0001"
    assert search_contact(contacts, "Unknown") is None
    
    # Search by phone
    def search_by_phone(contacts, phone):
        for name, info in contacts.items():
            if info["phone"] == phone:
                return name, info
        return None, None
    
    name, info = search_by_phone(contacts, "555-0002")
    assert name == "Bob Jones"
    assert info["email"] == "bob@email.com"

def test_dictionary_sorting():
    """Test sorting dictionaries"""
    grades = {"Bob": 85, "Alice": 92, "Carol": 78, "David": 88}
    
    # Sort by keys
    sorted_by_name = dict(sorted(grades.items()))
    keys_list = list(sorted_by_name.keys())
    assert keys_list == ["Alice", "Bob", "Carol", "David"]
    
    # Sort by values (ascending)
    sorted_by_grade_asc = dict(sorted(grades.items(), key=lambda x: x[1]))
    first_student = list(sorted_by_grade_asc.keys())[0]
    assert first_student == "Carol"  # Lowest grade
    
    # Sort by values (descending)
    sorted_by_grade_desc = dict(sorted(grades.items(), key=lambda x: x[1], reverse=True))
    top_student = list(sorted_by_grade_desc.keys())[0]
    assert top_student == "Alice"  # Highest grade

def test_dictionary_filtering():
    """Test filtering dictionaries"""
    products = {
        "laptop": {"price": 999, "category": "electronics", "in_stock": True},
        "desk": {"price": 200, "category": "furniture", "in_stock": False},
        "phone": {"price": 599, "category": "electronics", "in_stock": True},
        "chair": {"price": 150, "category": "furniture", "in_stock": True}
    }
    
    # Filter by category
    electronics = {k: v for k, v in products.items() if v["category"] == "electronics"}
    assert len(electronics) == 2
    assert "laptop" in electronics
    
    # Filter by price range
    expensive = {k: v for k, v in products.items() if v["price"] > 500}
    assert len(expensive) == 2
    assert "laptop" in expensive
    assert "phone" in expensive
    
    # Filter by availability
    available = {k: v for k, v in products.items() if v["in_stock"]}
    assert len(available) == 3
    assert "desk" not in available

def test_dictionary_transformations():
    """Test dictionary transformation operations"""
    prices = {"apple": 1.20, "banana": 0.50, "orange": 0.80}
    
    # Transform values (apply tax)
    tax_rate = 0.1
    with_tax = {k: round(v * (1 + tax_rate), 2) for k, v in prices.items()}
    assert with_tax["apple"] == 1.32
    assert with_tax["banana"] == 0.55
    
    # Transform keys (uppercase)
    upper_keys = {k.upper(): v for k, v in prices.items()}
    assert "APPLE" in upper_keys
    assert upper_keys["BANANA"] == 0.50
    
    # Invert dictionary (swap keys and values)
    inverted = {v: k for k, v in prices.items()}
    assert inverted[1.20] == "apple"
    assert inverted[0.50] == "banana"

def test_dictionary_default_values():
    """Test handling default values in dictionaries"""
    # Using setdefault()
    counter = {}
    items = ["apple", "banana", "apple", "orange", "banana", "apple"]
    
    for item in items:
        counter.setdefault(item, 0)
        counter[item] += 1
    
    assert counter["apple"] == 3
    assert counter["banana"] == 2
    assert counter["orange"] == 1
    
    # Using defaultdict would be better, but testing basic dict operations
    def count_items(items):
        counts = {}
        for item in items:
            counts[item] = counts.get(item, 0) + 1
        return counts
    
    result = count_items(items)
    assert result["apple"] == 3

def test_dictionary_validation():
    """Test dictionary validation operations"""
    def validate_user_data(user):
        required_fields = ["name", "email", "age"]
        
        # Check required fields
        for field in required_fields:
            if field not in user:
                return False, f"Missing field: {field}"
        
        # Validate types
        if not isinstance(user["name"], str) or len(user["name"]) == 0:
            return False, "Name must be a non-empty string"
        
        if not isinstance(user["age"], int) or user["age"] < 0:
            return False, "Age must be a positive integer"
        
        if "@" not in user["email"]:
            return False, "Email must contain @"
        
        return True, "Valid"
    
    valid_user = {"name": "Alice", "email": "alice@example.com", "age": 25}
    is_valid, message = validate_user_data(valid_user)
    assert is_valid == True
    
    invalid_user = {"name": "", "email": "invalid", "age": -5}
    is_valid, message = validate_user_data(invalid_user)
    assert is_valid == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])