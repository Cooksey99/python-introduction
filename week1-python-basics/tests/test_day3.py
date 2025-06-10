"""
Day 3 Tests: String Operations and User Input
=============================================

Tests for Day 3 concepts: string manipulation, formatting, and text processing.
"""

import pytest
import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_string_methods():
    """Test basic string methods"""
    text = "  Python Programming  "
    
    assert text.strip() == "Python Programming"
    assert text.upper() == "  PYTHON PROGRAMMING  "
    assert text.lower() == "  python programming  "
    assert text.title() == "  Python Programming  "
    assert text.replace("Python", "Java") == "  Java Programming  "

def test_string_properties():
    """Test string properties and checks"""
    text = "Hello World"
    
    assert len(text) == 11
    assert text.count("l") == 3
    assert text.startswith("Hello")
    assert text.endswith("World")
    assert "World" in text
    assert "Python" not in text

def test_string_slicing():
    """Test string slicing operations"""
    word = "PROGRAMMING"
    
    assert word[:4] == "PROG"
    assert word[-4:] == "MING"
    assert word[::2] == "PORMIG"
    assert word[::-1] == "GNIMMARGORP"
    assert word[3:7] == "GRAM"

def test_string_formatting():
    """Test string formatting methods"""
    name = "Alice"
    age = 25
    
    # f-string formatting
    formatted = f"Hello {name}, you are {age}"
    assert formatted == "Hello Alice, you are 25"
    
    # .format() method
    formatted2 = "Hello {}, you are {}".format(name, age)
    assert formatted2 == "Hello Alice, you are 25"
    
    # String concatenation
    formatted3 = "Hello " + name + ", you are " + str(age)
    assert formatted3 == "Hello Alice, you are 25"

def test_text_analysis():
    """Test text analysis functions"""
    text = "The quick brown fox"
    
    # Word count
    words = text.split()
    assert len(words) == 4
    
    # Character count
    assert len(text) == 19
    assert len(text.replace(" ", "")) == 16  # Without spaces
    
    # Vowel count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    assert vowel_count == 5  # e, u, i, o, o

def test_name_formatting():
    """Test name cleaning and formatting"""
    messy_name = "  john    SMITH  "
    
    # Clean and format
    cleaned = messy_name.strip()
    parts = cleaned.split()
    formatted_parts = [part.title() for part in parts]
    clean_name = " ".join(formatted_parts)
    
    assert clean_name == "John Smith"
    
    # Create initials
    initials = "".join([part[0] for part in formatted_parts])
    assert initials == "JS"

def test_email_validation():
    """Test email validation logic"""
    
    def validate_email(email):
        has_single_at = email.count("@") == 1
        if not has_single_at:
            return False
            
        parts = email.split("@")
        has_text_before = len(parts[0]) > 0
        has_text_after = len(parts[1]) > 0
        
        valid_domains = [".com", ".org", ".edu", ".net"]
        has_valid_domain = any(email.endswith(domain) for domain in valid_domains)
        no_spaces = " " not in email
        
        return all([has_text_before, has_text_after, has_valid_domain, no_spaces])
    
    assert validate_email("user@example.com") == True
    assert validate_email("invalid.email") == False
    assert validate_email("user@@domain.com") == False
    assert validate_email("user@domain") == False
    assert validate_email("user @domain.com") == False

def test_password_strength():
    """Test password strength checking"""
    
    def check_password_strength(password):
        min_length = len(password) >= 8
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*" for c in password)
        
        criteria_met = sum([min_length, has_upper, has_lower, has_digit, has_special])
        
        if criteria_met >= 5:
            return "Strong"
        elif criteria_met >= 3:
            return "Medium"
        else:
            return "Weak"
    
    assert check_password_strength("MyPass123!") == "Strong"
    assert check_password_strength("password") == "Weak"
    assert check_password_strength("Pass123") == "Medium"

def test_caesar_cipher():
    """Test Caesar cipher encryption/decryption"""
    
    def caesar_encrypt(text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += char
        return result
    
    def caesar_decrypt(text, shift):
        return caesar_encrypt(text, -shift)
    
    original = "HELLO"
    encrypted = caesar_encrypt(original, 3)
    assert encrypted == "KHOOR"
    
    decrypted = caesar_decrypt(encrypted, 3)
    assert decrypted == original

def test_string_case_conversion():
    """Test various case conversion methods"""
    text = "hello WORLD"
    
    assert text.upper() == "HELLO WORLD"
    assert text.lower() == "hello world"
    assert text.title() == "Hello World"
    assert text.capitalize() == "Hello world"
    assert text.swapcase() == "HELLO world"

def test_string_searching():
    """Test string searching and finding"""
    text = "Python is awesome and Python is fun"
    
    assert text.find("Python") == 0  # First occurrence
    assert text.find("Java") == -1   # Not found
    assert text.count("Python") == 2
    assert text.count("is") == 2

def test_string_splitting_joining():
    """Test string splitting and joining"""
    sentence = "apple,banana,cherry"
    
    # Split
    fruits = sentence.split(",")
    assert fruits == ["apple", "banana", "cherry"]
    
    # Join
    rejoined = " | ".join(fruits)
    assert rejoined == "apple | banana | cherry"

def test_string_validation_methods():
    """Test string validation methods"""
    assert "123".isdigit() == True
    assert "abc".isalpha() == True
    assert "abc123".isalnum() == True
    assert "   ".isspace() == True
    assert "Hello World".istitle() == True
    assert "HELLO".isupper() == True
    assert "hello".islower() == True

def test_word_frequency():
    """Test word frequency counting"""
    text = "the quick brown fox jumps over the lazy dog"
    words = text.split()
    
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    assert frequency["the"] == 2
    assert frequency["quick"] == 1
    assert len(frequency) == 8  # 8 unique words

def test_string_cleaning():
    """Test text cleaning operations"""
    dirty_text = "  Hello,   World!  \n\t"
    
    # Clean whitespace
    cleaned = dirty_text.strip()
    assert cleaned == "Hello,   World!"
    
    # Remove punctuation (simple version)
    import string
    no_punct = "".join(char for char in cleaned if char not in string.punctuation)
    assert no_punct == "Hello   World"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])