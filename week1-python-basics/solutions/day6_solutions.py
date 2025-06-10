"""
Day 6 Solutions: Dictionaries Basics
===================================

Complete solutions for dictionary operations and data management.
"""

print("=== Day 6 Solutions: Dictionaries ===")
print()

# Exercise 1: Personal Profile Dictionary
print("Exercise 1: Personal Profile")
profile = {
    "name": "Alex Johnson",
    "age": 28,
    "city": "San Francisco",
    "email": "alex.johnson@email.com",
    "phone": "555-123-4567",
    "occupation": "Software Engineer"
}

# Print entire dictionary
print("Profile:", profile)

# Access individual values
print(f"\nName: {profile['name']}")
print(f"Age: {profile['age']}")
print(f"Location: {profile['city']}")

# Update values
profile["age"] = 29
profile["city"] = "Seattle"
print(f"\nUpdated age to {profile['age']}")
print(f"Moved to {profile['city']}")

# Add new key-value pairs
profile["skills"] = ["Python", "JavaScript", "SQL"]
profile["hobbies"] = ["Reading", "Hiking", "Photography"]
profile["linkedin"] = "linkedin.com/in/alexjohnson"

print("\nUpdated profile with new fields:")
for key, value in profile.items():
    print(f"  {key}: {value}")

print()

# Exercise 2: Contact Book
print("Exercise 2: Contact Book")
contacts = {}

def add_contact(name, phone, email, address):
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Added contact: {name}")

