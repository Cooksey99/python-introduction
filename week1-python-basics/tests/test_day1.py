"""
Day 1 Tests: Environment Setup and Hello World
==============================================

Tests for Day 1 exercise functions.
Run these tests with: python -m pytest tests/test_day1.py -v
"""

import pytest
import sys
import os

# Add the project root to the path so we can import exercises
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import the exercise functions
try:
    from exercises.day1_exercises import (
        exercise_1, exercise_2, exercise_3, exercise_4,
        exercise_5, exercise_6, exercise_7, exercise_8
    )
except ImportError as e:
    pytest.fail(f"Could not import exercise functions: {e}")

def test_exercise_1():
    """Test that exercise_1 returns 'Hello, Python!'"""
    result = exercise_1()
    assert result == "Hello, Python!", f"Expected 'Hello, Python!', got {repr(result)}"

def test_exercise_2():
    """Test that exercise_2 returns a list with name, age, and hobby"""
    result = exercise_2()
    assert isinstance(result, list), f"Expected a list, got {type(result)}"
    assert len(result) == 3, f"Expected list of length 3, got {len(result)}"
    
    # All items should be strings
    for i, item in enumerate(result):
        assert isinstance(item, str), f"Item {i} should be a string, got {type(item)}"
    
    # Basic validation - name and hobby should be non-empty
    assert len(result[0]) > 0, "Name (first item) should not be empty"
    assert len(result[2]) > 0, "Hobby (third item) should not be empty"

def test_exercise_3():
    """Test that exercise_3 returns a tuple with number and sentence"""
    result = exercise_3()
    assert isinstance(result, tuple), f"Expected a tuple, got {type(result)}"
    assert len(result) == 2, f"Expected tuple of length 2, got {len(result)}"
    
    number, sentence = result
    assert isinstance(number, int), f"First item should be an integer, got {type(number)}"
    assert isinstance(sentence, str), f"Second item should be a string, got {type(sentence)}"
    assert str(number) in sentence, f"The sentence should contain the number {number}"

def test_exercise_4():
    """Test that exercise_4 returns a sentence with text and numbers"""
    result = exercise_4()
    assert isinstance(result, str), f"Expected a string, got {type(result)}"
    assert len(result) > 0, "Result should not be empty"
    
    # Should contain at least one digit
    assert any(char.isdigit() for char in result), "Sentence should contain at least one number"

def test_exercise_5():
    """Test that exercise_5 returns ASCII art with at least 3 lines"""
    result = exercise_5()
    assert isinstance(result, str), f"Expected a string, got {type(result)}"
    
    lines = result.split('\n')
    assert len(lines) >= 3, f"ASCII art should have at least 3 lines, got {len(lines)}"
    
    # Should have some visual characters
    visual_chars = ['*', '/', '\\', '|', '-', '_', '^', 'o', '(', ')']
    has_visual = any(char in result for char in visual_chars)
    assert has_visual, "ASCII art should contain visual characters"

def test_exercise_6():
    """Test that exercise_6 returns a 4-line story"""
    result = exercise_6()
    assert isinstance(result, str), f"Expected a string, got {type(result)}"
    
    lines = result.split('\n')
    assert len(lines) == 4, f"Story should have exactly 4 lines, got {len(lines)}"
    
    # Each line should have reasonable content
    for i, line in enumerate(lines):
        assert len(line.strip()) > 0, f"Line {i+1} should not be empty"

def test_exercise_7():
    """Test that exercise_7 returns a list of strings with different quote usage"""
    result = exercise_7()
    assert isinstance(result, list), f"Expected a list, got {type(result)}"
    assert len(result) == 3, f"Expected list of length 3, got {len(result)}"
    
    # All items should be strings
    for i, item in enumerate(result):
        assert isinstance(item, str), f"Item {i} should be a string, got {type(item)}"
        assert len(item) > 0, f"String {i} should not be empty"
    
    # Third string should demonstrate mixed quote usage (contain single quotes in content)
    # Example: "She said 'Hello!' to me" uses double quotes to wrap content with single quotes
    mixed_quotes_string = result[2]
    assert "'" in mixed_quotes_string, \
        "Third string should contain single quotes to demonstrate mixed quote usage"

def test_exercise_8():
    """Test that exercise_8 returns a helpful comment"""
    result = exercise_8()
    assert isinstance(result, str), f"Expected a string, got {type(result)}"
    assert len(result) > 10, "Comment should be descriptive (more than 10 characters)"
    
    # Should be a reasonable comment about printing
    result_lower = result.lower()
    print_related = any(word in result_lower for word in ['print', 'display', 'output', 'show', 'console'])
    assert print_related, "Comment should be related to printing/displaying output"

def test_all_functions_implemented():
    """Test that all functions are implemented (don't just return None)"""
    functions = [exercise_1, exercise_2, exercise_3, exercise_4, 
                exercise_5, exercise_6, exercise_7, exercise_8]
    
    for i, func in enumerate(functions, 1):
        result = func()
        assert result is not None, f"Exercise {i} is not implemented (returns None)"

def test_no_syntax_errors():
    """Test that all exercise functions can be called without syntax errors"""
    functions = [exercise_1, exercise_2, exercise_3, exercise_4, 
                exercise_5, exercise_6, exercise_7, exercise_8]
    
    for i, func in enumerate(functions, 1):
        try:
            func()
        except Exception as e:
            # Allow NotImplementedError or functions that return None
            if not isinstance(e, NotImplementedError):
                pytest.fail(f"Exercise {i} has an error: {e}")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])