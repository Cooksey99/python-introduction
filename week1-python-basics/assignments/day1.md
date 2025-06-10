# Day 1: Environment Setup and Hello World

## 🎯 Learning Objectives

By the end of Day 1, you will be able to:
- Set up a Python development environment on your computer
- Write and run your first Python program
- Understand the basic structure of a Python program
- Use the `print()` function to display output
- Navigate and use a code editor effectively
- Troubleshoot common setup issues

## 📋 Pre-Work

Before starting today's lesson:
- [ ] Ensure you have completed the setup instructions in the main README.md
- [ ] Have Python installed and verified (run `python --version` in terminal)
- [ ] Have a code editor ready (VS Code, PyCharm, or IDLE)
- [ ] Create a folder on your desktop called "python-practice"

## 📚 Concepts Covered

### 1. Python Interpreter
The Python interpreter is a program that reads and executes Python code. When you type `python` in your terminal, you're starting the interpreter.

### 2. Python Files
Python programs are saved as files with the `.py` extension. These are plain text files containing Python code.

### 3. The `print()` Function
The `print()` function displays output to the screen. It's one of the most basic and useful functions in Python.

### 4. Strings
Text in Python is called a "string" and must be enclosed in quotes (single or double).

## 🔧 Step-by-Step Instructions

### Step 1: Verify Your Setup (5 minutes)

1. **Open your terminal/command prompt**
   - Windows: Press Win+R, type `cmd`, press Enter
   - Mac: Press Cmd+Space, type "terminal", press Enter
   - Linux: Press Ctrl+Alt+T

2. **Check Python installation**
   ```bash
   python --version
   ```
   You should see something like `Python 3.11.5` or similar.

3. **Test the Python interpreter**
   ```bash
   python
   ```
   You should see the Python prompt `>>>`. Type `exit()` to quit.

### Step 2: Create Your First Python File (10 minutes)

1. **Open your code editor** (VS Code, PyCharm, or IDLE)

2. **Create a new file** and save it as `hello_world.py` in your python-practice folder

3. **Type this code exactly as shown:**
   ```python
   print("Hello, World!")
   ```

4. **Save the file** (Ctrl+S or Cmd+S)

### Step 3: Run Your First Program (10 minutes)

#### Method 1: Using the Terminal
1. Navigate to your python-practice folder in terminal:
   ```bash
   cd path/to/your/python-practice
   ```
2. Run your program:
   ```bash
   python hello_world.py
   ```

#### Method 2: Using Your Code Editor
- **VS Code**: Click the play button in the top right, or press F5
- **PyCharm**: Right-click in the editor and select "Run"
- **IDLE**: Press F5

**Expected Output:**
```
Hello, World!
```

### Step 4: Experiment with Print Statements (15 minutes)

Create a new file called `print_practice.py` and try these examples:

```python
# This is a comment - it doesn't run as code
print("Hello, World!")
print('You can use single quotes too')
print("My name is [Your Name]")  # Replace with your actual name
print("I am learning Python!")
```

**Try running this and observe the output.**

### Step 5: Multiple Print Statements (10 minutes)

Add more print statements to see how they work:

```python
print("Welcome to Python!")
print("This is my first program.")
print("Python is fun!")
print("I can print multiple lines.")
```

**Expected Output:**
```
Welcome to Python!
This is my first program.
Python is fun!
I can print multiple lines.
```

### Step 6: Print with Numbers (10 minutes)

Try printing numbers (notice no quotes needed):

```python
print("Text needs quotes")
print(42)
print(3.14)
print("I am", 25, "years old")
```

**Expected Output:**
```
Text needs quotes
42
3.14
I am 25 years old
```

## 💡 Key Concepts to Remember

1. **Python is case-sensitive**: `Print()` is different from `print()`
2. **Strings need quotes**: Text must be in quotes, numbers don't
3. **Indentation matters**: Python uses indentation to organize code
4. **Comments start with #**: Use comments to explain your code
5. **Save before running**: Always save your file before running it

## 🏋️ Practice Exercises

### Basic Level

**Exercise 1: Personal Introduction**
Create a file called `introduction.py` and write a program that prints:
- Your name
- Your age
- Your favorite color
- One thing you want to learn about programming

**Example Output:**
```
My name is Alex
I am 22 years old
My favorite color is blue
I want to learn how to build websites
```

**Exercise 2: ASCII Art**
Create a file called `ascii_art.py` and use print statements to create simple ASCII art:

```python
print("  *  ")
print(" *** ")
print("*****")
print(" *** ")
print("  *  ")
```

