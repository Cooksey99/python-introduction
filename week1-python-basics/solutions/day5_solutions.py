"""
Day 5 Solutions: Lists Basics
============================

Complete solutions for list creation, manipulation, and algorithms.
"""

import random

print("=== Day 5 Solutions: Lists ===")
print()

# Exercise 1: List Creation and Basic Operations
print("Exercise 1: List Basics")
# Create different types of lists
movies = ["The Matrix", "Inception", "Interstellar", "The Prestige", "Memento"]
numbers = list(range(1, 11))  # Numbers 1 through 10
mixed_list = ["Python", 42, 3.14, True, None]
empty_list = []

# Print each list with descriptive labels
print("Favorite Movies:", movies)
print("Numbers 1-10:", numbers)
print("Mixed Types:", mixed_list)
print("Empty List:", empty_list)

# Print the length of each list
print("\nList Lengths:")
print(f"Movies: {len(movies)} items")
print(f"Numbers: {len(numbers)} items")
print(f"Mixed: {len(mixed_list)} items")
print(f"Empty: {len(empty_list)} items")

# Print first and last elements (handle empty list)
print("\nFirst and Last Elements:")
if movies:
    print(f"Movies - First: {movies[0]}, Last: {movies[-1]}")
if numbers:
    print(f"Numbers - First: {numbers[0]}, Last: {numbers[-1]}")
if mixed_list:
    print(f"Mixed - First: {mixed_list[0]}, Last: {mixed_list[-1]}")
if empty_list:
    print(f"Empty - First: {empty_list[0]}, Last: {empty_list[-1]}")
else:
    print("Empty list has no elements")

print()

# Exercise 2: Shopping List Manager
print("Exercise 2: Shopping List Manager")
shopping_list = []

# Simulate shopping list operations
print("Shopping List Manager Demo")

# Add items
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")
print(f"Added items. List: {shopping_list}")

# Check if item exists
item_to_check = "Bread"
if item_to_check in shopping_list:
    print(f"{item_to_check} is in the shopping list")

# Remove item
shopping_list.remove("Bread")
print(f"Removed Bread. List: {shopping_list}")

# Add more items
shopping_list.extend(["Apples", "Bananas", "Cheese"])
print(f"Added more items. List: {shopping_list}")

# Clear list
shopping_list.clear()
print(f"Cleared list. List: {shopping_list}")

print()

# Exercise 3: Grade Analyzer
print("Exercise 3: Grade Analyzer")
grades = [85, 92, 78, 95, 88, 73, 91, 82, 87, 90]
print("Grades:", grades)

# Calculate statistics
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

# Count letter grades
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for grade in grades:
    if grade >= 90:
        grade_counts["A"] += 1
    elif grade >= 80:
        grade_counts["B"] += 1
    elif grade >= 70:
        grade_counts["C"] += 1
    elif grade >= 60:
        grade_counts["D"] += 1
    else:
        grade_counts["F"] += 1

# Display results
print(f"Average Grade: {average:.2f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
print("Grade Distribution:")
for letter, count in grade_counts.items():
    print(f"  {letter}'s: {count}")

# Sorted grades
print("Sorted (ascending):", sorted(grades))
print("Sorted (descending):", sorted(grades, reverse=True))

print()

# Exercise 4: List Methods Practice
print("Exercise 4: List Methods")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print("Original list:", numbers.copy())  # Use copy to preserve original

# Demonstrate all methods
numbers.append(7)
print(f"After append(7): {numbers}")

numbers.insert(2, 8)
print(f"After insert(2, 8): {numbers}")

numbers.remove(1)  # Removes first occurrence
print(f"After remove(1): {numbers}")

popped = numbers.pop(4)
print(f"After pop(4), removed {popped}: {numbers}")

index_of_5 = numbers.index(5)
print(f"Index of 5: {index_of_5}")

count_of_3 = numbers.count(3)
print(f"Count of 3: {count_of_3}")

# Sort and reverse (modifies in place)
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"After sort(): {numbers_copy}")

numbers_copy.reverse()
print(f"After reverse(): {numbers_copy}")

print()

# Exercise 5: Number List Operations
print("Exercise 5: Number Operations")
numbers = [random.randint(1, 100) for _ in range(10)]
print("Random numbers:", numbers)

# Basic statistics
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}")
print(f"Average: {average:.2f}")

# Filter operations
even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 == 1]
divisible_by_3 = [n for n in numbers if n % 3 == 0]
greater_than_50 = [n for n in numbers if n > 50]

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print(f"Divisible by 3: {divisible_by_3}")
print(f"Greater than 50: {greater_than_50}")

# Transformations
doubled = [n * 2 for n in numbers]
print(f"Doubled values: {doubled}")

# Second largest
sorted_numbers = sorted(numbers)
if len(sorted_numbers) >= 2:
    second_largest = sorted_numbers[-2]
    print(f"Second largest: {second_largest}")

print()

# Exercise 6: 2D Lists (Matrix)
print("Exercise 6: 2D Lists")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Display matrix nicely
print("Matrix:")
for row in matrix:
    print(" ".join(f"{val:3}" for val in row))

