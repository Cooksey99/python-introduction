"""
Day 3 Solutions: String Operations and User Input
================================================

Complete solutions demonstrating string manipulation, user input handling,
and text processing techniques.
"""

print("=== Day 3 Solutions: Strings and User Input ===")
print()

# Exercise 1: String Methods Exploration
print("Exercise 1: String Methods")
sample_text = "  Python Programming is Amazing!  "
print("Original text:", repr(sample_text))

# Apply string methods
print("Stripped:", repr(sample_text.strip()))
print("Upper:", sample_text.upper())
print("Lower:", sample_text.lower())
print("Title:", sample_text.title())
print("Replace 'Amazing' with 'Fantastic':", sample_text.replace("Amazing", "Fantastic"))
print("Length:", len(sample_text))
print("Count 'a':", sample_text.count('a'))
print("Count 'A':", sample_text.count('A'))
print("Starts with '  Py':", sample_text.startswith("  Py"))
print("Ends with '!  ':", sample_text.endswith("!  "))

print()

# Exercise 2: Text Analyzer (simulated with preset text)
print("Exercise 2: Text Analyzer")
text = "The quick brown fox jumps over the lazy dog"
print("Analyzing:", text)

# Analysis
char_count_with_spaces = len(text)
char_count_without_spaces = len(text.replace(" ", ""))
word_count = len(text.split())

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

# First and last words
words = text.split()
first_word = words[0] if words else ""
last_word = words[-1] if words else ""

# Reverse text
reversed_text = text[::-1]

print(f"Characters (with spaces): {char_count_with_spaces}")
print(f"Characters (without spaces): {char_count_without_spaces}")
print(f"Word count: {word_count}")
print(f"Vowel count: {vowel_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Reversed: {reversed_text}")

print()

# Exercise 3: Name Formatter
print("Exercise 3: Name Formatter")
full_name = "  john    michael   SMITH  "
print("Original name:", repr(full_name))

# Clean and format
cleaned_name = full_name.strip()
name_parts = cleaned_name.split()
formatted_parts = [part.title() for part in name_parts]
formatted_name = " ".join(formatted_parts)

# Extract components
if len(formatted_parts) >= 2:
    first_name = formatted_parts[0]
    last_name = formatted_parts[-1]
    middle_names = formatted_parts[1:-1] if len(formatted_parts) > 2 else []
else:
    first_name = formatted_parts[0] if formatted_parts else ""
    last_name = ""
    middle_names = []

# Create initials
initials = "".join([part[0] for part in formatted_parts if part])

# Username suggestion
import random
username = first_name.lower() + str(random.randint(100, 999))

print(f"Formatted name: {formatted_name}")
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Middle names: {middle_names}")
print(f"Initials: {initials}")
print(f"Username suggestion: {username}")

print()

# Exercise 4: Password Strength Checker
print("Exercise 4: Password Strength Checker")
password = "MySecure123!"
print("Checking password:", password)

# Check criteria
min_length = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

# Count satisfied criteria
criteria_met = sum([min_length, has_upper, has_lower, has_digit, has_special])

# Determine strength
if criteria_met >= 5:
    strength = "Strong"
elif criteria_met >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print(f"Length >= 8: {min_length}")
print(f"Has uppercase: {has_upper}")
print(f"Has lowercase: {has_lower}")
print(f"Has numbers: {has_digit}")
print(f"Has special chars: {has_special}")
print(f"Overall strength: {strength}")

print()

# Exercise 5: Mad Libs Generator
print("Exercise 5: Mad Libs Generator")

# Preset inputs for demonstration
noun = "elephant"
verb = "danced"
adjective = "purple"
place = "library"
number = "42"
color = "green"
animal = "penguin"

story = f"Yesterday, I {verb} to the {place} and saw a {adjective} {color} {animal}! There were {number} {noun}s there too!"
print("Mad Libs Story:")
print(story)

print()

# Exercise 6: Email Validator
print("Exercise 6: Email Validator")
email = "user@example.com"
print("Validating email:", email)

