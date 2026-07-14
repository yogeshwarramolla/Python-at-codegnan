from database import users


def Register(name: str, email: str, password: int):

    account = max(users.keys()) + 1

    users[account] = {
        "name": name,
        "email": email,
        "password": password,
        "income": 0,
        "expenses": 0
    }

    return f"""
Registration Successful

Account Number : {account}
Name : {name}
Email : {email}
"""


def login(account: int, password: int):

    if account in users:
        if password == users[account]["password"]:
            return True

    return False


def add_income(account: int, income: int):

    if income <= 0:
        return "Income should be greater than 0."

    users[account]["income"] = income

    return f"""
Income Updated Successfully

Monthly Income : ₹{income}
"""


def add_expenses(account: int, expense: int):

    if expense <= 0:
        return "Expense should be greater than 0."

    users[account]["expenses"] += expense

    return f"""
Expense Added Successfully

Total Expenses : ₹{users[account]['expenses']}
"""


def cashflow(account: int):

    income = users[account]["income"]
    expenses = users[account]["expenses"]

    return income - expenses


def investment_readiness(account: int):

    balance = cashflow(account)

    if balance >= 10000:

        return f"""
Investment Status : Ready to Invest

Monthly Surplus : ₹{balance}
"""

    elif balance >= 5000:

        return f"""
Investment Status : Can Start Small SIP

Monthly Surplus : ₹{balance}
"""

    else:

        return f"""
Investment Status : Not Ready

Monthly Surplus : ₹{balance}

Suggestion : Reduce your monthly expenses.
"""


def logout():

    return "Thank you. Visit Again."