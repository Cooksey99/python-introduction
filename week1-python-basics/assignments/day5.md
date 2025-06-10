# Day 5: Lists Basics

## 🎯 Learning Objectives

By the end of Day 5, you will be able to:
- Create and modify lists to store collections of data
- Access list elements using indexing and slicing
- Use list methods to add, remove, and modify elements
- Understand list mutability and common operations
- Iterate through lists and perform bulk operations
- Work with nested lists and multi-dimensional data

## 📚 Core Concepts

### Creating Lists
```python
# Empty list
empty_list = []

# List with initial values
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Alice", 25, True, 3.14]

# Using list() constructor
letters = list("hello")  # ['h', 'e', 'l', 'l', 'o']
range_list = list(range(5))  # [0, 1, 2, 3, 4]
```

### Accessing Elements
```python
fruits = ["apple", "banana", "orange", "grape"]

print(fruits[0])    # apple (first element)
print(fruits[-1])   # grape (last element)
print(fruits[1:3])  # ['banana', 'orange'] (slicing)
print(len(fruits))  # 4 (length)
```

### Modifying Lists
```python
fruits = ["apple", "banana", "orange"]

# Add elements
fruits.append("grape")          # Add to end
fruits.insert(1, "kiwi")        # Insert at index
fruits.extend(["mango", "berry"])  # Add multiple

# Remove elements
fruits.remove("banana")         # Remove by value
deleted = fruits.pop()          # Remove and return last
deleted = fruits.pop(0)         # Remove and return at index

# Modify elements
fruits[0] = "pineapple"        # Change by index
```

## 🔧 Hands-On Examples

### Example 1: Shopping List Manager
```python
print("=== Shopping List Manager ===")

shopping_list = []

while True:
    print("\nCurrent list:", shopping_list)
    print("1. Add item")
    print("2. Remove item") 
    print("3. View list")
    print("4. Clear list")
    print("5. Exit")
    
    choice = input("Choice (1-5): ")
    
    if choice == "1":
        item = input("Enter item: ").strip().title()
        if item and item not in shopping_list:
            shopping_list.append(item)
            print(f"Added '{item}' to list")
        elif item in shopping_list:
            print("Item already in list!")
            
    elif choice == "2":
        if shopping_list:
            print("Items:", ", ".join(shopping_list))
            item = input("Remove which item? ").strip().title()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}'")
            else:
                print("Item not found!")
        else:
            print("List is empty!")
            
    elif choice == "3":
        if shopping_list:
            print("\nShopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
        else:
            print("List is empty!")
            
    elif choice == "4":
        shopping_list.clear()
        print("List cleared!")
        
    elif choice == "5":
        print("Final list:", shopping_list)
        break
```

### Example 2: Grade Analyzer
```python
print("=== Grade Analyzer ===")

# Get grades from user
grades = []
while True:
    grade_input = input("Enter a grade (or 'done' to finish): ")
    if grade_input.lower() == 'done':
        break
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Grade must be between 0 and 100")
    except ValueError:
        print("Please enter a valid number")

if grades:
    # Calculate statistics
    total = sum(grades)
    average = total / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    # Count letter grades
    a_count = sum(1 for g in grades if g >= 90)
    b_count = sum(1 for g in grades if 80 <= g < 90)
    c_count = sum(1 for g in grades if 70 <= g < 80)
    d_count = sum(1 for g in grades if 60 <= g < 70)
    f_count = sum(1 for g in grades if g < 60)
    
    print(f"\n=== Grade Analysis ===")
    print(f"Grades: {grades}")
    print(f"Total grades: {len(grades)}")
    print(f"Average: {average:.1f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Range: {highest - lowest}")
    
    print(f"\nLetter Grade Distribution:")
    print(f"A (90-100): {a_count}")
    print(f"B (80-89): {b_count}")
    print(f"C (70-79): {c_count}")
    print(f"D (60-69): {d_count}")
    print(f"F (0-59): {f_count}")
```

### Example 3: List Operations Showcase
```python
# Demonstrate various list operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print("Original list:", numbers)
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# Sorting (creates new list)
print("Sorted (ascending):", sorted(numbers))
print("Sorted (descending):", sorted(numbers, reverse=True))

# In-place operations
numbers_copy = numbers.copy()
numbers_copy.sort()
print("After sort():", numbers_copy)

numbers_copy.reverse()
print("After reverse():", numbers_copy)

# Finding elements
print("Index of 4:", numbers.index(4))
print("Count of 1:", numbers.count(1))
print("Is 7 in list?", 7 in numbers)

# List comprehensions (preview)
doubled = [x * 2 for x in numbers]
print("Doubled:", doubled)

evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)
```

