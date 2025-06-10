"""
Day 7 Integration Project Solutions: Personal Data Manager
=========================================================

Complete implementation of the Personal Data Manager application.
"""

import random
import datetime

print("=== Day 7 Integration Project ===")
print("Personal Data Manager Solution")
print()

# Global data structures
user_profile = {}
contacts = {}
goals = {}
expenses = []
skills = {}

def display_welcome():
    """Display welcome message and app info"""
    print("=" * 50)
    print("    PERSONAL DATA MANAGER")
    print("    Week 1 Integration Project")
    print("=" * 50)
    print("Manage your personal information, contacts, goals,")
    print("expenses, and learning progress all in one place!")
    print()

def setup_profile():
    """Setup user profile with comprehensive information"""
    global user_profile
    print("=== Personal Profile Setup ===")
    
    user_profile["name"] = input("Enter your full name: ")
    
    while True:
        try:
            user_profile["age"] = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number for age!")
    
    user_profile["location"] = input("Enter your location (city, state/country): ")
    user_profile["email"] = input("Enter your email: ")
    user_profile["phone"] = input("Enter your phone number: ")
    user_profile["occupation"] = input("Enter your occupation: ")
    
    interests_input = input("Enter your interests (comma-separated): ")
    user_profile["interests"] = [i.strip() for i in interests_input.split(",")]
    
    user_profile["created_date"] = datetime.date.today().strftime("%Y-%m-%d")
    
    print("\nProfile created successfully!")

def display_profile():
    """Display user profile information"""
    if not user_profile:
        print("Profile not set up yet!")
        return
    
    print("\n=== Your Profile ===")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Location: {user_profile['location']}")
    print(f"Email: {user_profile['email']}")
    print(f"Phone: {user_profile['phone']}")
    print(f"Occupation: {user_profile['occupation']}")
    print(f"Interests: {', '.join(user_profile['interests'])}")
    print(f"Profile created: {user_profile['created_date']}")

