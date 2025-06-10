"""
Day 2 Tests: Variables and Data Types
====================================

Tests that verify students have completed Day 2 exercises about
variables, data types, and type conversion.
"""

import pytest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout
import re

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def get_exercise_file_content():
    """Helper function to read the exercise file"""
    exercise_file = 'exercises/day2_exercises.py'
    if not os.path.exists(exercise_file):
        pytest.fail(f"Exercise file {exercise_file} not found")
    
    try:
        with open(exercise_file, 'r') as f:
            return f.read()
    except Exception as e:
        pytest.fail(f"Could not read exercise file: {e}")

def capture_exercise_output():
    """Capture the output of running the exercise file"""
    f = StringIO()
    with redirect_stdout(f):
        try:
            exec(open('exercises/day2_exercises.py').read())
        except Exception as e:
            pytest.fail(f"Error running exercises: {e}")
    return f.getvalue()

def count_code_lines_in_section(content, exercise_num):
    """Count non-comment, non-empty lines of code in an exercise section"""
    # Look for the exercise section
    if exercise_num < 10:  # Single digit
        pattern = f'# Exercise {exercise_num}:.*?(?=# Exercise {exercise_num + 1}:|print\\(\\)|\\Z)'
    else:  # Handle last exercise or special cases
        pattern = f'# Exercise {exercise_num}:.*?(?=print\\(\\)|\\Z)'
    
    exercise_section = re.search(pattern, content, re.DOTALL)
    if not exercise_section:
        return 0
    
    section_content = exercise_section.group(0)
    
    lines_after_todo = []
    found_todo = False
    for line in section_content.split('\n'):
        if 'Your code here:' in line:
            found_todo = True
            continue
        if found_todo and line.strip() and not line.strip().startswith('#'):
            lines_after_todo.append(line.strip())
    
    return len(lines_after_todo)

def test_exercise_file_exists():
    """Test that the exercise file exists and is readable"""
    content = get_exercise_file_content()
    assert len(content) > 0, "Exercise file is empty"
    assert "Exercise 1" in content, "Exercise file doesn't contain expected exercises"

def test_exercise_1_completed():
    """Test that Exercise 1 is completed - personal information variables"""
    content = get_exercise_file_content()
    
    # Should have multiple variable assignments and print statements
    code_lines = count_code_lines_in_section(content, 1)
    assert code_lines >= 8, f"Exercise 1 not completed - expected at least 8 lines of code, found {code_lines}"
    
    # Check for specific variable names mentioned in the TODO
    assert "first_name" in content, "Exercise 1 missing - should create first_name variable"
    assert "last_name" in content, "Exercise 1 missing - should create last_name variable"
    assert "age" in content, "Exercise 1 missing - should create age variable"

def test_exercise_2_completed():
    """Test that Exercise 2 is completed - type checking"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 2)
    assert code_lines >= 6, f"Exercise 2 not completed - expected at least 6 lines of code, found {code_lines}"
    
    # Should use type() function
    assert "type(" in content, "Exercise 2 missing - should use type() function to check types"

def test_exercise_3_completed():
    """Test that Exercise 3 is completed - variable naming"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 3)
    assert code_lines >= 3, f"Exercise 3 not completed - expected at least 3 lines of code, found {code_lines}"

def test_exercise_4_completed():
    """Test that Exercise 4 is completed - numbers and math"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 4)
    assert code_lines >= 8, f"Exercise 4 not completed - expected at least 8 lines of code, found {code_lines}"

def test_exercise_5_completed():
    """Test that Exercise 5 is completed - type conversion"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 5)
    assert code_lines >= 6, f"Exercise 5 not completed - expected at least 6 lines of code, found {code_lines}"
    
    # Should have type conversion functions
    has_conversion = any(func in content for func in ['int(', 'float(', 'str(', 'bool('])
    assert has_conversion, "Exercise 5 missing - should include type conversion functions (int, float, str, bool)"

def test_exercise_6_completed():
    """Test that Exercise 6 is completed - string variables"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 6)
    assert code_lines >= 5, f"Exercise 6 not completed - expected at least 5 lines of code, found {code_lines}"

def test_exercise_7_completed():
    """Test that Exercise 7 is completed - boolean logic"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 7)
    assert code_lines >= 6, f"Exercise 7 not completed - expected at least 6 lines of code, found {code_lines}"
    
    # Should use boolean values
    has_boolean = any(val in content for val in ['True', 'False'])
    assert has_boolean, "Exercise 7 missing - should use boolean values (True/False)"

def test_exercise_8_completed():
    """Test that Exercise 8 is completed - multiple assignment"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 8)
    assert code_lines >= 4, f"Exercise 8 not completed - expected at least 4 lines of code, found {code_lines}"

def test_exercise_9_completed():
    """Test that Exercise 9 is completed - variable swapping"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 9)
    assert code_lines >= 3, f"Exercise 9 not completed - expected at least 3 lines of code, found {code_lines}"

def test_exercise_10_completed():
    """Test that Exercise 10 is completed - user profile"""
    content = get_exercise_file_content()
    
    code_lines = count_code_lines_in_section(content, 10)
    assert code_lines >= 8, f"Exercise 10 not completed - expected at least 8 lines of code, found {code_lines}"

def test_no_syntax_errors():
    """Test that the exercise file runs without syntax errors"""
    try:
        output = capture_exercise_output()
        assert len(output) > 0, "Exercise file produced no output - exercises may not be completed"
    except Exception as e:
        pytest.fail(f"Exercise file has errors: {e}")

def test_file_structure_intact():
    """Test that students haven't accidentally deleted important parts"""
    content = get_exercise_file_content()
    
    # Check that all exercise headers are still present
    for i in range(1, 11):
        assert f"Exercise {i}" in content, f"Exercise {i} header missing - file may be corrupted"
    
    # Check that TODO comments are still present
    assert "TODO" in content, "TODO comments removed - these should be kept for reference"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])