**Exercise 3: Story Printer**
Create a file called `story.py` that prints a short 5-line story of your choice.

### Intermediate Level

**Exercise 4: Mixed Content**
Create a file called `mixed_printing.py` that demonstrates:
- Printing text
- Printing numbers
- Printing text and numbers together
- Using both single and double quotes

**Exercise 5: Multi-line Message**
Create a program that prints a formatted message like:
```
=============================
    WELCOME TO PYTHON!
=============================
Today's lesson: Hello World
Status: Learning in progress
=============================
```

### Challenge Level

**Exercise 6: Error Investigation**
Try running each of these code snippets and explain what happens:

```python
# Test 1
print("Hello World")

# Test 2
Print("Hello World")

# Test 3
print(Hello World)

# Test 4
print("Hello World"
```

Write your observations in comments in your code.

## ✅ Self-Testing Instructions

### Manual Verification
1. **Can you create a new Python file?** ✓/✗
2. **Can you run a Python program from the terminal?** ✓/✗
3. **Can you run a Python program from your editor?** ✓/✗
4. **Do you see the expected output?** ✓/✗
5. **Can you print both text and numbers?** ✓/✗

### Understanding Check
Answer these questions to yourself:
1. What file extension do Python files use?
2. What function is used to display output in Python?
3. What's the difference between `print("5")` and `print(5)`?
4. Why do we put quotes around text but not numbers?

### Automated Testing
Run the Day 1 test file to check your work:
```bash
python -m pytest tests/test_day1.py -v
```

## 🛠️ Troubleshooting Guide

### Common Issues and Solutions

**Issue 1: "python is not recognized" or "command not found"**
- **Solution**: Python is not in your PATH. Reinstall Python and check "Add to PATH"
- **Alternative**: Try `python3` instead of `python`

**Issue 2: "No such file or directory"**
- **Solution**: Make sure you're in the correct folder. Use `cd` to navigate to your file location

**Issue 3: "SyntaxError: invalid syntax"**
- **Solution**: Check for typos, missing quotes, or parentheses
- **Common mistake**: Writing `Print` instead of `print`

**Issue 4: Nothing happens when I run the program**
- **Solution**: Make sure you saved the file and are running the correct file name

**Issue 5: "IndentationError"**
- **Solution**: Make sure all lines start at the left margin (no extra spaces at the beginning)

**Issue 6: Code editor doesn't run Python**
- **Solution**: Check that Python interpreter is selected in your editor settings

### Debugging Steps
1. **Read the error message carefully** - it often tells you exactly what's wrong
2. **Check line numbers** - errors often reference specific lines
3. **Verify file is saved** - unsaved changes won't run
4. **Start small** - if complex code doesn't work, try simpler versions first

## 📊 Success Criteria

By the end of Day 1, you should be able to:
- [ ] Create a new Python file
- [ ] Write print statements with text and numbers
- [ ] Run Python programs successfully
- [ ] Troubleshoot basic syntax errors
- [ ] Understand the difference between strings and numbers in print statements

### Self-Assessment Scale
Rate your confidence (1-5) on:
- Setting up Python development environment: ___/5
- Writing basic print statements: ___/5
- Running Python programs: ___/5
- Understanding error messages: ___/5

**Target**: All ratings should be 3 or higher before moving to Day 2.

## 🚀 Extension Activities (For Fast Learners)

### Advanced Challenges
1. **Research Project**: Look up 3 other Python functions besides `print()` and write what you think they do
2. **Creative ASCII**: Create a more complex ASCII art picture using only print statements
3. **Error Collection**: Intentionally create 5 different types of errors and document the error messages
4. **Environment Exploration**: Learn about your code editor's features (auto-completion, syntax highlighting)

### Real-World Connections
- **Where is Python used?** Research 3 companies or applications that use Python
- **Python versions**: Look up the difference between Python 2 and Python 3
- **Programming languages**: Compare Python to other languages you might have heard of

## 📝 Day 1 Reflection

Before moving to Day 2, take a moment to reflect:
1. What was the most challenging part of today's lesson?
2. What concept made the most sense to you?
3. What are you excited to learn next?
4. What questions do you still have?

Write your reflections in a file called `day1_reflection.txt`.

## 🎯 Preparation for Day 2

Tomorrow we'll learn about variables and data types. To prepare:
- Make sure you can confidently run Python programs
- Keep your python-practice folder organized
- Think about what kinds of information you might want to store in a program

**Great job completing Day 1! You've taken your first steps into the world of programming! 🎉**