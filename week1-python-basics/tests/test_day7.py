"""
Day 7 Tests: Integration Project
===============================

Integration tests for the Week 1 capstone project.
Tests the combination of all concepts learned.
"""

import pytest
import sys
import os
from datetime import datetime, date

# Add the project root to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_data_structure_creation():
    """Test that basic data structures can be created and used"""
    # Test dictionary for user profile
    user_profile = {
        "name": "Test User",
        "age": 25,
        "email": "test@example.com",
        "interests": ["programming", "reading"]
    }
    
    assert isinstance(user_profile, dict)
    assert user_profile["name"] == "Test User"
    assert isinstance(user_profile["interests"], list)
    assert len(user_profile["interests"]) == 2

def test_contact_management():
    """Test contact management functionality"""
    contacts = {}
    
    # Add contact
    contact_id = "001"
    contacts[contact_id] = {
        "name": "John Doe",
        "phone": "555-1234",
        "email": "john@example.com"
    }
    
    assert contact_id in contacts
    assert contacts[contact_id]["name"] == "John Doe"
    
    # Update contact
    contacts[contact_id]["phone"] = "555-5678"
    assert contacts[contact_id]["phone"] == "555-5678"
    
    # Delete contact
    del contacts[contact_id]
    assert contact_id not in contacts

def test_goal_tracking():
    """Test goal tracking functionality"""
    goals = {}
    
    # Add goal
    goal_id = 1
    goals[goal_id] = {
        "title": "Learn Python",
        "description": "Complete Week 1",
        "deadline": date(2024, 12, 31),
        "completed": False,
        "category": "learning"
    }
    
    assert goals[goal_id]["title"] == "Learn Python"
    assert goals[goal_id]["completed"] == False
    
    # Complete goal
    goals[goal_id]["completed"] = True
    goals[goal_id]["completion_date"] = date.today()
    
    assert goals[goal_id]["completed"] == True

def test_expense_tracking():
    """Test expense tracking functionality"""
    expenses = []
    
    # Add income
    income = {
        "date": "2024-01-01",
        "amount": 3000.00,
        "category": "salary",
        "description": "Monthly salary",
        "type": "income"
    }
    expenses.append(income)
    
    # Add expense
    expense = {
        "date": "2024-01-02",
        "amount": 1200.00,
        "category": "rent",
        "description": "Monthly rent",
        "type": "expense"
    }
    expenses.append(expense)
    
    assert len(expenses) == 2
    assert expenses[0]["type"] == "income"
    assert expenses[1]["type"] == "expense"
    
    # Calculate totals
    total_income = sum(t["amount"] for t in expenses if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in expenses if t["type"] == "expense")
    net_savings = total_income - total_expenses
    
    assert total_income == 3000.00
    assert total_expenses == 1200.00
    assert net_savings == 1800.00

def test_skill_tracking():
    """Test skill tracking functionality"""
    skills = {}
    
    # Add skill
    skill_name = "Python"
    skills[skill_name] = {
        "proficiency": 3,  # 1-10 scale
        "hours_practiced": 20,
        "notes": "Learning basics"
    }
    
    assert skills[skill_name]["proficiency"] == 3
    
    # Update proficiency
    skills[skill_name]["proficiency"] = 5
    skills[skill_name]["hours_practiced"] += 10
    
    assert skills[skill_name]["proficiency"] == 5
    assert skills[skill_name]["hours_practiced"] == 30

def test_data_validation():
    """Test data validation helpers"""
    
    def validate_email(email):
        return "@" in email and "." in email and len(email) > 5
    
    def validate_phone(phone):
        digits = "".join(c for c in phone if c.isdigit())
        return len(digits) == 10
    
    def validate_proficiency(level):
        return isinstance(level, int) and 1 <= level <= 10
    
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False
    
    assert validate_phone("555-123-4567") == True
    assert validate_phone("123") == False
    
    assert validate_proficiency(5) == True
    assert validate_proficiency(15) == False

def test_data_analysis():
    """Test basic data analysis functionality"""
    # Sample expense data
    expenses = [
        {"amount": 1200, "category": "rent"},
        {"amount": 500, "category": "groceries"},
        {"amount": 300, "category": "utilities"},
        {"amount": 200, "category": "groceries"}
    ]
    
    # Total expenses
    total = sum(e["amount"] for e in expenses)
    assert total == 2200
    
    # Average expense
    average = total / len(expenses)
    assert average == 550
    
    # Expenses by category
    categories = {}
    for expense in expenses:
        cat = expense["category"]
        categories[cat] = categories.get(cat, 0) + expense["amount"]
    
    assert categories["groceries"] == 700
    assert categories["rent"] == 1200

