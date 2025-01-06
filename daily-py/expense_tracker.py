def display_menu():
    print("""
Welcome to Expense Tracker!
1. Add an Expense
2. View all expenses
3. Search expenses by date
4. Calculate total spending
5. Exit
""")


def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, description, amount = line.strip().split(", ")
                expenses.append(
                    {
                        "date": date,
                        "category": category,
                        "description": description,
                        "amount": float(amount),
                    }
                )
    except FileNotFoundError:
        print("Expenses file not found, starting fresh.")
    return expenses


def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter the amount: "))

    expenses.append(
        {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }
    )

    with open("expenses.txt", "a") as file:
        file.write(f"{date}, {category}, {description}, {amount}\n")

    print("Expense added successfully!")


def view_expenses(expenses):
    print("---All Expenses---")
    print(f"{'Date':<15} | {'Category':<15} | {'Description':<20} | {'Amount':<10}")
    print("-" * 65)
    for expense in expenses:
        print(
            f"{expense['date']:<15} | {expense['category']:<15} | {expense['description']:<20} | ${expense['amount']:<10.2f}"
        )


def search_expenses_by_date(expenses):
    search_date = input("Enter date (YYYY-MM-DD): ")
    found = False
    print("---Expenses Found---")
    print(f"{'Date':<15} | {'Category':<15} | {'Description':<20} | {'Amount':<10}")
    print("-" * 65)
    for expense in expenses:
        if expense["date"] == search_date:
            print(
                f"{expense['date']:<15} | {expense['category']:<15} | {expense['description']:<20} | ${expense['amount']:<10.2f}"
            )
            found = True
    if not found:
        print("No expenses found for that date.")


def calculate_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ${total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            search_expenses_by_date(expenses)
        elif choice == "4":
            calculate_total(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
