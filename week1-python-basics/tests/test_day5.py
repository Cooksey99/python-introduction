"""
Day 5 Tests: List Operations and Algorithms
===========================================

Tests for Day 5 concepts: list creation, manipulation, and algorithms.
"""

import pytest
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_list_creation():
    """Test basic list creation and initialization"""
    # Empty list
    empty = []
    assert len(empty) == 0
    assert empty == []
    
    # List with numbers
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert numbers[0] == 1
    assert numbers[-1] == 5
    
    # List with mixed types
    mixed = ["hello", 42, 3.14, True]
    assert len(mixed) == 4
    assert mixed[0] == "hello"
    assert mixed[1] == 42
    
    # List from range
    range_list = list(range(5))
    assert range_list == [0, 1, 2, 3, 4]
    
    # List with list()
    string_list = list("hello")
    assert string_list == ['h', 'e', 'l', 'l', 'o']

def test_list_indexing():
    """Test list indexing and slicing"""
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    
    # Positive indexing
    assert fruits[0] == "apple"
    assert fruits[2] == "cherry"
    assert fruits[4] == "elderberry"
    
    # Negative indexing
    assert fruits[-1] == "elderberry"
    assert fruits[-2] == "date"
    assert fruits[-5] == "apple"
    
    # Slicing
    assert fruits[1:4] == ["banana", "cherry", "date"]
    assert fruits[:3] == ["apple", "banana", "cherry"]
    assert fruits[2:] == ["cherry", "date", "elderberry"]
    assert fruits[:] == fruits  # Copy of the list
    
    # Step slicing
    assert fruits[::2] == ["apple", "cherry", "elderberry"]
    assert fruits[::-1] == ["elderberry", "date", "cherry", "banana", "apple"]

def test_list_methods():
    """Test list methods"""
    # append()
    numbers = [1, 2, 3]
    numbers.append(4)
    assert numbers == [1, 2, 3, 4]
    
    # insert()
    numbers.insert(1, 1.5)
    assert numbers == [1, 1.5, 2, 3, 4]
    
    # remove()
    numbers.remove(1.5)
    assert numbers == [1, 2, 3, 4]
    
    # pop()
    popped = numbers.pop()
    assert popped == 4
    assert numbers == [1, 2, 3]
    
    # pop with index
    popped = numbers.pop(1)
    assert popped == 2
    assert numbers == [1, 3]
    
    # extend()
    numbers.extend([4, 5, 6])
    assert numbers == [1, 3, 4, 5, 6]
    
    # clear()
    numbers.clear()
    assert numbers == []

def test_list_searching():
    """Test list searching methods"""
    colors = ["red", "green", "blue", "red", "yellow"]
    
    # index()
    assert colors.index("green") == 1
    assert colors.index("red") == 0  # First occurrence
    
    # count()
    assert colors.count("red") == 2
    assert colors.count("purple") == 0
    
    # in operator
    assert "blue" in colors
    assert "purple" not in colors

def test_list_sorting():
    """Test list sorting operations"""
    # sort() - modifies in place
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    numbers.sort()
    assert numbers == [1, 1, 2, 3, 4, 5, 6, 9]
    
    # sort() reverse
    numbers.sort(reverse=True)
    assert numbers == [9, 6, 5, 4, 3, 2, 1, 1]
    
    # sorted() - returns new list
    original = [3, 1, 4, 1, 5]
    sorted_list = sorted(original)
    assert original == [3, 1, 4, 1, 5]  # Original unchanged
    assert sorted_list == [1, 1, 3, 4, 5]
    
    # reverse()
    letters = ['a', 'b', 'c', 'd']
    letters.reverse()
    assert letters == ['d', 'c', 'b', 'a']

def test_list_operations():
    """Test list operations like concatenation and repetition"""
    # Concatenation
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    assert combined == [1, 2, 3, 4, 5, 6]
    
    # Repetition
    repeated = [1, 2] * 3
    assert repeated == [1, 2, 1, 2, 1, 2]
    
    # Length
    assert len([1, 2, 3, 4, 5]) == 5
    
    # Min/Max (for comparable elements)
    assert min([3, 1, 4, 1, 5]) == 1
    assert max([3, 1, 4, 1, 5]) == 5
    
    # Sum (for numeric lists)
    assert sum([1, 2, 3, 4, 5]) == 15

def test_list_comprehensions():
    """Test list comprehensions"""
    # Basic comprehension
    squares = [x**2 for x in range(5)]
    assert squares == [0, 1, 4, 9, 16]
    
    # With condition
    evens = [x for x in range(10) if x % 2 == 0]
    assert evens == [0, 2, 4, 6, 8]
    
    # With transformation and condition
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    assert even_squares == [0, 4, 16, 36, 64]
    
    # From string
    vowels = [char for char in "hello world" if char in "aeiou"]
    assert vowels == ['e', 'o', 'o']

def test_nested_lists():
    """Test 2D lists (nested lists)"""
    # Create 2D list
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Access elements
    assert matrix[0][0] == 1
    assert matrix[1][2] == 6
    assert matrix[2][1] == 8
    
    # Access rows
    assert matrix[0] == [1, 2, 3]
    assert matrix[2] == [7, 8, 9]
    
    # Modify elements
    matrix[1][1] = 99
    assert matrix[1][1] == 99
    
    # Calculate row sums
    row_sums = [sum(row) for row in matrix]
    assert row_sums[0] == 6  # 1+2+3
    assert row_sums[1] == 109  # 4+99+6