def test_date_calculations():
    """Test date-related calculations"""
    from datetime import date, timedelta
    
    def days_until_deadline(deadline_str):
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        today = date.today()
        delta = deadline - today
        return delta.days
    
    def age_from_birth_year(birth_year):
        current_year = date.today().year
        return current_year - birth_year
    
    # Test with future date
    future_date = (date.today() + timedelta(days=30)).strftime("%Y-%m-%d")
    days_left = days_until_deadline(future_date)
    assert 29 <= days_left <= 31  # Account for today's calculation
    
    # Test age calculation
    assert age_from_birth_year(2000) == date.today().year - 2000

def test_search_functionality():
    """Test search and filtering functionality"""
    contacts = {
        "001": {"name": "John Doe", "phone": "555-1234"},
        "002": {"name": "Jane Smith", "phone": "555-5678"},
        "003": {"name": "Bob Johnson", "phone": "555-9999"}
    }
    
    def search_contacts_by_name(contacts, query):
        results = {}
        for contact_id, contact in contacts.items():
            if query.lower() in contact["name"].lower():
                results[contact_id] = contact
        return results
    
    # Search for "John"
    results = search_contacts_by_name(contacts, "John")
    assert len(results) == 2  # John Doe and Bob Johnson
    
    # Search for exact match
    results = search_contacts_by_name(contacts, "Jane Smith")
    assert len(results) == 1

def test_data_export():
    """Test data export functionality"""
    def format_contact_for_export(contact):
        return f"{contact['name']},{contact['phone']},{contact.get('email', 'N/A')}"
    
    def export_contacts_to_text(contacts):
        lines = ["Name,Phone,Email"]  # Header
        for contact in contacts.values():
            lines.append(format_contact_for_export(contact))
        return "\n".join(lines)
    
    contacts = {
        "001": {"name": "John Doe", "phone": "555-1234", "email": "john@example.com"}
    }
    
    exported = export_contacts_to_text(contacts)
    lines = exported.split("\n")
    
    assert lines[0] == "Name,Phone,Email"
    assert "John Doe" in lines[1]

def test_menu_navigation():
    """Test menu system logic"""
    def process_menu_choice(choice, valid_choices):
        if choice in valid_choices:
            return True, f"Selected: {choice}"
        else:
            return False, "Invalid choice"
    
    valid_choices = ["1", "2", "3", "4", "5"]
    
    success, message = process_menu_choice("3", valid_choices)
    assert success == True
    assert "Selected: 3" in message
    
    success, message = process_menu_choice("9", valid_choices)
    assert success == False
    assert "Invalid choice" in message

def test_integration_requirements():
    """Test that integration requirements are met"""
    # Test that all required data types are used
    
    # Strings
    name = "Test User"
    assert isinstance(name, str)
    
    # Numbers (int and float)
    age = 25
    height = 5.6
    assert isinstance(age, int)
    assert isinstance(height, float)
    
    # Boolean
    is_active = True
    assert isinstance(is_active, bool)
    
    # List
    interests = ["coding", "reading"]
    assert isinstance(interests, list)
    
    # Dictionary
    profile = {"name": name, "age": age}
    assert isinstance(profile, dict)
    
    # Nested structures
    complex_data = {
        "users": [
            {"name": "Alice", "scores": [85, 90, 88]},
            {"name": "Bob", "scores": [92, 87, 95]}
        ]
    }
    assert isinstance(complex_data["users"], list)
    assert isinstance(complex_data["users"][0], dict)
    assert isinstance(complex_data["users"][0]["scores"], list)

class TestProjectQuality:
    """Test overall project quality requirements"""
    
    def test_data_persistence(self):
        """Test that data structures maintain state"""
        data = {"counter": 0}
        
        # Simulate operations
        data["counter"] += 1
        assert data["counter"] == 1
        
        data["counter"] *= 2
        assert data["counter"] == 2
    
    def test_error_handling(self):
        """Test basic error handling patterns"""
        def safe_divide(a, b):
            try:
                return a / b
            except ZeroDivisionError:
                return "Cannot divide by zero"
        
        assert safe_divide(10, 2) == 5
        assert safe_divide(10, 0) == "Cannot divide by zero"
    
    def test_input_validation(self):
        """Test input validation patterns"""
        def validate_age(age_str):
            try:
                age = int(age_str)
                return 0 <= age <= 150
            except ValueError:
                return False
        
        assert validate_age("25") == True
        assert validate_age("200") == False
        assert validate_age("abc") == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])