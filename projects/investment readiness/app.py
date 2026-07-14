from service import *
from database import users
from menu import *


if __name__ == "__main__":

    home_menu()

    choice = int(input("Enter Choice : "))

    if choice == 1:

        name = input("Enter Name : ")
        email = input("Enter Email : ")
        password = int(input("Create Password : "))

        print(Register(
            name=name,
            email=email,
            password=password
        ))

    elif choice == 2:

        account = int(input("Enter Account Number : "))
        password = int(input("Enter Password : "))

        login_val = login(
            account=account,
            password=password
        )

        if not login_val:
            print("Invalid Account Number or Password.")

        while login_val:

            service_menu()

            choice = int(input("Enter Choice : "))

            if choice == 1:

                income = int(input("Enter Monthly Income : "))

                print(add_income(
                    account=account,
                    income=income
                ))

            elif choice == 2:

                expense = int(input("Enter Expense Amount : "))

                print(add_expenses(
                    account=account,
                    expense=expense
                ))

            elif choice == 3:

                print(f"""
Cash Flow

Income : ₹{users[account]['income']}
Expenses : ₹{users[account]['expenses']}
Cash Flow : ₹{cashflow(account)}
""")

            elif choice == 4:

                print(investment_readiness(account))

            elif choice == 5:

                print(logout())
                break

            else:

                print("Invalid Choice.")