# Contact Management Functions
def add_contact():
    """Add new contact"""
    print("\n=== Add New Contact ===")
    name = input("Contact name: ")
    
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Phone number: ")
    email = input("Email address: ")
    address = input("Address: ")
    birthday = input("Birthday (YYYY-MM-DD, optional): ")
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
        "birthday": birthday,
        "added_date": datetime.date.today().strftime("%Y-%m-%d")
    }
    
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Display all contacts"""
    if not contacts:
        print("No contacts found!")
        return
    
    print(f"\n=== All Contacts ({len(contacts)} total) ===")
    for name in sorted(contacts.keys()):
        contact = contacts[name]
        print(f"\n{name}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
        print(f"  Address: {contact['address']}")
        if contact['birthday']:
            print(f"  Birthday: {contact['birthday']}")

def search_contact():
    """Search for contact by name or phone"""
    search_term = input("Enter name or phone number to search: ").lower()
    found = False
    
    for name, contact in contacts.items():
        if search_term in name.lower() or search_term in contact['phone']:
            print(f"\nFound: {name}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            found = True
    
    if not found:
        print("No matching contacts found!")

def update_contact():
    """Update existing contact"""
    name = input("Enter contact name to update: ")
    
    if name not in contacts:
        print("Contact not found!")
        return
    
    print("\nWhat would you like to update?")
    print("1. Phone")
    print("2. Email")
    print("3. Address")
    print("4. Birthday")
    
    choice = input("Choose option (1-4): ")
    
    if choice == "1":
        contacts[name]["phone"] = input("New phone number: ")
    elif choice == "2":
        contacts[name]["email"] = input("New email: ")
    elif choice == "3":
        contacts[name]["address"] = input("New address: ")
    elif choice == "4":
        contacts[name]["birthday"] = input("New birthday (YYYY-MM-DD): ")
    else:
        print("Invalid choice!")
        return
    
    print("Contact updated successfully!")

def delete_contact():
    """Delete a contact"""
    name = input("Enter contact name to delete: ")
    
    if name not in contacts:
        print("Contact not found!")
        return
    
    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ")
    if confirm.lower() == "yes":
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Deletion cancelled.")

# Goal Management Functions
def add_goal():
    """Add new goal"""
    print("\n=== Add New Goal ===")
    goal_id = f"G{len(goals) + 1:03d}"
    
    title = input("Goal title: ")
    description = input("Goal description: ")
    category = input("Category (personal/career/health/financial/other): ")
    deadline = get_valid_date("Deadline")
    
    goals[goal_id] = {
        "title": title,
        "description": description,
        "category": category,
        "deadline": deadline.strftime("%Y-%m-%d"),
        "status": "active",
        "created_date": datetime.date.today().strftime("%Y-%m-%d"),
        "completed_date": None
    }
    
    print(f"Goal '{title}' added successfully! (ID: {goal_id})")

def view_goals():
    """Display all goals"""
    if not goals:
        print("No goals found!")
        return
    
    active_goals = [g for g in goals.values() if g["status"] == "active"]
    completed_goals = [g for g in goals.values() if g["status"] == "completed"]
    
    print(f"\n=== Goals ({len(active_goals)} active, {len(completed_goals)} completed) ===")
    
    if active_goals:
        print("\nActive Goals:")
        for goal_id, goal in goals.items():
            if goal["status"] == "active":
                days_left = calculate_days_until(goal["deadline"])
                print(f"\n[{goal_id}] {goal['title']}")
                print(f"  Category: {goal['category']}")
                print(f"  Deadline: {goal['deadline']} ({days_left} days left)")
                print(f"  Description: {goal['description']}")
    
    if completed_goals:
        print("\nCompleted Goals:")
        for goal_id, goal in goals.items():
            if goal["status"] == "completed":
                print(f"\n[{goal_id}] {goal['title']} ✓")
                print(f"  Completed: {goal['completed_date']}")

def complete_goal():
    """Mark goal as completed"""
    goal_id = input("Enter goal ID to mark as complete: ")
    
    if goal_id not in goals:
        print("Goal not found!")
        return
    
    if goals[goal_id]["status"] == "completed":
        print("Goal is already completed!")
        return
    
    goals[goal_id]["status"] = "completed"
    goals[goal_id]["completed_date"] = datetime.date.today().strftime("%Y-%m-%d")
    print(f"Goal '{goals[goal_id]['title']}' marked as completed!")

def update_goal():
    """Update existing goal"""
    goal_id = input("Enter goal ID to update: ")
    
    if goal_id not in goals:
        print("Goal not found!")
        return
    
    print("\nWhat would you like to update?")
    print("1. Title")
    print("2. Description")
    print("3. Deadline")
    print("4. Category")
    
    choice = input("Choose option (1-4): ")
    
    if choice == "1":
        goals[goal_id]["title"] = input("New title: ")
    elif choice == "2":
        goals[goal_id]["description"] = input("New description: ")
    elif choice == "3":
        new_deadline = get_valid_date("New deadline")
        goals[goal_id]["deadline"] = new_deadline.strftime("%Y-%m-%d")
    elif choice == "4":
        goals[goal_id]["category"] = input("New category: ")
    else:
        print("Invalid choice!")
        return
    
    print("Goal updated successfully!")

def delete_goal():
    """Delete a goal"""
    goal_id = input("Enter goal ID to delete: ")
    
    if goal_id not in goals:
        print("Goal not found!")
        return
    
    confirm = input(f"Are you sure you want to delete '{goals[goal_id]['title']}'? (yes/no): ")
    if confirm.lower() == "yes":
        del goals[goal_id]
        print("Goal deleted successfully!")
    else:
        print("Deletion cancelled.")

def goal_progress_report():
    """Generate goal progress report"""
    if not goals:
        print("No goals to report on!")
        return
    
    total_goals = len(goals)
    completed = sum(1 for g in goals.values() if g["status"] == "completed")
    active = total_goals - completed
    
    print("\n=== Goal Progress Report ===")
    print(f"Total Goals: {total_goals}")
    print(f"Completed: {completed} ({completed/total_goals*100:.1f}%)")
    print(f"Active: {active}")
    
    # Check for overdue goals
    overdue = []
    today = datetime.date.today()
    
    for goal_id, goal in goals.items():
        if goal["status"] == "active":
            deadline = datetime.datetime.strptime(goal["deadline"], "%Y-%m-%d").date()
            if deadline < today:
                overdue.append((goal_id, goal["title"], deadline))
    
    if overdue:
        print(f"\nOverdue Goals ({len(overdue)}):")
        for goal_id, title, deadline in overdue:
            days_overdue = (today - deadline).days
            print(f"  [{goal_id}] {title} - {days_overdue} days overdue")
    
    # Category breakdown
    categories = {}
    for goal in goals.values():
        cat = goal["category"]
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\nGoals by Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat.title()}: {count}")

# Expense Management Functions
def add_income():
    """Add income transaction"""
    print("\n=== Add Income ===")
    
    amount = get_valid_number("Income amount: $", min_val=0)
    source = input("Income source: ")
    description = input("Description (optional): ")
    date = datetime.date.today().strftime("%Y-%m-%d")
    
    transaction = {
        "type": "income",
        "amount": amount,
        "category": source,
        "description": description,
        "date": date
    }
    
    expenses.append(transaction)
    print(f"Income of ${amount:.2f} added successfully!")

def add_expense():
    """Add expense transaction"""
    print("\n=== Add Expense ===")
    
    amount = get_valid_number("Expense amount: $", min_val=0)
    category = input("Category (food/transport/utilities/entertainment/other): ")
    description = input("Description: ")
    date = datetime.date.today().strftime("%Y-%m-%d")
    
    transaction = {
        "type": "expense",
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }
    
    expenses.append(transaction)
    print(f"Expense of ${amount:.2f} added successfully!")

def view_transactions():
    """Display all transactions"""
    if not expenses:
        print("No transactions found!")
        return
    
    print(f"\n=== Transactions ({len(expenses)} total) ===")
    
    # Sort by date (most recent first)
    sorted_transactions = sorted(expenses, key=lambda x: x["date"], reverse=True)
    
    for i, trans in enumerate(sorted_transactions[:20]):  # Show last 20
        if trans["type"] == "income":
            print(f"\n+${trans['amount']:.2f} - {trans['category']}")
        else:
            print(f"\n-${trans['amount']:.2f} - {trans['category']}")
        print(f"  {trans['description']}")
        print(f"  Date: {trans['date']}")

def expense_report():
    """Generate expense report"""
    if not expenses:
        print("No transactions to report on!")
        return
    
    print("\n=== Expense Report ===")
    
    total_income = sum(t["amount"] for t in expenses if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in expenses if t["type"] == "expense")
    net_balance = total_income - total_expenses
    
    print(f"Total Income: ${total_income:,.2f}")
    print(f"Total Expenses: ${total_expenses:,.2f}")
    print(f"Net Balance: ${net_balance:,.2f}")
    
    # Expense breakdown by category
    expense_categories = {}
    for trans in expenses:
        if trans["type"] == "expense":
            cat = trans["category"]
            expense_categories[cat] = expense_categories.get(cat, 0) + trans["amount"]
    
    if expense_categories:
        print("\nExpenses by Category:")
        for cat, amount in sorted(expense_categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total_expenses) * 100 if total_expenses > 0 else 0
            print(f"  {cat.title()}: ${amount:.2f} ({percentage:.1f}%)")
    
    # Monthly average
    if expenses:
        # Simple calculation based on date range
        dates = [datetime.datetime.strptime(t["date"], "%Y-%m-%d").date() for t in expenses]
        date_range = (max(dates) - min(dates)).days + 1
        months = max(1, date_range / 30)
        
        print(f"\nMonthly Averages:")
        print(f"  Income: ${total_income/months:.2f}")
        print(f"  Expenses: ${total_expenses/months:.2f}")

def budget_analysis():
    """Analyze spending patterns"""
    if not expenses:
        print("No data for analysis!")
        return
    
    print("\n=== Budget Analysis ===")
    
    # Calculate savings rate
    total_income = sum(t["amount"] for t in expenses if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in expenses if t["type"] == "expense")
    
    if total_income > 0:
        savings_rate = ((total_income - total_expenses) / total_income) * 100
        print(f"Savings Rate: {savings_rate:.1f}%")
        
        if savings_rate < 10:
            print("  ⚠️  Low savings rate - consider reducing expenses")
        elif savings_rate < 20:
            print("  ✓ Good savings rate")
        else:
            print("  ⭐ Excellent savings rate!")
    
    # Find biggest expense categories
    expense_categories = {}
    for trans in expenses:
        if trans["type"] == "expense":
            cat = trans["category"]
            expense_categories[cat] = expense_categories.get(cat, 0) + trans["amount"]
    
    if expense_categories:
        biggest_category = max(expense_categories.items(), key=lambda x: x[1])
        print(f"\nBiggest expense category: {biggest_category[0]} (${biggest_category[1]:.2f})")
        
        # Recommendations
        print("\nRecommendations:")
        if biggest_category[0] == "food":
            print("  • Consider meal planning to reduce food expenses")
        elif biggest_category[0] == "entertainment":
            print("  • Look for free or low-cost entertainment options")
        elif biggest_category[0] == "transport":
            print("  • Consider carpooling or public transportation")

# Skill Management Functions
def add_skill():
    """Add new skill to track"""
    print("\n=== Add New Skill ===")
    
    skill_name = input("Skill name: ")
    
    if skill_name in skills:
        print("Skill already exists!")
        return
    
    proficiency = int(get_valid_number("Current proficiency (1-10): ", min_val=1, max_val=10))
    goal_proficiency = int(get_valid_number("Goal proficiency (1-10): ", min_val=proficiency, max_val=10))
    
    skills[skill_name] = {
        "current_proficiency": proficiency,
        "goal_proficiency": goal_proficiency,
        "practice_hours": 0,
        "last_practiced": None,
        "added_date": datetime.date.today().strftime("%Y-%m-%d")
    }
    
    print(f"Skill '{skill_name}' added successfully!")

def update_proficiency():
    """Update skill proficiency level"""
    if not skills:
        print("No skills to update!")
        return
    
    print("\nAvailable skills:")
    for skill in skills:
        print(f"  - {skill}")
    
    skill_name = input("\nEnter skill name to update: ")
    
    if skill_name not in skills:
        print("Skill not found!")
        return
    
    current = skills[skill_name]["current_proficiency"]
    new_proficiency = int(get_valid_number(f"New proficiency (current: {current}): ", min_val=1, max_val=10))
    
    skills[skill_name]["current_proficiency"] = new_proficiency
    
    if new_proficiency > current:
        print(f"Great progress! Proficiency increased from {current} to {new_proficiency}")
    elif new_proficiency < current:
        print(f"Proficiency updated from {current} to {new_proficiency}")
    else:
        print("Proficiency unchanged")

def log_practice_time():
    """Log time spent practicing a skill"""
    if not skills:
        print("No skills to log time for!")
        return
    
    print("\nAvailable skills:")
    for skill in skills:
        print(f"  - {skill}")
    
    skill_name = input("\nEnter skill name: ")
    
    if skill_name not in skills:
        print("Skill not found!")
        return
    
    hours = get_valid_number("Practice time (hours): ", min_val=0)
    
    skills[skill_name]["practice_hours"] += hours
    skills[skill_name]["last_practiced"] = datetime.date.today().strftime("%Y-%m-%d")
    
    print(f"Logged {hours} hours of practice for {skill_name}")
    print(f"Total practice time: {skills[skill_name]['practice_hours']} hours")

def view_skills():
    """Display all skills and progress"""
    if not skills:
        print("No skills tracked yet!")
        return
    
    print(f"\n=== Skills Overview ({len(skills)} total) ===")
    
    for skill_name, skill_data in sorted(skills.items()):
        current = skill_data["current_proficiency"]
        goal = skill_data["goal_proficiency"]
        hours = skill_data["practice_hours"]
        
        print(f"\n{skill_name}")
        print(f"  Proficiency: {current}/10 (Goal: {goal}/10)")
        print(f"  Progress: {'▓' * current}{'░' * (10 - current)}")
        print(f"  Practice time: {hours} hours")
        
        if skill_data["last_practiced"]:
            print(f"  Last practiced: {skill_data['last_practiced']}")
        
        if current >= goal:
            print("  ⭐ Goal achieved!")

def skills_progress_report():
    """Generate skills progress report"""
    if not skills:
        print("No skills to report on!")
        return
    
    print("\n=== Skills Progress Report ===")
    
    total_skills = len(skills)
    total_hours = sum(s["practice_hours"] for s in skills.values())
    goals_met = sum(1 for s in skills.values() if s["current_proficiency"] >= s["goal_proficiency"])
    
    print(f"Total Skills: {total_skills}")
    print(f"Total Practice Time: {total_hours} hours")
    print(f"Goals Achieved: {goals_met}/{total_skills}")
    
    # Average proficiency
    avg_proficiency = sum(s["current_proficiency"] for s in skills.values()) / total_skills
    print(f"Average Proficiency: {avg_proficiency:.1f}/10")
    
    # Most practiced skill
    if total_hours > 0:
        most_practiced = max(skills.items(), key=lambda x: x[1]["practice_hours"])
        print(f"\nMost Practiced: {most_practiced[0]} ({most_practiced[1]['practice_hours']} hours)")
    
    # Skills needing attention
    print("\nSkills Needing Practice:")
    for skill_name, skill_data in skills.items():
        if skill_data["current_proficiency"] < skill_data["goal_proficiency"]:
            gap = skill_data["goal_proficiency"] - skill_data["current_proficiency"]
            print(f"  - {skill_name} (need +{gap} proficiency)")

# Analytics and Data Management Functions
def analytics_dashboard():
    """Generate comprehensive analytics"""
    print("\n=== Analytics Dashboard ===")
    
    if user_profile:
        print(f"User: {user_profile.get('name', 'Unknown')}")
        print(f"Member since: {user_profile.get('created_date', 'Unknown')}")
    
    print(f"\nData Summary:")
    print(f"  Contacts: {len(contacts)}")
    print(f"  Goals: {len(goals)}")
    print(f"  Transactions: {len(expenses)}")
    print(f"  Skills: {len(skills)}")
    
    # Financial summary
    if expenses:
        total_income = sum(t["amount"] for t in expenses if t["type"] == "income")
        total_expenses = sum(t["amount"] for t in expenses if t["type"] == "expense")
        print(f"\nFinancial Summary:")
        print(f"  Net Worth: ${total_income - total_expenses:,.2f}")
    
    # Goal completion rate
    if goals:
        completed = sum(1 for g in goals.values() if g["status"] == "completed")
        completion_rate = (completed / len(goals)) * 100
        print(f"\nGoal Completion Rate: {completion_rate:.1f}%")
    
    # Skill progress
    if skills:
        avg_proficiency = sum(s["current_proficiency"] for s in skills.values()) / len(skills)
        print(f"\nAverage Skill Level: {avg_proficiency:.1f}/10")
    
    # Activity insights
    print("\nActivity Insights:")
    if goals:
        active_goals = sum(1 for g in goals.values() if g["status"] == "active")
        print(f"  • You have {active_goals} active goals")
    
    if skills:
        total_practice = sum(s["practice_hours"] for s in skills.values())
        print(f"  • You've practiced skills for {total_practice} hours total")

def export_data():
    """Export data to text format"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"personal_data_export_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        f.write("=== Personal Data Manager Export ===\n")
        f.write(f"Export Date: {datetime.datetime.now()}\n\n")
        
        # Profile
        if user_profile:
            f.write("PROFILE:\n")
            for key, value in user_profile.items():
                f.write(f"  {key}: {value}\n")
            f.write("\n")
        
        # Contacts
        if contacts:
            f.write(f"CONTACTS ({len(contacts)} total):\n")
            for name, contact in sorted(contacts.items()):
                f.write(f"  {name}: {contact['phone']}, {contact['email']}\n")
            f.write("\n")
        
        # Goals
        if goals:
            f.write(f"GOALS ({len(goals)} total):\n")
            for goal_id, goal in goals.items():
                f.write(f"  [{goal_id}] {goal['title']} - {goal['status']}\n")
            f.write("\n")
        
        # Financial Summary
        if expenses:
            total_income = sum(t["amount"] for t in expenses if t["type"] == "income")
            total_expenses = sum(t["amount"] for t in expenses if t["type"] == "expense")
            f.write("FINANCIAL SUMMARY:\n")
            f.write(f"  Total Income: ${total_income:.2f}\n")
            f.write(f"  Total Expenses: ${total_expenses:.2f}\n")
            f.write(f"  Net Balance: ${total_income - total_expenses:.2f}\n\n")
        
        # Skills
        if skills:
            f.write(f"SKILLS ({len(skills)} total):\n")
            for skill, data in skills.items():
                f.write(f"  {skill}: {data['current_proficiency']}/10\n")
    
    print(f"Data exported to {filename}")