### Example 4: 2D Lists (Lists of Lists)
```python
print("=== Tic Tac Toe Board ===")

# Create 3x3 board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board(board):
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(f"{i} {row[0]} | {row[1]} | {row[2]}")
        if i < 2:
            print("  ---------")

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

# Game simulation
current_player = "X"
moves = 0

print_board(board)

while moves < 9:
    try:
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter col (0-2): "))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if make_move(board, row, col, current_player):
                moves += 1
                print_board(board)
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That space is taken!")
        else:
            print("Invalid position!")
            
    except ValueError:
        print("Please enter valid numbers!")
    
    # Simple check for 3 in a row (basic version)
    if moves >= 5:  # Minimum moves for a win
        print("Game could be won - implement win checking!")
        break
```

## 🏋️ Practice Exercises

### Exercise 1: List Statistics
```python
# Create a program that:
# 1. Gets a list of numbers from user input
# 2. Calculates: mean, median, mode, range
# 3. Shows numbers above/below average
# 4. Displays results in a formatted report
```

### Exercise 2: Todo List App
```python
# Build a simple todo list with these features:
# - Add tasks with priority levels (high, medium, low)
# - Mark tasks as complete
# - View tasks by priority
# - Remove completed tasks
# - Show completion statistics
```

### Exercise 3: Word Games
```python
# Create programs for:
# 1. Word frequency counter (count each word in a sentence)
# 2. Anagram checker (check if two words use same letters)
# 3. Word sorter (sort words by length, alphabetically)
# 4. Palindrome list finder (find palindromes in word list)
```

### Exercise 4: Matrix Operations
```python
# Work with 2D lists (matrices):
# 1. Create a matrix addition function
# 2. Matrix multiplication (if you know the math)
# 3. Find sum of each row and column
# 4. Transpose a matrix (swap rows and columns)
```

### Exercise 5: Data Analysis
```python
# Analyze a dataset (list of dictionaries):
sales_data = [
    {"product": "Laptop", "price": 999, "quantity": 5},
    {"product": "Phone", "price": 599, "quantity": 12},
    {"product": "Tablet", "price": 399, "quantity": 8}
]

# Calculate:
# - Total revenue
# - Average price
# - Best selling product
# - Inventory value
```

### Challenge: Advanced List Algorithms
```python
# Implement these algorithms:
# 1. Binary search (find element in sorted list)
# 2. Bubble sort (sort list using bubble sort algorithm)
# 3. Find duplicate elements efficiently
# 4. Merge two sorted lists into one sorted list
```

## 💡 List Methods Reference

### Adding Elements
```python
lst = [1, 2, 3]
lst.append(4)           # [1, 2, 3, 4]
lst.insert(0, 0)        # [0, 1, 2, 3, 4]  
lst.extend([5, 6])      # [0, 1, 2, 3, 4, 5, 6]
```

### Removing Elements
```python
lst = [1, 2, 3, 2, 4]
lst.remove(2)           # [1, 3, 2, 4] (removes first 2)
last = lst.pop()        # Returns 4, lst = [1, 3, 2]
first = lst.pop(0)      # Returns 1, lst = [3, 2]
lst.clear()             # lst = []
```

### Searching & Counting
```python
lst = [1, 2, 3, 2, 4]
lst.index(2)            # 1 (first occurrence)
lst.count(2)            # 2 (appears twice)
2 in lst                # True
```

### Organizing
```python
lst = [3, 1, 4, 1, 5]
lst.sort()              # [1, 1, 3, 4, 5] (in-place)
lst.reverse()           # [5, 4, 3, 1, 1] (in-place)
new_lst = sorted(lst)   # Creates new sorted list
```

## ✅ Self-Check Questions

1. How do you add an element to the end of a list?
2. What's the difference between `append()` and `extend()`?
3. How do you access the last element of a list?
4. What does `list.pop()` return?
5. How do you check if an element exists in a list?
6. What's the difference between `sort()` and `sorted()`?

## 🛠️ Common Mistakes

**Mistake 1: Index out of range**
```python
lst = [1, 2, 3]
# print(lst[3])  # IndexError!

# Better
if len(lst) > 3:
    print(lst[3])
```

**Mistake 2: Modifying list while iterating**
```python
lst = [1, 2, 3, 4, 5]
# Wrong way
for item in lst:
    if item % 2 == 0:
        lst.remove(item)  # Can skip elements!

# Right way
lst = [item for item in lst if item % 2 != 0]
```

**Mistake 3: Shallow vs deep copy**
```python
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999
print(original)  # [[999, 2], [3, 4]] - original changed!

# For nested lists, use deep copy
import copy
deep = copy.deepcopy(original)
```

## 🚀 Tomorrow's Preview

Day 6 covers dictionaries - you'll learn to work with key-value pairs, creating more sophisticated data structures for real-world applications!

**Test your understanding with `python -m pytest tests/test_day5.py -v`**