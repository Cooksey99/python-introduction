# Day 6: Dictionaries Basics

## 🎯 Learning Objectives

By the end of Day 6, you will be able to:
- Create and manipulate dictionaries to store key-value data
- Access, add, update, and remove dictionary elements
- Use dictionary methods for efficient data operations
- Understand when to use dictionaries vs lists
- Work with nested dictionaries and complex data structures
- Build real-world applications using dictionary data

## 📚 Core Concepts

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}

# Dictionary with initial data
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
coordinates = dict(x=10, y=20)
grades = dict([("math", 85), ("science", 92)])
```

### Accessing and Modifying
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Access values
print(person["name"])           # Alice
print(person.get("age"))        # 25
print(person.get("phone", "N/A"))  # N/A (default value)

# Modify values
person["age"] = 26              # Update existing
person["phone"] = "555-1234"    # Add new key

# Remove items
del person["city"]              # Remove key-value pair
phone = person.pop("phone")     # Remove and return value
```

### Dictionary Methods
```python
person = {"name": "Alice", "age": 25, "city": "New York"}

print(person.keys())            # dict_keys(['name', 'age', 'city'])
print(person.values())          # dict_values(['Alice', 25, 'New York'])
print(person.items())           # dict_items([('name', 'Alice'), ...])

print("name" in person)         # True
print("phone" in person)        # False
```

## 🔧 Hands-On Examples

### Example 1: Student Database
```python
print("=== Student Database ===")

students = {}

def add_student():
    student_id = input("Enter student ID: ").strip()
    if student_id in students:
        print("Student ID already exists!")
        return
    
    name = input("Enter name: ").strip().title()
    age = int(input("Enter age: "))
    major = input("Enter major: ").strip().title()
    gpa = float(input("Enter GPA: "))
    
    students[student_id] = {
        "name": name,
        "age": age,
        "major": major,
        "gpa": gpa,
        "courses": []
    }
    print(f"Added student {name} with ID {student_id}")

def view_student():
    student_id = input("Enter student ID: ").strip()
    if student_id not in students:
        print("Student not found!")
        return
    
    student = students[student_id]
    print(f"\nStudent Information:")
    print(f"ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}")
    print(f"GPA: {student['gpa']}")
    print(f"Courses: {student['courses']}")

def list_all_students():
    if not students:
        print("No students in database!")
        return
    
    print("\nAll Students:")
    print("-" * 50)
    for student_id, info in students.items():
        print(f"ID: {student_id} | Name: {info['name']} | Major: {info['major']} | GPA: {info['gpa']}")

# Sample usage
add_student()  # Add a few students
list_all_students()
view_student()
```

### Example 2: Word Frequency Counter
```python
def count_word_frequency(text):
    """Count frequency of each word in text"""
    # Clean and split text
    words = text.lower().replace(",", "").replace(".", "").split()
    
    # Count frequencies
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def display_frequency(frequency, top_n=10):
    """Display word frequencies, sorted by count"""
    # Sort by frequency (descending)
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    print(f"\nTop {top_n} most frequent words:")
    print("-" * 30)
    for i, (word, count) in enumerate(sorted_words[:top_n], 1):
        print(f"{i:2}. {word:15} : {count:3} times")
    
    print(f"\nTotal unique words: {len(frequency)}")
    print(f"Total words: {sum(frequency.values())}")

# Example usage
sample_text = """
Python is a powerful programming language. Python is easy to learn
and Python is widely used in data science, web development, and automation.
The Python community is very supportive and Python has excellent libraries.
"""

word_freq = count_word_frequency(sample_text)
display_frequency(word_freq)
```

### Example 3: Inventory Management System
```python
print("=== Inventory Management ===")

inventory = {
    "laptop": {"price": 999.99, "quantity": 15, "category": "electronics"},
    "phone": {"price": 599.99, "quantity": 25, "category": "electronics"},
    "desk": {"price": 299.99, "quantity": 8, "category": "furniture"},
    "chair": {"price": 149.99, "quantity": 12, "category": "furniture"}
}

def add_item():
    name = input("Item name: ").lower().strip()
    price = float(input("Price: $"))
    quantity = int(input("Quantity: "))
    category = input("Category: ").lower().strip()
    
    inventory[name] = {
        "price": price,
        "quantity": quantity,
        "category": category
    }
    print(f"Added {name} to inventory")

def update_quantity():
    name = input("Item name: ").lower().strip()
    if name not in inventory:
        print("Item not found!")
        return
    
    change = int(input("Quantity change (+/-): "))
    inventory[name]["quantity"] += change
    
    if inventory[name]["quantity"] < 0:
        inventory[name]["quantity"] = 0
        print("Warning: Quantity set to 0 (cannot be negative)")
    
    print(f"Updated {name} quantity to {inventory[name]['quantity']}")

def show_inventory():
    if not inventory:
        print("Inventory is empty!")
        return
    
    print("\nCurrent Inventory:")
    print("-" * 70)
    print(f"{'Item':<15} {'Price':<10} {'Qty':<5} {'Category':<15} {'Value':<10}")
    print("-" * 70)
    
    total_value = 0
    for name, details in inventory.items():
        value = details["price"] * details["quantity"]
        total_value += value
        print(f"{name:<15} ${details['price']:<9.2f} {details['quantity']:<5} "
              f"{details['category']:<15} ${value:<9.2f}")
    
    print("-" * 70)
    print(f"Total Inventory Value: ${total_value:.2f}")

def low_stock_alert(threshold=5):
    low_stock = {name: details for name, details in inventory.items() 
                 if details["quantity"] <= threshold}
    
    if low_stock:
        print(f"\nLow Stock Alert (≤{threshold} items):")
        for name, details in low_stock.items():
            print(f"- {name}: {details['quantity']} remaining")
    else:
        print("All items are well stocked!")

# Sample usage
show_inventory()
low_stock_alert()
```