def backup_data():
    """Create backup of all data"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # In a real application, this would save to a database or JSON file
    print(f"Backup created at {timestamp}")
    print("Backup includes:")
    print(f"  - Profile data")
    print(f"  - {len(contacts)} contacts")
    print(f"  - {len(goals)} goals")
    print(f"  - {len(expenses)} transactions")
    print(f"  - {len(skills)} skills")

def clear_all_data():
    """Clear all data (with confirmation)"""
    print("\n⚠️  WARNING: This will delete ALL your data!")
    confirm = input("Type 'DELETE ALL' to confirm: ")
    
    if confirm == "DELETE ALL":
        global user_profile, contacts, goals, expenses, skills
        user_profile = {}
        contacts = {}
        goals = {}
        expenses = []
        skills = {}
        print("All data has been cleared.")
    else:
        print("Data clearing cancelled.")

def summary_report():
    """Generate comprehensive summary report"""
    print("\n=== Summary Report ===")
    print(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    if user_profile:
        print(f"\nUser: {user_profile.get('name', 'Unknown')}")
    
    # Quick stats
    print("\nQuick Statistics:")
    print(f"  • Contacts: {len(contacts)}")
    print(f"  • Active Goals: {sum(1 for g in goals.values() if g['status'] == 'active')}")
    print(f"  • Completed Goals: {sum(1 for g in goals.values() if g['status'] == 'completed')}")
    print(f"  • Total Transactions: {len(expenses)}")
    print(f"  • Skills Tracked: {len(skills)}")
    
    # Financial position
    if expenses:
        total_income = sum(t["amount"] for t in expenses if t["type"] == "income")
        total_expenses = sum(t["amount"] for t in expenses if t["type"] == "expense")
        net = total_income - total_expenses
        
        print(f"\nFinancial Position:")
        print(f"  • Net Balance: ${net:,.2f}")
        
        if net > 0:
            print("  • Status: Positive cash flow ✓")
        else:
            print("  • Status: Negative cash flow ⚠️")
    
    # Top achievements
    print("\nRecent Achievements:")
    completed_goals = [(gid, g) for gid, g in goals.items() if g["status"] == "completed"]
    if completed_goals:
        recent = sorted(completed_goals, key=lambda x: x[1]["completed_date"], reverse=True)[:3]
        for goal_id, goal in recent:
            print(f"  • Completed: {goal['title']}")
    
    # Areas for improvement
    print("\nAreas for Focus:")
    
    # Overdue goals
    overdue_count = 0
    today = datetime.date.today()
    for goal in goals.values():
        if goal["status"] == "active":
            deadline = datetime.datetime.strptime(goal["deadline"], "%Y-%m-%d").date()
            if deadline < today:
                overdue_count += 1
    
    if overdue_count > 0:
        print(f"  • {overdue_count} overdue goals need attention")
    
    # Skills below target
    skills_below_target = sum(1 for s in skills.values() 
                             if s["current_proficiency"] < s["goal_proficiency"])
    if skills_below_target > 0:
        print(f"  • {skills_below_target} skills need more practice")

# Menu Management Functions
def manage_contacts():
    """Contact management system"""
    while True:
        print("\n=== Contact Management ===")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Back to main menu")
        
        choice = input("Choose option (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

def manage_goals():
    """Goal tracking system"""
    while True:
        print("\n=== Goal Management ===")
        print("1. Add goal")
        print("2. View goals")
        print("3. Mark goal complete")
        print("4. Update goal")
        print("5. Delete goal")
        print("6. Goal progress report")
        print("7. Back to main menu")
        
        choice = input("Choose option (1-7): ")
        
        if choice == "1":
            add_goal()
        elif choice == "2":
            view_goals()
        elif choice == "3":
            complete_goal()
        elif choice == "4":
            update_goal()
        elif choice == "5":
            delete_goal()
        elif choice == "6":
            goal_progress_report()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

def manage_expenses():
    """Expense tracking system"""
    while True:
        print("\n=== Expense Management ===")
        print("1. Add income")
        print("2. Add expense")
        print("3. View transactions")
        print("4. Expense report")
        print("5. Budget analysis")
        print("6. Back to main menu")
        
        choice = input("Choose option (1-6): ")
        
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            expense_report()
        elif choice == "5":
            budget_analysis()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

def manage_skills():
    """Learning progress tracking"""
    while True:
        print("\n=== Skill Management ===")
        print("1. Add skill")
        print("2. Update proficiency")
        print("3. Log practice time")
        print("4. View skills")
        print("5. Progress report")
        print("6. Back to main menu")
        
        choice = input("Choose option (1-6): ")
        
        if choice == "1":
            add_skill()
        elif choice == "2":
            update_proficiency()
        elif choice == "3":
            log_practice_time()
        elif choice == "4":
            view_skills()
        elif choice == "5":
            skills_progress_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")

def data_management():
    """Data import/export functionality"""
    while True:
        print("\n=== Data Management ===")
        print("1. Export all data")
        print("2. Backup data")
        print("3. Clear all data")
        print("4. Generate summary report")
        print("5. Back to main menu")
        
        choice = input("Choose option (1-5): ")
        
        if choice == "1":
            export_data()
        elif choice == "2":
            backup_data()
        elif choice == "3":
            clear_all_data()
        elif choice == "4":
            summary_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

# Helper Functions
def get_valid_number(prompt, min_val=None, max_val=None):
    """Get valid number input from user"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")

