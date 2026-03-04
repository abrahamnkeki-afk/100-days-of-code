debts = []

def add_debt(lender, borrower, amount):
    """Record a new debt."""
    debts.append({'lender': lender, 'borrower': borrower, 'amount': amount})
    print(f"Debt recorded: {borrower} owes {lender} ₦{amount}")

def repay_debt(lender, borrower, amount):
    """Reduce or clear a debt."""
    for debt in debts:
        if debt['lender'] == lender and debt['borrower'] == borrower:
            if debt['amount'] >= amount:
                debt['amount'] -= amount
                print(f"{borrower} repaid ₦{amount} to {lender}")
                if debt['amount'] == 0:
                    debts.remove(debt)
                    print("Debt cleared!")
                return
            else:
                print(f"Error: {borrower} only owes ₦{debt['amount']}")
                return
    print("No such debt found.")

def show_all_debts():
    """Display all current debts."""
    if not debts:
        print("No debts recorded.")
        return
    print("\n--- Current Debts ---")
    for d in debts:
        print(f"{d['borrower']} owes {d['lender']} ₦{d['amount']}")

while True:
    print("\n📋 Borrow-Lend Tracker")
    print("1. Add debt")
    print("2. Repay debt")
    print("3. Show all debts")
    print("4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        lender = input("Lender's name: ")
        borrower = input("Borrower's name: ")
        amount = float(input("Amount (₦): "))
        add_debt(lender, borrower, amount)
    elif choice == '2':
        lender = input("Lender's name: ")
        borrower = input("Borrower's name: ")
        amount = float(input("Amount repaid (₦): "))
        repay_debt(lender, borrower, amount)
    elif choice == '3':
        show_all_debts()
    elif choice == '4':
        print("Bye!")
        break
    else:
        print("Invalid choice")