### Example 4: Configuration Manager
```python
# Complex nested dictionary structure
app_config = {
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
        "version": "v2",
        "timeout": 30,
        "endpoints": {
            "users": "/users",
            "orders": "/orders",
            "products": "/products"
        }
    },
    "features": {
        "logging": True,
        "caching": True,
        "notifications": False
    }
}

def get_config_value(config, path):
    """Get nested config value using dot notation path"""
    keys = path.split(".")
    value = config
    
    for key in keys:
        if isinstance(value, dict) and key in value:
            value = value[key]
        else:
            return None
    
    return value

def set_config_value(config, path, new_value):
    """Set nested config value using dot notation path"""
    keys = path.split(".")
    current = config
    
    # Navigate to parent of target key
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    
    # Set the final value
    current[keys[-1]] = new_value

# Usage examples
print("Database host:", get_config_value(app_config, "database.host"))
print("API timeout:", get_config_value(app_config, "api.timeout"))
print("Users endpoint:", get_config_value(app_config, "api.endpoints.users"))

# Update configuration
set_config_value(app_config, "api.timeout", 60)
set_config_value(app_config, "features.debug_mode", True)

print("Updated timeout:", get_config_value(app_config, "api.timeout"))
```

## 🏋️ Practice Exercises

### Exercise 1: Contact Book
```python
# Create a contact management system with:
# - Add contact (name, phone, email, address)
# - Search contacts by name or phone
# - Update contact information
# - Delete contacts
# - Export contacts to formatted text
# - Import contacts from user input
```

### Exercise 2: Grade Book
```python
# Build a gradebook system that stores:
# - Student information (name, ID, class)
# - Multiple assignments with grades
# - Calculate GPA, class average
# - Generate report cards
# - Track attendance
```

### Exercise 3: Recipe Manager
```python
# Create a recipe database with:
# - Recipe name, ingredients (with quantities), instructions
# - Search recipes by ingredient
# - Scale recipe portions up/down
# - Calculate nutritional info (if ingredients have calories)
# - Meal planning functionality
```

### Exercise 4: Library System
```python
# Build a library management system:
# - Books (title, author, ISBN, genre, copies)
# - Members (name, ID, borrowed books)
# - Check out/return books
# - Search books by various criteria
# - Generate overdue reports
```

### Exercise 5: Sales Analytics
```python
# Analyze sales data structure:
sales_data = {
    "2024-01": {"revenue": 50000, "units": 150, "customers": 45},
    "2024-02": {"revenue": 62000, "units": 180, "customers": 52},
    # ... more months
}

# Calculate:
# - Total revenue and units for year
# - Average revenue per customer
# - Month-over-month growth
# - Best and worst performing months
```

### Challenge: Database-like Operations
```python
# Implement database-like operations on dictionaries:
# 1. JOIN: Combine two dictionaries on a common key
# 2. FILTER: Filter records based on criteria
# 3. GROUP BY: Group records by a field value
# 4. AGGREGATE: Calculate sums, averages, etc.
# 5. INDEX: Create secondary indexes for fast lookup
```

## 💡 Dictionary Methods Reference

### Basic Operations
```python
d = {"a": 1, "b": 2}

d["c"] = 3              # Add/update
value = d.get("a", 0)   # Safe access with default
value = d.pop("b")      # Remove and return
d.clear()               # Remove all items
```

### Iterating
```python
d = {"name": "Alice", "age": 25}

for key in d:                    # Iterate keys
    print(key, d[key])

for key in d.keys():            # Explicit keys iteration
    print(key)

for value in d.values():        # Iterate values
    print(value)

for key, value in d.items():    # Iterate key-value pairs
    print(key, value)
```

### Dictionary Comprehensions
```python
# Create dictionaries using comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filter and transform
words = ["apple", "banana", "cherry"]
lengths = {word: len(word) for word in words if len(word) > 5}
```

### Merging Dictionaries
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Python 3.9+
merged = dict1 | dict2          # {"a": 1, "b": 3, "c": 4}

# Alternative methods
merged = {**dict1, **dict2}     # Unpacking
merged = dict1.copy()
merged.update(dict2)
```

## ✅ Self-Check Questions

1. How do you safely access a dictionary key that might not exist?
2. What's the difference between `dict["key"]` and `dict.get("key")`?
3. How do you iterate through both keys and values simultaneously?
4. What happens when you try to access a non-existent key with `[]`?
5. How do you check if a key exists in a dictionary?
6. What's the difference between `pop()` and `del` for removing items?

## 🛠️ Common Mistakes

**Mistake 1: KeyError when accessing non-existent keys**
```python
d = {"name": "Alice"}
# print(d["age"])  # KeyError!

# Better approaches
print(d.get("age", "Unknown"))  # Unknown
if "age" in d:
    print(d["age"])
```

**Mistake 2: Modifying dictionary during iteration**
```python
d = {"a": 1, "b": 2, "c": 3}
# Wrong - will cause RuntimeError
for key in d:
    if d[key] == 2:
        del d[key]

# Right way
d = {k: v for k, v in d.items() if v != 2}
```

**Mistake 3: Using mutable objects as keys**
```python
# This won't work - lists are mutable
# d = {[1, 2]: "value"}  # TypeError!

# Use tuples instead
d = {(1, 2): "value"}   # OK
```

## 🚀 Tomorrow's Preview

Day 7 is the integration project day! You'll combine all Week 1 concepts to build a comprehensive application that demonstrates your Python fundamentals mastery.

**Test your understanding with `python -m pytest tests/test_day6.py -v`**