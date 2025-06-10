# Day 3: String Operations and User Input

## 🎯 Learning Objectives

By the end of Day 3, you will be able to:
- Manipulate strings using built-in methods
- Format strings for clean output
- Get user input with the `input()` function
- Combine strings using concatenation and f-strings
- Handle common string operations (case conversion, splitting, etc.)
- Build interactive programs that respond to user input

## 📚 Core Concepts

### String Methods
Strings have many built-in methods for manipulation:
```python
text = "Hello World"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.replace("World", "Python"))  # Hello Python
print(len(text))         # 11
```

### User Input
The `input()` function gets text from the user:
```python
name = input("What's your name? ")
print("Hello,", name)
```

### String Formatting
Multiple ways to format strings:
```python
name = "Alice"
age = 25

# Method 1: Concatenation
print("Hello " + name + ", you are " + str(age))

# Method 2: f-strings (recommended)
print(f"Hello {name}, you are {age}")

# Method 3: .format()
print("Hello {}, you are {}".format(name, age))
```

## 🔧 Hands-On Examples

### Example 1: String Methods Showcase
```python
text = "  Python Programming is Fun!  "

print("Original:", repr(text))
print("Stripped:", text.strip())
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title Case:", text.title())
print("Length:", len(text))
print("Word count:", len(text.split()))
print("Replace:", text.replace("Fun", "Awesome"))
print("Starts with 'Python':", text.strip().startswith("Python"))
print("Ends with '!':", text.strip().endswith("!"))
```

### Example 2: Interactive Name Processor
```python
print("=== Name Processor ===")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Process the names
full_name = first_name + " " + last_name
initials = first_name[0].upper() + last_name[0].upper()

print(f"\nProcessed Information:")
print(f"Full name: {full_name.title()}")
print(f"Initials: {initials}")
print(f"Username suggestion: {first_name.lower()}{len(last_name)}")
print(f"Name length: {len(full_name)} characters")
```

### Example 3: String Slicing
```python
message = "Hello, World!"

print("Full string:", message)
print("First 5 characters:", message[:5])
print("Last 6 characters:", message[-6:])
print("Every other character:", message[::2])
print("Reversed:", message[::-1])
print("Characters 2-8:", message[2:8])
```

### Example 4: User Input with Validation
```python
print("=== Age Calculator ===")

name = input("What's your name? ").strip().title()
birth_year = input("What year were you born? ")

# Convert and calculate
try:
    birth_year = int(birth_year)
    current_year = 2024
    age = current_year - birth_year
    
    print(f"\nHello {name}!")
    print(f"You are approximately {age} years old.")
    
    if age < 18:
        print("You're still a minor.")
    elif age < 65:
        print("You're an adult.")
    else:
        print("You're a senior citizen.")
        
except ValueError:
    print("Please enter a valid year next time!")
```

## 🏋️ Practice Exercises

### Exercise 1: Text Analyzer
```python
# Get a sentence from the user
# Display:
# - Number of characters
# - Number of words
# - Number of vowels
# - Text in all caps
# - Text in all lowercase
# - First and last word
```

### Exercise 2: Mad Libs Generator
```python
# Ask user for:
# - A noun
# - A verb
# - An adjective
# - A place
# - A number

# Create a funny story using their inputs
# Example: "The [adjective] [noun] [verb] to [place] [number] times!"
```

### Exercise 3: Email Validator
```python
# Get an email address from user
# Check if it:
# - Contains exactly one @ symbol
# - Has text before and after @
# - Ends with .com, .org, .edu, or .net
# - Display validation results
```

### Exercise 4: Password Strength Checker
```python
# Get a password from user
# Check and report:
# - Length (should be 8+ characters)
# - Contains uppercase letters
# - Contains lowercase letters  
# - Contains numbers
# - Contains special characters
# - Give overall strength rating
```

### Exercise 5: Name Formatter
```python
# Get a full name from user (could be messy format)
# Clean it up:
# - Remove extra spaces
# - Proper capitalization
# - Extract first, middle, last names
# - Create formal version: "Last, First M."
```

### Challenge: Text Adventure Setup
```python
# Create character creation for a text adventure:
# - Get player name
# - Choose character class (warrior, mage, archer)
# - Allocate skill points
# - Generate character description
# - Save character info in formatted strings
```

## 💡 String Method Reference

### Case Conversion
```python
text = "Hello World"
text.upper()        # HELLO WORLD
text.lower()        # hello world
text.title()        # Hello World
text.capitalize()   # Hello world
text.swapcase()     # hELLO wORLD
```

### Searching & Checking
```python
text = "Python Programming"
text.find("gram")         # Returns index or -1
text.count("m")           # Count occurrences
text.startswith("Py")     # True/False
text.endswith("ing")      # True/False
text.isdigit()           # True if all digits
text.isalpha()           # True if all letters
```

### Cleaning & Splitting
```python
text = "  Hello, World!  "
text.strip()             # Remove whitespace
text.replace("!", "?")   # Replace characters
text.split(",")          # Split into list
"_".join(["a", "b"])     # Join list with separator
```

## ✅ Self-Check Questions

1. How do you get input from a user in Python?
2. What's the difference between `+` and `f""` for string formatting?
3. How do you make text uppercase/lowercase?
4. What does `strip()` do to a string?
5. How do you check if a string contains another string?
6. What happens when you use `int()` on invalid input?

## 🛠️ Common Pitfalls

**Pitfall 1: Forgetting input() returns strings**
```python
# Wrong - will concatenate, not add
age = input("Your age: ")
next_year = age + 1  # Error!

# Right
age = int(input("Your age: "))
next_year = age + 1
```

**Pitfall 2: Not handling empty input**
```python
# Better to check for empty input
name = input("Name: ").strip()
if not name:
    name = "Anonymous"
```

**Pitfall 3: Case sensitivity in comparisons**
```python
answer = input("Yes or no? ")
# Wrong - won't catch "YES", "Yes", etc.
if answer == "yes":
    
# Better
if answer.lower() == "yes":
```

## 🚀 Tomorrow's Preview

Day 4 covers numbers and math operations - you'll learn to perform calculations, work with different number types, and use Python's math capabilities!

**Test your understanding with `python -m pytest tests/test_day3.py -v`**