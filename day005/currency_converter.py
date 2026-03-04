
def ngn_to_usd(amount, rate=0.00067):
    """Convert Nigerian Naira to US Dollars."""
    return amount * rate

def usd_to_ngn(amount, rate=1500):
    """Convert US Dollars to Nigerian Naira."""
    return amount * rate

def ngn_to_cfa(amount, rate=0.92):
    """Convert Naira to CFA Franc."""
    return amount * rate


print("💰 Currency Converter")
print("1. NGN to USD")
print("2. USD to NGN")
print("3. NGN to CFA")
choice = input("Choose an option (1/2/3): ")

amount = float(input("Enter amount: "))

if choice == '1':
    result = ngn_to_usd(amount)
    print(f"{amount} NGN = {result:.2f} USD")
elif choice == '2':
    result = usd_to_ngn(amount)
    print(f"{amount} USD = {result:.2f} NGN")
elif choice == '3':
    result = ngn_to_cfa(amount)
    print(f"{amount} NGN = {result:.2f} CFA")
else:
    print("Invalid option")
