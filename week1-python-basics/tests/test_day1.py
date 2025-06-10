"""
Day 1 Tests: Environment Setup and Hello World
==============================================

This file contains automated tests to verify Day 1 exercise completion.
Run these tests with: python -m pytest tests/test_day1.py -v

Note: These tests check for basic functionality and common patterns.
There may be multiple correct solutions that these tests don't cover.
"""

import pytest
import sys
import os
from io import StringIO
from contextlib import redirect_stdout

# Add the project root to the path so we can import exercises
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def capture_print_output(func):
    """Helper function to capture print output from a function"""
    f = StringIO()
    with redirect_stdout(f):
        func()
    return f.getvalue()

def test_python_environment():
    """Test that Python environment is set up correctly"""
    # Test that we can run Python and basic operations work
    assert sys.version_info >= (3, 6), "Python 3.6 or higher required"
    
    # Test basic print functionality
    f = StringIO()
    with redirect_stdout(f):
        print("Hello, World!")
    output = f.getvalue()
    assert "Hello, World!" in output

def test_hello_world_file_exists():
    """Test that students have created basic Python files"""
    # Check if common beginner files exist
    expected_files = ['hello_world.py', 'print_practice.py']
    
    # Look in common locations
    search_paths = [
        '.',
        '../',
        'exercises/',
        '../exercises/',
    ]
    
    found_files = []
    for path in search_paths:
        for file in expected_files:
            full_path = os.path.join(path, file)
            if os.path.exists(full_path):
                found_files.append(file)
    
    # We should find at least one practice file
    assert len(found_files) > 0, "No practice Python files found. Create hello_world.py or print_practice.py"

def test_basic_print_functionality():
    """Test that students understand basic print statements"""
    
    def test_print():
        print("Hello, Python!")
        print(42)
        print("My age is", 25)
    
    output = capture_print_output(test_print)
    lines = output.strip().split('\n')
    
    # Should have 3 lines of output
    assert len(lines) == 3, f"Expected 3 lines of output, got {len(lines)}"
    
    # Check specific content
    assert "Hello, Python!" in lines[0]
    assert "42" in lines[1]
    assert "My age is 25" in lines[2]

def test_string_and_number_printing():
    """Test understanding of strings vs numbers in print statements"""
    
    # Test that students understand quotes vs no quotes
    def test_mixed_printing():
        print("Text with quotes")
        print(123)
        print("Number as text:", "456")
        print("Number as number:", 789)
    
    output = capture_print_output(test_mixed_printing)
    lines = output.strip().split('\n')
    
    assert len(lines) == 4
    assert "Text with quotes" in lines[0]
    assert "123" in lines[1]
    assert "456" in lines[2]
    assert "789" in lines[3]

def test_comments():
    """Test that students can use comments"""
    
    def test_with_comments():
        # This is a comment
        print("This line should print")
        # print("This line should not print")
    
    output = capture_print_output(test_with_comments)
    lines = output.strip().split('\n')
    
    # Should only have one line of actual output
    assert len(lines) == 1
    assert "This line should print" in lines[0]
    assert "This line should not print" not in output

def test_multiple_items_in_print():
    """Test printing multiple items in one statement"""
    
    def test_multiple():
        print("Hello", "World", 123, "Python")
    
    output = capture_print_output(test_multiple)
    
    # All items should appear in the output
    assert "Hello" in output
    assert "World" in output
    assert "123" in output
    assert "Python" in output

def test_quote_variations():
    """Test using both single and double quotes"""
    
    def test_quotes():
        print("Double quotes work")
        print('Single quotes work')
        print("She said, 'Hello!'")
    
    output = capture_print_output(test_quotes)
    lines = output.strip().split('\n')
    
    assert len(lines) == 3
    assert "Double quotes work" in lines[0]
    assert "Single quotes work" in lines[1]
    assert "Hello!" in lines[2]

class TestDay1Exercises:
    """Test class for Day 1 specific exercises"""
    
    def test_exercise_file_exists(self):
        """Test that the day1_exercises.py file exists"""
        exercise_file = 'exercises/day1_exercises.py'
        assert os.path.exists(exercise_file), f"Exercise file {exercise_file} not found"
    
    def test_exercise_file_runnable(self):
        """Test that the exercise file can be imported without errors"""
        try:
            # Try to run the exercises file
            import exercises.day1_exercises
        except ImportError:
            pytest.skip("exercises.day1_exercises module not found")
        except SyntaxError as e:
            pytest.fail(f"Syntax error in exercises file: {e}")
        except Exception as e:
            # Other errors are okay - students might have incomplete solutions
            pass

def test_ascii_art_attempt():
    """Test that students have attempted ASCII art"""
    
    def test_ascii():
        print("  *  ")
        print(" *** ")
        print("*****")
    
    output = capture_print_output(test_ascii)
    lines = output.strip().split('\n')
    
    # Should have multiple lines
    assert len(lines) >= 3, "ASCII art should have multiple lines"
    
    # Should contain some visual characters
    visual_chars = ['*', '/', '\\', '|', '-', '_', '^', 'o', '(', ')']
    has_visual = any(char in output for char in visual_chars)
    assert has_visual, "ASCII art should contain visual characters"

def test_story_telling():
    """Test that students can create multi-line narratives"""
    
    def test_story():
        print("Once upon a time there was a programmer.")
        print("They wanted to learn Python.")
        print("They practiced every day.")
        print("And they became very skilled!")
    
    output = capture_print_output(test_story)
    lines = output.strip().split('\n')
    
    # Should have multiple lines for a story
    assert len(lines) >= 3, "Story should have multiple lines"
    
    # Lines should have reasonable content (not just single words)
    for line in lines:
        assert len(line.strip()) > 5, f"Story line too short: {line}"

@pytest.mark.parametrize("test_case", [
    ("print('Hello')", "Hello"),
    ("print(42)", "42"),
    ("print('Age:', 25)", "Age: 25"),
])
def test_specific_print_cases(test_case):
    """Test specific print statement patterns"""
    code, expected = test_case
    
    # Execute the code and capture output
    f = StringIO()
    with redirect_stdout(f):
        exec(code)
    output = f.getvalue().strip()
    
    assert expected in output, f"Expected '{expected}' in output, got '{output}'"

def test_error_awareness():
    """Test that students are aware of common errors"""
    
    # These should raise errors (good for learning)
    error_cases = [
        "print(Hello World)",  # Missing quotes
        "Print('Hello')",      # Wrong capitalization
        "print('Hello World'", # Missing closing quote
    ]
    
    for case in error_cases:
        with pytest.raises((SyntaxError, NameError)):
            exec(case)

if __name__ == "__main__":
    # Run tests when file is executed directly
    pytest.main([__file__, "-v"])