# Row sums
print("\nRow sums:")
for i, row in enumerate(matrix):
    print(f"Row {i}: {sum(row)}")

# Column sums
print("\nColumn sums:")
for col in range(len(matrix[0])):
    col_sum = sum(matrix[row][col] for row in range(len(matrix)))
    print(f"Column {col}: {col_sum}")

# Diagonal sums
main_diagonal = sum(matrix[i][i] for i in range(len(matrix)))
anti_diagonal = sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))
print(f"\nMain diagonal sum: {main_diagonal}")
print(f"Anti-diagonal sum: {anti_diagonal}")

print()

# Exercise 7: Word List Processing
print("Exercise 7: Word Processing")
sentence = "The quick brown fox jumps over the lazy dog and the cat"
words = sentence.lower().split()
print(f"Sentence: {sentence}")
print(f"Words: {words}")

# Analysis
print(f"\nTotal words: {len(words)}")

# Find longest and shortest
longest = max(words, key=len)
shortest = min(words, key=len)
print(f"Longest word: '{longest}' ({len(longest)} chars)")
print(f"Shortest word: '{shortest}' ({len(shortest)} chars)")

# Count words by length
length_counts = {}
for word in words:
    length = len(word)
    length_counts[length] = length_counts.get(length, 0) + 1

print("\nWord lengths:")
for length in sorted(length_counts.keys()):
    print(f"  {length} chars: {length_counts[length]} words")

# Remove duplicates while preserving order
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
print(f"\nUnique words ({len(unique_words)}): {unique_words}")

# Sort alphabetically
sorted_words = sorted(unique_words)
print(f"Alphabetically: {sorted_words}")

# Words starting with vowels
vowels = 'aeiou'
vowel_words = [word for word in unique_words if word[0] in vowels]
print(f"Starting with vowels: {vowel_words}")

print()

# Exercise 8: List Algorithms
print("Exercise 8: List Algorithms")
test_list = [64, 34, 25, 12, 22, 11, 90]
print("Test list:", test_list)

# 1. Linear search
def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1

print(f"Linear search for 22: index {linear_search(test_list, 22)}")
print(f"Linear search for 99: index {linear_search(test_list, 99)}")

# 2. Find maximum without using max()
def find_max(lst):
    if not lst:
        return None
    maximum = lst[0]
    for item in lst[1:]:
        if item > maximum:
            maximum = item
    return maximum

print(f"Maximum value: {find_max(test_list)}")

# 3. Reverse list without using reverse()
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(f"Reversed: {reverse_list(test_list)}")

# 4. Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

dup_list = [1, 2, 2, 3, 4, 3, 5]
print(f"Remove duplicates from {dup_list}: {remove_duplicates(dup_list)}")

# 5. Merge two sorted lists
def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    
    return merged

sorted1 = [1, 3, 5, 7]
sorted2 = [2, 4, 6, 8]
print(f"Merge {sorted1} and {sorted2}: {merge_sorted_lists(sorted1, sorted2)}")

print()

# Challenge: Advanced List Operations
print("Challenge: Advanced Operations")

# 1. Flatten nested list
def flatten_list(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested = [[1, 2], [3, [4, 5]], 6, [7, 8, 9]]
print(f"Flatten {nested}: {flatten_list(nested)}")

# 2. Group by even/odd
def group_by_even_odd(numbers):
    groups = {"even": [], "odd": []}
    for num in numbers:
        if num % 2 == 0:
            groups["even"].append(num)
        else:
            groups["odd"].append(num)
    return groups

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Group {nums}: {group_by_even_odd(nums)}")

# 3. Rotate list
def rotate_list(lst, n):
    if not lst:
        return lst
    n = n % len(lst)  # Handle n > len(lst)
    return lst[n:] + lst[:n]

original = [1, 2, 3, 4, 5]
print(f"Rotate {original} by 2: {rotate_list(original, 2)}")

print()
print("=== Day 5 Solutions Complete! ===")

"""
Teaching Notes for Mentors:
===========================

Key Concepts Demonstrated:
1. List creation and initialization
2. List indexing and slicing
3. List methods (append, insert, remove, pop, etc.)
4. List comprehensions
5. Nested lists (2D arrays)
6. Common list algorithms
7. List sorting and filtering

Important List Concepts:
- Lists are mutable (can be changed)
- Zero-based indexing
- Negative indexing for accessing from end
- Slicing creates new lists
- List methods modify in-place vs return new lists
- List comprehensions for concise operations

Common Challenges:
1. Index out of range errors
2. Modifying lists while iterating
3. Understanding mutable vs immutable
4. List reference vs copy
5. Nested list operations

Real-World Applications:
- Shopping carts
- Grade tracking systems
- Data analysis
- Game boards (2D lists)
- Queue/stack implementations
- Sorting and searching algorithms

Code Quality Features:
- Proper error handling for empty lists
- Clear variable names
- Efficient algorithms
- Good use of list comprehensions
- Proper documentation
"""