def test_list_algorithms():
    """Test common list algorithms"""
    
    # Linear search
    def linear_search(lst, target):
        for i, item in enumerate(lst):
            if item == target:
                return i
        return -1
    
    test_list = [10, 23, 45, 70, 11, 15]
    assert linear_search(test_list, 70) == 3
    assert linear_search(test_list, 99) == -1
    
    # Find maximum without max()
    def find_max(lst):
        if not lst:
            return None
        maximum = lst[0]
        for item in lst[1:]:
            if item > maximum:
                maximum = item
        return maximum
    
    assert find_max([3, 7, 2, 9, 1]) == 9
    assert find_max([-5, -10, -1]) == -1
    assert find_max([]) is None
    
    # Reverse without reverse()
    def reverse_list(lst):
        reversed_lst = []
        for i in range(len(lst) - 1, -1, -1):
            reversed_lst.append(lst[i])
        return reversed_lst
    
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([]) == []
    
    # Remove duplicates preserving order
    def remove_duplicates(lst):
        seen = []
        for item in lst:
            if item not in seen:
                seen.append(item)
        return seen
    
    assert remove_duplicates([1, 2, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1]) == [1]

def test_list_statistics():
    """Test statistical calculations with lists"""
    data = [10, 20, 30, 40, 50]
    
    # Mean
    mean = sum(data) / len(data)
    assert mean == 30.0
    
    # Median (odd length)
    sorted_data = sorted(data)
    median = sorted_data[len(sorted_data) // 2]
    assert median == 30
    
    # Median (even length)
    even_data = [10, 20, 30, 40]
    sorted_even = sorted(even_data)
    median_even = (sorted_even[len(sorted_even)//2 - 1] + sorted_even[len(sorted_even)//2]) / 2
    assert median_even == 25.0
    
    # Range
    data_range = max(data) - min(data)
    assert data_range == 40

def test_list_filtering():
    """Test list filtering operations"""
    numbers = list(range(1, 21))  # 1 to 20
    
    # Filter even numbers
    evens = [n for n in numbers if n % 2 == 0]
    assert evens == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    # Filter numbers divisible by 3
    div_by_3 = [n for n in numbers if n % 3 == 0]
    assert div_by_3 == [3, 6, 9, 12, 15, 18]
    
    # Filter numbers greater than 15
    greater_15 = [n for n in numbers if n > 15]
    assert greater_15 == [16, 17, 18, 19, 20]
    
    # Using filter() function
    evens_filter = list(filter(lambda x: x % 2 == 0, numbers))
    assert evens_filter == evens

def test_list_transformations():
    """Test list transformation operations"""
    numbers = [1, 2, 3, 4, 5]
    
    # Square all numbers
    squares = [n**2 for n in numbers]
    assert squares == [1, 4, 9, 16, 25]
    
    # Double all numbers
    doubled = [n * 2 for n in numbers]
    assert doubled == [2, 4, 6, 8, 10]
    
    # String conversion
    str_nums = [str(n) for n in numbers]
    assert str_nums == ['1', '2', '3', '4', '5']
    
    # Using map() function
    squares_map = list(map(lambda x: x**2, numbers))
    assert squares_map == squares

def test_word_lists():
    """Test operations with word lists"""
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    
    # Word count
    assert len(words) == 9
    
    # Unique words
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    assert len(unique_words) == 8  # "the" appears twice
    
    # Words starting with specific letter
    words_with_t = [word for word in words if word.startswith('t')]
    assert words_with_t == ['the', 'the']
    
    # Word lengths
    word_lengths = [len(word) for word in words]
    assert max(word_lengths) == 5  # "brown", "jumps", "quick"
    assert min(word_lengths) == 3  # "the", "fox", "dog"

def test_list_copying():
    """Test list copying behavior"""
    original = [1, 2, 3]
    
    # Shallow copy with copy()
    copy1 = original.copy()
    copy1.append(4)
    assert original == [1, 2, 3]  # Original unchanged
    assert copy1 == [1, 2, 3, 4]
    
    # Shallow copy with slicing
    copy2 = original[:]
    copy2[0] = 99
    assert original == [1, 2, 3]  # Original unchanged
    assert copy2 == [99, 2, 3]
    
    # Assignment (not a copy!)
    reference = original
    reference.append(5)
    assert original == [1, 2, 3, 5]  # Original changed!

def test_list_advanced_operations():
    """Test advanced list operations"""
    
    # Merge two sorted lists
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
    
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    merged = merge_sorted_lists(list1, list2)
    assert merged == [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Flatten nested list
    def flatten_list(nested):
        flat = []
        for item in nested:
            if isinstance(item, list):
                flat.extend(flatten_list(item))
            else:
                flat.append(item)
        return flat
    
    nested = [[1, 2], [3, [4, 5]], 6]
    flattened = flatten_list(nested)
    assert flattened == [1, 2, 3, 4, 5, 6]
    
    # Rotate list
    def rotate_list(lst, n):
        if not lst:
            return lst
        n = n % len(lst)
        return lst[n:] + lst[:n]
    
    original = [1, 2, 3, 4, 5]
    rotated = rotate_list(original, 2)
    assert rotated == [3, 4, 5, 1, 2]

def test_list_error_handling():
    """Test error handling with lists"""
    lst = [1, 2, 3]
    
    # Index errors
    with pytest.raises(IndexError):
        lst[10]
    
    with pytest.raises(IndexError):
        lst[-10]
    
    # Value errors
    with pytest.raises(ValueError):
        lst.index(99)  # Item not in list
    
    with pytest.raises(ValueError):
        lst.remove(99)  # Item not in list

def test_list_memory_efficiency():
    """Test list memory and performance considerations"""
    # List vs generator expression
    list_comp = [x**2 for x in range(1000)]
    assert len(list_comp) == 1000
    assert isinstance(list_comp, list)
    
    # Generator expression (more memory efficient for large datasets)
    gen_exp = (x**2 for x in range(1000))
    assert list(gen_exp)[:5] == [0, 1, 4, 9, 16]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])