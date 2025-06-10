# Week 1: Python Programming Basics

Welcome to your first week of Python programming! This comprehensive learning package is designed for complete beginners and will guide you through the fundamentals of Python programming over 7 days.

## 📋 Overview

This week covers essential Python concepts that form the foundation of programming:

- **Day 1**: Environment setup and Hello World
- **Day 2**: Variables and data types  
- **Day 3**: String operations and user input
- **Day 4**: Numbers and math operations
- **Day 5**: Lists basics
- **Day 6**: Dictionaries basics
- **Day 7**: Integration project

Each day is designed for 1-2 hours of focused learning and practice.

## 🎯 Learning Objectives

By the end of Week 1, you will be able to:
- Set up a Python development environment
- Write and run basic Python programs
- Work with variables and different data types
- Manipulate strings and handle user input
- Perform mathematical operations
- Create and manipulate lists and dictionaries
- Combine concepts to build a simple project

## 📂 Project Structure

```
week1-python-basics/
├── README.md                 # This file - overview and setup
├── assignments/              # Daily lesson materials
│   ├── day1.md              # Environment setup and Hello World
│   ├── day2.md              # Variables and data types
│   ├── day3.md              # String operations and user input
│   ├── day4.md              # Numbers and math operations
│   ├── day5.md              # Lists basics
│   ├── day6.md              # Dictionaries basics
│   └── day7.md              # Integration project
├── exercises/               # Practice exercises for each day
│   ├── day1_exercises.py
│   ├── day2_exercises.py
│   └── ... (for each day)
├── solutions/              # Solution files for reference
│   ├── day1_solutions.py
│   ├── day2_solutions.py
│   └── ... (for each day)
├── tests/                  # Automated tests to check your work
│   ├── test_day1.py
│   ├── test_day2.py
│   └── ... (for each day)
└── final_project/          # Week-end integration project
    ├── requirements.md
    └── starter_code.py
```

## 🛠️ Setup Instructions

### Prerequisites
- A computer with internet access
- Basic computer literacy (creating files, navigating folders)
- Enthusiasm to learn!

### Python Installation

#### Option 1: Python.org (Recommended for beginners)
1. Visit [python.org/downloads](https://python.org/downloads)
2. Download Python 3.11 or 3.12 (latest stable version)
3. Run the installer
4. **Important**: Check "Add Python to PATH" during installation
5. Verify installation by opening terminal/command prompt and typing:
   ```bash
   python --version
   ```

#### Option 2: Anaconda (Alternative)
1. Visit [anaconda.com](https://www.anaconda.com/products/distribution)
2. Download and install Anaconda
3. Use Anaconda Navigator or conda commands

### Code Editor Setup

Choose one of these beginner-friendly editors:

#### VS Code (Recommended)
1. Download from [code.visualstudio.com](https://code.visualstudio.com)
2. Install the Python extension by Microsoft
3. Configure Python interpreter (Ctrl/Cmd + Shift + P → "Python: Select Interpreter")

#### PyCharm Community Edition
1. Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm)
2. Choose Community Edition (free)
3. Create a new Python project

#### IDLE (Comes with Python)
- Basic editor that comes pre-installed with Python
- Good for simple scripts and learning

### Testing Your Setup

1. Create a test file called `hello_test.py`
2. Add this code:
   ```python
   print("Hello, Python!")
   print("Setup successful!")
   ```
3. Run the file:
   - **VS Code**: Click the play button or press F5
   - **PyCharm**: Right-click and select "Run"
   - **IDLE**: Press F5
   - **Terminal**: `python hello_test.py`

If you see both messages printed, you're ready to start!

## 📚 How to Use This Course

### Daily Routine
1. **Read the assignment** (assignments/dayX.md)
2. **Follow along** with guided examples
3. **Complete exercises** (exercises/dayX_exercises.py)
4. **Run tests** to check your work
5. **Review solutions** if needed
6. **Self-assess** using the provided checklists

### Testing Your Work

#### Automated Tests
Run tests for each day to verify your solutions:
```bash
python -m pytest tests/test_day1.py -v
```

#### Manual Verification
Each assignment includes step-by-step verification instructions.

### Getting Help

#### Self-Help Resources
1. **Common Errors Section** in each assignment
2. **Troubleshooting Guide** in each day's materials
3. **Solution files** for reference (try first on your own!)

#### When Stuck
1. Read error messages carefully
2. Check the troubleshooting section
3. Review the examples in the assignment
4. Compare with solution files
5. Take a break and come back with fresh eyes

## 📊 Progress Tracking

### Daily Checklists
Each day includes a self-assessment checklist to track your understanding.

### Success Criteria
- **Beginner**: Complete basic exercises
- **Intermediate**: Complete all exercises including intermediate level
- **Advanced**: Complete challenge exercises and explore extensions

### Time Management
- **Minimum**: 1 hour per day (basic exercises)
- **Recommended**: 1.5-2 hours per day (complete experience)
- **Extended**: Add 30-60 minutes for challenge exercises

## 🎖️ Completion Requirements

To successfully complete Week 1:
- [ ] Complete all 7 daily assignments
- [ ] Pass all automated tests
- [ ] Complete the final integration project
- [ ] Self-assess as "confident" on all daily checklists

## 🚀 What's Next?

After completing Week 1, you'll be ready for:
- Week 2: Control Flow and Functions
- Week 3: File Operations and Error Handling
- Week 4: Object-Oriented Programming Basics

## 📝 Notes for Mentors

### Teaching Points
- Emphasize hands-on practice over theory
- Encourage experimentation and making mistakes
- Focus on building confidence through small wins
- Connect concepts to real-world applications

### Common Student Challenges
1. **Environment setup** - Be patient, this is often the hardest part
2. **Syntax errors** - Teach careful reading of error messages
3. **Indentation** - Emphasize Python's whitespace sensitivity
4. **Variable naming** - Establish good practices early

### Assessment Opportunities
- Review completed exercises
- Observe problem-solving approach
- Check understanding through questioning
- Evaluate final project complexity and creativity

## 🆘 Troubleshooting

### Installation Issues
- **"Python not found"**: PATH not set correctly
- **Permission errors**: Run as administrator/sudo
- **Version conflicts**: Use virtual environments

### Common Beginner Mistakes
- Forgetting to save files before running
- Incorrect indentation
- Mixing up assignment (=) and comparison (==)
- Not reading error messages

### Performance Tips
- Start each day fresh
- Take breaks when frustrated
- Practice typing code rather than copy-pasting
- Explain your code out loud

---

**Ready to start?** Open `assignments/day1.md` and begin your Python journey!

**Remember**: Programming is learned by doing. Make mistakes, fix them, and keep coding!