# Validation checks
has_single_at = email.count("@") == 1
has_text_before_at = len(email.split("@")[0]) > 0
has_text_after_at = len(email.split("@")[1]) > 0 if "@" in email else False
valid_domains = [".com", ".org", ".edu", ".net"]
has_valid_domain = any(email.endswith(domain) for domain in valid_domains)
no_spaces = " " not in email

all_valid = all([has_single_at, has_text_before_at, has_text_after_at, has_valid_domain, no_spaces])

print(f"Has single @: {has_single_at}")
print(f"Text before @: {has_text_before_at}")
print(f"Text after @: {has_text_after_at}")
print(f"Valid domain: {has_valid_domain}")
print(f"No spaces: {no_spaces}")
print(f"Overall valid: {all_valid}")

print()

# Exercise 7: String Slicing Practice
print("Exercise 7: String Slicing")
word = "PROGRAMMING"
print("Original word:", word)

print("First 4 characters:", word[:4])
print("Last 4 characters:", word[-4:])
print("Every other character:", word[::2])
print("Middle 4 characters:", word[3:7])  # GRAM
print("String reversed:", word[::-1])
print("Characters at even positions:", word[::2])
print("Characters at odd positions:", word[1::2])

print()

# Exercise 8: Interactive Story (simplified for demo)
print("Exercise 8: Interactive Story Builder")
character_name = "Alex"
choice = "explore"

print(f"Welcome to the Adventure Story Generator!")
print(f"Your character {character_name} decides to {choice}.")

if choice == "explore":
    print(f"{character_name} ventures into the mysterious forest and discovers a hidden treasure!")
elif choice == "rest":
    print(f"{character_name} takes a peaceful nap and dreams of great adventures.")
elif choice == "fight":
    print(f"{character_name} bravely faces the dragon and emerges victorious!")
else:
    print(f"{character_name} chooses their own path and writes their own destiny.")

print()

# Challenge: Text Encryption (Caesar Cipher)
print("Challenge: Simple Text Encryption")
message = "HELLO WORLD"
shift = 3
print(f"Original message: {message}")
print(f"Shift amount: {shift}")

encrypted = ""
for char in message:
    if char.isalpha():
        # Handle uppercase letters
        if char.isupper():
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        encrypted += shifted
    else:
        encrypted += char

print(f"Encrypted message: {encrypted}")

# Demonstrate decryption
decrypted = ""
for char in encrypted:
    if char.isalpha():
        if char.isupper():
            shifted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            shifted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        decrypted += shifted
    else:
        decrypted += char

print(f"Decrypted message: {decrypted}")

print()
print("=== Day 3 Solutions Complete! ===")

"""
Teaching Notes for Mentors:
===========================

Key Learning Objectives Demonstrated:
1. String method usage (.strip(), .upper(), .lower(), etc.)
2. String slicing and indexing
3. Text analysis and processing
4. Input validation techniques
5. String formatting (f-strings, concatenation)
6. Character encoding with ord() and chr()

Important Concepts to Emphasize:
- Strings are immutable in Python
- String methods return new strings
- Slicing syntax: [start:end:step]
- String comparison is case-sensitive
- Unicode and ASCII character codes

Common Student Challenges:
1. Understanding string immutability
2. Slicing syntax confusion (negative indices)
3. Case sensitivity in comparisons
4. Handling edge cases in validation
5. Working with user input (always strings)

Extension Opportunities:
- Regular expressions for pattern matching
- String encoding/decoding (UTF-8, ASCII)
- More complex text analysis algorithms
- File reading and text processing
- Natural language processing basics

Code Quality Highlights:
- Clear variable names for text processing
- Comprehensive validation logic
- Multiple approaches to string manipulation
- Error handling for edge cases
- Educational use of algorithms (Caesar cipher)

Real-World Applications:
- Data cleaning and preprocessing
- User input validation
- Text analysis and NLP
- Cryptography basics
- Web form processing
"""