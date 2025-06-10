"""
Week 1 Final Project: Personal Information Manager
================================================

Instructions:
1. Complete each section by adding your own information
2. Use the concepts learned throughout Week 1
3. Feel free to customize and add your own creative touches
4. Test your code frequently as you build it

Required concepts to demonstrate:
- Print statements
- Variables (strings, numbers)
- Lists
- Dictionaries
- Comments
- Basic formatting

Tips:
- Replace placeholder information with your own details
- Add more sections if you want to be creative
- Use meaningful variable names
- Add comments to explain your code
- Test your program often to catch errors early
"""

# TODO: Add your personal information here
print("================================")
print("    PERSONAL INFORMATION MANAGER")
print("================================")
print()

# Section 1: Personal Profile
print("Personal Profile:")
print("-" * 20)

# TODO: Create variables for your personal information
name = "Your Name Here"
age = 0  # Replace with your age
location = "Your City, State"
favorite_color = "Your Favorite Color"
hobby = "Your Favorite Hobby"
fun_fact = "Something interesting about you"

# TODO: Print your personal information using the variables
print("Name:", name)
print("Age:", age, "years old")
# Add more print statements for location, color, hobby, and fun fact


print()

# Section 2: Contact Information
print("Contact Information:")
print("-" * 20)

# TODO: Create variables for contact information
email = "your.email@example.com"
phone = "(555) 123-4567"

# TODO: Print contact information
print("Email:", email)
# Add print statement for phone


print()

# Section 3: Favorite Movies (Using Lists)
print("My Top 5 Favorite Movies:")
print("-" * 25)

# TODO: Create a list of your favorite movies
favorite_movies = [
    "Movie 1",
    "Movie 2", 
    "Movie 3",
    "Movie 4",
    "Movie 5"
]

# TODO: Print each movie with its number
# Hint: You can use the format: print("1.", favorite_movies[0])
print("1.", favorite_movies[0])
# Add print statements for the other 4 movies


print()

# Section 4: Programming Goals (Using Dictionaries)
print("My Programming Goals:")
print("-" * 20)

# TODO: Create a dictionary with your programming goals
programming_goals = {
    "short_term": "Your short-term programming goal",
    "long_term": "Your long-term programming goal",
    "current_focus": "What you're focusing on right now",
    "dream_project": "A project you'd love to build someday"
}

# TODO: Print your goals using the dictionary
print("Short-term goal:", programming_goals["short_term"])
# Add print statements for the other goals


print()

# Section 5: Fun Calculations (Using Numbers)
print("Fun Facts About Me:")
print("-" * 18)

# TODO: Calculate your age in days (approximately)
# Hint: age_in_days = age * 365
age_in_days = age * 365
print("I am approximately", age_in_days, "days old!")

# TODO: Add more fun calculations
# Ideas: 
# - Hours spent sleeping (age * 365 * 8)
# - How many years you want to program
# - Days until your next birthday


print()

# Section 6: Skills and Interests (Using Lists)
print("Programming Languages I Want to Learn:")
print("-" * 38)

# TODO: Create a list of programming languages you want to learn
languages_to_learn = [
    "Python",  # You're already learning this one!
    "JavaScript",
    "Add more languages here"
]

# TODO: Print each language
for i, language in enumerate(languages_to_learn, 1):
    print(f"{i}. {language}")

print()

# Section 7: Creative Section (Your Choice!)
print("Something Special About Me:")
print("-" * 26)

# TODO: Add your own creative section here
# Ideas:
# - Favorite books
# - Places you want to visit
# - Skills you have
# - Interesting experiences
# - Goals for this year


print()

# Section 8: Closing Message
print("================================")
print("Thanks for learning about me!")
print("I'm excited to continue learning Python!")
print("================================")

"""
Extension Ideas (Optional Challenges):

1. ASCII Art: Add some ASCII art to make your output more visual
2. More Lists: Add lists for books, places to visit, foods you like
3. Nested Dictionaries: Create more complex data structures
4. User Input: Ask the user questions and respond (if you've learned input())
5. Formatting: Make your output even more beautiful with spacing and symbols

Self-Check Questions:
1. Does your program run without errors?
2. Have you used variables, lists, and dictionaries?
3. Is your output formatted nicely?
4. Do your variable names make sense?
5. Have you added helpful comments?

Remember: This is YOUR project - make it reflect who you are!
"""