def search_contact(name):
    if name in contacts:
        contact = contacts[name]
        print(f"\nContact found: {name}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
        print(f"  Address: {contact['address']}")
        return contact
    else:
        print(f"Contact '{name}' not found")
        return None

def update_contact(name, field, new_value):
    if name in contacts:
        if field in contacts[name]:
            old_value = contacts[name][field]
            contacts[name][field] = new_value
            print(f"Updated {name}'s {field} from '{old_value}' to '{new_value}'")
        else:
            print(f"Field '{field}' not found for {name}")
    else:
        print(f"Contact '{name}' not found")

def display_all_contacts():
    if not contacts:
        print("No contacts in the book")
        return
    
    print(f"\nAll Contacts ({len(contacts)} total):")
    for name, info in sorted(contacts.items()):
        print(f"\n{name}:")
        for field, value in info.items():
            print(f"  {field.title()}: {value}")

# Test the contact book
add_contact("Alice Smith", "555-0001", "alice@email.com", "123 Main St")
add_contact("Bob Jones", "555-0002", "bob@email.com", "456 Oak Ave")
add_contact("Carol Davis", "555-0003", "carol@email.com", "789 Pine Rd")

display_all_contacts()
search_contact("Bob Jones")
update_contact("Alice Smith", "phone", "555-9999")

print()

# Exercise 3: Grade Book System
print("Exercise 3: Grade Book")
gradebook = {
    "Alice": {"Math": 85, "Science": 92, "English": 78, "History": 88},
    "Bob": {"Math": 79, "Science": 88, "English": 85, "History": 82},
    "Carol": {"Math": 95, "Science": 90, "English": 92, "History": 94},
    "David": {"Math": 73, "Science": 78, "English": 80, "History": 75},
}

# Calculate each student's average
print("Student Averages:")
student_averages = {}
for student, grades in gradebook.items():
    average = sum(grades.values()) / len(grades)
    student_averages[student] = average
    print(f"  {student}: {average:.1f}")

# Calculate class average for each subject
print("\nSubject Averages:")
subjects = ["Math", "Science", "English", "History"]
subject_averages = {}
for subject in subjects:
    total = sum(gradebook[student][subject] for student in gradebook)
    average = total / len(gradebook)
    subject_averages[subject] = average
    print(f"  {subject}: {average:.1f}")

# Overall class average
all_grades = []
for student_grades in gradebook.values():
    all_grades.extend(student_grades.values())
overall_average = sum(all_grades) / len(all_grades)
print(f"\nOverall Class Average: {overall_average:.1f}")

# Student with highest average
top_student = max(student_averages, key=student_averages.get)
print(f"Top Student: {top_student} ({student_averages[top_student]:.1f})")

print()

# Exercise 4: Inventory Management
print("Exercise 4: Inventory Management")
inventory = {
    "laptop": {"price": 999.99, "quantity": 15, "category": "electronics"},
    "phone": {"price": 599.99, "quantity": 25, "category": "electronics"},
    "desk": {"price": 299.99, "quantity": 10, "category": "furniture"},
    "chair": {"price": 149.99, "quantity": 20, "category": "furniture"},
    "headphones": {"price": 79.99, "quantity": 30, "category": "electronics"},
    "mouse": {"price": 29.99, "quantity": 50, "category": "electronics"},
}

def add_item(name, price, quantity, category):
    inventory[name] = {
        "price": price,
        "quantity": quantity,
        "category": category
    }
    print(f"Added {name} to inventory")

def update_quantity(name, change):
    if name in inventory:
        old_qty = inventory[name]["quantity"]
        inventory[name]["quantity"] += change
        print(f"Updated {name}: {old_qty} → {inventory[name]['quantity']}")
    else:
        print(f"Item '{name}' not found")

def calculate_total_value():
    total = 0
    for item, details in inventory.items():
        value = details["price"] * details["quantity"]
        total += value
    return total

def low_stock_report(threshold=15):
    print(f"\nLow Stock Report (threshold: {threshold}):")
    low_items = []
    for item, details in inventory.items():
        if details["quantity"] <= threshold:
            low_items.append((item, details["quantity"]))
    
    if low_items:
        for item, qty in sorted(low_items, key=lambda x: x[1]):
            print(f"  {item}: {qty} units")
    else:
        print("  No items below threshold")

# Test inventory functions
print(f"Total Inventory Value: ${calculate_total_value():,.2f}")
low_stock_report()

# Add and update items
add_item("keyboard", 49.99, 8, "electronics")
update_quantity("desk", -5)
update_quantity("keyboard", 12)

# Search by category
print("\nElectronics Category:")
for item, details in inventory.items():
    if details["category"] == "electronics":
        print(f"  {item}: ${details['price']} ({details['quantity']} units)")

print()

# Exercise 5: Word Frequency Counter
print("Exercise 5: Word Frequency Counter")

def count_word_frequency(text):
    # Clean and split text
    words = text.lower().replace('.', '').replace(',', '').split()
    
    # Count frequencies
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def display_frequency_report(frequency_dict):
    # Sort by frequency (descending)
    sorted_words = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Statistics
    total_words = sum(frequency_dict.values())
    unique_words = len(frequency_dict)
    most_common = sorted_words[0] if sorted_words else ("", 0)
    
    print(f"\nWord Frequency Analysis:")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Most common: '{most_common[0]}' ({most_common[1]} times)")
    
    print("\nTop 10 words:")
    for word, count in sorted_words[:10]:
        print(f"  '{word}': {count}")

# Test with sample text
sample_text = "The quick brown fox jumps over the lazy dog. The dog was sleeping. The fox was quick."
frequency = count_word_frequency(sample_text)
display_frequency_report(frequency)

print()

# Exercise 6: Student Database
print("Exercise 6: Student Database")
students = {
    "S001": {
        "name": "Emma Wilson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
        "courses": ["CS101", "MATH201", "PHYS101"]
    },
    "S002": {
        "name": "James Chen",
        "age": 21,
        "major": "Engineering",
        "gpa": 3.6,
        "courses": ["ENG101", "MATH201", "CHEM101"]
    },
    "S003": {
        "name": "Sophia Martinez",
        "age": 19,
        "major": "Computer Science",
        "gpa": 3.9,
        "courses": ["CS101", "CS102", "MATH101"]
    }
}

def add_student(student_id, name, age, major, gpa, courses):
    students[student_id] = {
        "name": name,
        "age": age,
        "major": major,
        "gpa": gpa,
        "courses": courses
    }
    print(f"Added student: {name} ({student_id})")

def add_course_to_student(student_id, course):
    if student_id in students:
        students[student_id]["courses"].append(course)
        print(f"Added {course} to {students[student_id]['name']}'s courses")
    else:
        print(f"Student {student_id} not found")

def calculate_average_gpa():
    if not students:
        return 0
    total_gpa = sum(student["gpa"] for student in students.values())
    return total_gpa / len(students)

def find_students_by_major(major):
    matching = []
    for sid, student in students.items():
        if student["major"] == major:
            matching.append((sid, student["name"]))
    return matching

def generate_student_report(student_id):
    if student_id not in students:
        print(f"Student {student_id} not found")
        return
    
    student = students[student_id]
    print(f"\n--- Student Report ---")
    print(f"ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}")
    print(f"GPA: {student['gpa']}")
    print(f"Courses: {', '.join(student['courses'])}")

# Test student database
print(f"Average GPA: {calculate_average_gpa():.2f}")

cs_students = find_students_by_major("Computer Science")
print(f"\nComputer Science Students:")
for sid, name in cs_students:
    print(f"  {sid}: {name}")

generate_student_report("S001")
add_course_to_student("S001", "CS201")

print()

# Exercise 7: Configuration Manager
print("Exercise 7: Configuration Manager")
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp",
        "credentials": {
            "username": "admin",
            "password": "secret123"
        }
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30,
        "retry_count": 3
    },
    "features": {
        "logging": True,
        "caching": False,
        "debug_mode": True
    }
}