def get_valid_date(prompt):
    """Get valid date input from user"""
    while True:
        date_str = input(prompt + " (YYYY-MM-DD): ")
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return date_obj
        except ValueError:
            print("Please use YYYY-MM-DD format!")

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

def calculate_days_until(target_date):
    """Calculate days until target date"""
    if isinstance(target_date, str):
        target_date = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
    
    today = datetime.date.today()
    delta = target_date - today
    return delta.days

def main_menu():
    """Main application menu"""
    display_welcome()
    
    # Check if profile exists, if not, set it up
    if not user_profile:
        print("Let's start by setting up your profile!")
        setup_profile()
    
    while True:
        print("\n" + "=" * 30)
        print("MAIN MENU")
        print("=" * 30)
        print("1. View Profile")
        print("2. Manage Contacts")
        print("3. Manage Goals")
        print("4. Manage Expenses")
        print("5. Manage Skills")
        print("6. Analytics Dashboard")
        print("7. Data Management")
        print("8. Update Profile")
        print("9. Exit")
        
        choice = input("Choose option (1-9): ")
        
        if choice == "1":
            display_profile()
        elif choice == "2":
            manage_contacts()
        elif choice == "3":
            manage_goals()
        elif choice == "4":
            manage_expenses()
        elif choice == "5":
            manage_skills()
        elif choice == "6":
            analytics_dashboard()
        elif choice == "7":
            data_management()
        elif choice == "8":
            setup_profile()
        elif choice == "9":
            print("\nThank you for using Personal Data Manager!")
            print("Your data has been saved for this session.")
            break
        else:
            print("Invalid choice! Please enter 1-9.")

