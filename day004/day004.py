contacts = {
    "Abraham": "0803-123-4567",
    "Thlama": "0701-987-6543",
    "Nkeki": "0902-555-7890"
}

print("Welcome to the phonebook.")

name = input("Enter a name to look up: ").title()  
number = contacts.get(name)
if number:
    print(f"{name}'s number is {number}")
else:
    print(f"Sorry, no contact found for {name}.")