def get_config_value(path):
    # Split path by dots
    keys = path.split('.')
    value = config
    
    try:
        for key in keys:
            value = value[key]
        return value
    except KeyError:
        return None

def set_config_value(path, new_value):
    keys = path.split('.')
    current = config
    
    # Navigate to the parent of the target key
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    
    # Set the value
    current[keys[-1]] = new_value
    print(f"Set {path} = {new_value}")

def display_config(d=None, indent=0):
    if d is None:
        d = config
        print("Configuration:")
    
    for key, value in d.items():
        if isinstance(value, dict):
            print("  " * indent + f"{key}:")
            display_config(value, indent + 1)
        else:
            print("  " * indent + f"{key}: {value}")

# Test configuration manager
print(f"Database host: {get_config_value('database.host')}")
print(f"API timeout: {get_config_value('api.timeout')}")
print(f"Debug mode: {get_config_value('features.debug_mode')}")

set_config_value('api.timeout', 60)
set_config_value('features.caching', True)

display_config()

print()

# Exercise 8: Dictionary Operations
print("Exercise 8: Dictionary Operations")
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4, "e": 5}

# Merge dictionaries
def merge_dictionaries(d1, d2):
    # Create new dictionary with d1's values
    merged = d1.copy()
    # Update with d2's values (overwrites conflicts)
    merged.update(d2)
    return merged

merged = merge_dictionaries(dict1, dict2)
print(f"Merged: {merged}")

# Filter dictionary
def filter_dictionary(d, condition):
    return {k: v for k, v in d.items() if condition(k, v)}

# Keep only even values
even_values = filter_dictionary(merged, lambda k, v: v % 2 == 0)
print(f"Even values only: {even_values}")

# Transform values
def transform_values(d, transform_func):
    return {k: transform_func(v) for k, v in d.items()}

doubled = transform_values(dict1, lambda x: x * 2)
print(f"Doubled values: {doubled}")

# Group list of dictionaries
people = [
    {"name": "Alice", "age": 25, "city": "NYC"},
    {"name": "Bob", "age": 30, "city": "LA"},
    {"name": "Carol", "age": 25, "city": "NYC"},
    {"name": "David", "age": 30, "city": "Chicago"}
]

def group_by_key(list_of_dicts, key):
    groups = {}
    for item in list_of_dicts:
        group_key = item.get(key)
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(item)
    return groups

grouped_by_age = group_by_key(people, "age")
print("\nGrouped by age:")
for age, group in grouped_by_age.items():
    names = [p["name"] for p in group]
    print(f"  Age {age}: {names}")

print()

# Challenge: Advanced Dictionary Applications
print("Challenge: Advanced Applications")