# Run the application
if __name__ == "__main__":
    # Initialize with some demo data for testing
    demo_mode = input("Run in demo mode with sample data? (yes/no): ").lower() == "yes"
    
    if demo_mode:
        # Add demo profile
        user_profile = {
            "name": "Demo User",
            "age": 25,
            "location": "San Francisco, CA",
            "email": "demo@example.com",
            "phone": "555-0000",
            "occupation": "Software Developer",
            "interests": ["Programming", "Reading", "Hiking"],
            "created_date": "2024-01-01"
        }
        
        # Add demo contacts
        contacts["John Doe"] = {
            "phone": "555-1234",
            "email": "john@example.com",
            "address": "123 Main St",
            "birthday": "1990-05-15",
            "added_date": "2024-01-05"
        }
        
        # Add demo goals
        goals["G001"] = {
            "title": "Learn Python",
            "description": "Complete Python course",
            "category": "career",
            "deadline": "2024-12-31",
            "status": "active",
            "created_date": "2024-01-01",
            "completed_date": None
        }
        
        # Add demo expenses
        expenses.extend([
            {"type": "income", "amount": 5000, "category": "salary", "description": "Monthly salary", "date": "2024-01-01"},
            {"type": "expense", "amount": 1200, "category": "rent", "description": "Monthly rent", "date": "2024-01-05"},
            {"type": "expense", "amount": 300, "category": "food", "description": "Groceries", "date": "2024-01-10"}
        ])
        
        # Add demo skills
        skills["Python"] = {
            "current_proficiency": 7,
            "goal_proficiency": 10,
            "practice_hours": 50,
            "last_practiced": "2024-01-15",
            "added_date": "2024-01-01"
        }
        
        print("\nDemo data loaded successfully!")
    
    main_menu()

print()
print("=== Day 7 Integration Project Complete! ===")

"""
Teaching Notes for Mentors:
===========================

Key Integration Concepts:
1. Combining all Week 1 concepts
2. Data persistence in memory
3. User interface design
4. Input validation
5. Error handling
6. Data relationships
7. Report generation

Project Features Demonstrated:
- Modular function design
- Menu-driven interface
- Data validation
- Complex data structures
- File I/O operations
- Date/time handling
- Statistical calculations

Common Student Challenges:
1. Managing global state
2. Preventing data loss
3. Handling edge cases
4. Creating intuitive UI
5. Balancing features vs complexity

Assessment Criteria:
- Code organization
- Feature completeness
- Error handling
- User experience
- Code readability
- Creative additions

Extension Ideas:
- Data persistence to files
- Data visualization
- Web interface
- Mobile app
- Cloud sync
- Multi-user support
"""