# 1. Recipe Manager
recipes = {
    "pasta_carbonara": {
        "ingredients": {
            "pasta": "400g",
            "eggs": "4",
            "bacon": "200g",
            "parmesan": "100g",
            "black_pepper": "to taste"
        },
        "instructions": [
            "Cook pasta according to package directions",
            "Fry bacon until crispy",
            "Beat eggs with parmesan",
            "Mix hot pasta with egg mixture",
            "Add bacon and pepper"
        ],
        "servings": 4
    }
}

def add_recipe(name, ingredients, instructions, servings):
    recipes[name] = {
        "ingredients": ingredients,
        "instructions": instructions,
        "servings": servings
    }
    print(f"Added recipe: {name}")

def scale_recipe(recipe_name, scale_factor):
    if recipe_name not in recipes:
        print(f"Recipe '{recipe_name}' not found")
        return None
    
    recipe = recipes[recipe_name]
    scaled = {
        "ingredients": {},
        "instructions": recipe["instructions"].copy(),
        "servings": recipe["servings"] * scale_factor
    }
    
    # Scale ingredients
    for ingredient, amount in recipe["ingredients"].items():
        # Simple scaling for demo (real implementation would parse units)
        scaled["ingredients"][ingredient] = f"scaled: {amount} x {scale_factor}"
    
    return scaled

# Test recipe manager
print("Pasta Carbonara Recipe:")
recipe = recipes["pasta_carbonara"]
print(f"Servings: {recipe['servings']}")
print("Ingredients:")
for ing, amount in recipe["ingredients"].items():
    print(f"  - {ing}: {amount}")

# 2. Library System
library = {
    "books": {
        "B001": {"title": "Python Basics", "author": "John Doe", "available": True},
        "B002": {"title": "Data Science", "author": "Jane Smith", "available": True}
    },
    "members": {
        "M001": {"name": "Alice Brown", "books_borrowed": []},
        "M002": {"name": "Bob Green", "books_borrowed": []}
    },
    "borrowed": {}
}

def checkout_book(member_id, book_id):
    if book_id in library["books"] and library["books"][book_id]["available"]:
        if member_id in library["members"]:
            # Update book status
            library["books"][book_id]["available"] = False
            
            # Update member record
            library["members"][member_id]["books_borrowed"].append(book_id)
            
            # Record transaction
            library["borrowed"][book_id] = member_id
            
            book_title = library["books"][book_id]["title"]
            member_name = library["members"][member_id]["name"]
            print(f"{member_name} checked out '{book_title}'")
        else:
            print(f"Member {member_id} not found")
    else:
        print(f"Book {book_id} not available")

def return_book(book_id):
    if book_id in library["borrowed"]:
        member_id = library["borrowed"][book_id]
        
        # Update book status
        library["books"][book_id]["available"] = True
        
        # Update member record
        library["members"][member_id]["books_borrowed"].remove(book_id)
        
        # Remove transaction
        del library["borrowed"][book_id]
        
        book_title = library["books"][book_id]["title"]
        print(f"'{book_title}' has been returned")
    else:
        print(f"Book {book_id} was not borrowed")

# Test library system
checkout_book("M001", "B001")
checkout_book("M002", "B002")
return_book("B001")

print()
print("=== Day 6 Solutions Complete! ===")

"""
Teaching Notes for Mentors:
===========================

Key Concepts Demonstrated:
1. Dictionary creation and initialization
2. Accessing and modifying values
3. Nested dictionaries
4. Dictionary methods (get, update, items, etc.)
5. Dictionary comprehensions
6. Complex data structures
7. Real-world applications

Important Dictionary Concepts:
- Keys must be immutable (strings, numbers, tuples)
- Values can be any type
- Dictionaries are unordered (Python 3.7+ maintains insertion order)
- Key lookup is O(1) - very fast
- Use .get() for safe access
- Dictionary comprehensions for transformations

Common Challenges:
1. KeyError when accessing non-existent keys
2. Modifying dictionary while iterating
3. Understanding nested dictionary access
4. Choosing between lists and dictionaries
5. Deep vs shallow copying

Real-World Applications:
- Configuration management
- User profiles and settings
- Database records
- Caching systems
- API responses
- Inventory management
- Grade tracking

Code Quality Features:
- Safe dictionary access with .get()
- Clear data structure design
- Proper error handling
- Meaningful key names
- Good use of dictionary methods
"""