# Function to calculate cable bill
def calculate_bill(account_number, customer_type, premium_channels, basic_connections=0):
    # Rates for Residential customers
    if customer_type in ['R', 'r']:
        bill = 4.50 + 20.50 + (7.50 * premium_channels)

    # Rates for Business customers
    elif customer_type in ['B', 'b']:
        if basic_connections <= 10:
            basic_fee = 75.00
        else:
            basic_fee = 75.00 + (5.00 * (basic_connections - 10))
        
        bill = 15.00 + basic_fee + (50.00 * premium_channels)
        
        

    return bill

# Main Program
print("__________CABLE BILL CALCULATOR__________\n")
print("This program computes a cable bill.")
try:
    
    account_number = int(input("Enter account number (an integer): "))
except: print("Invalid input. Please enter valid  accountnumber or customer type!.")
    
customer_type = input("Enter customer type (R/r for Residential, B/b for Business): ")
premium_channels = int(input("Enter the number of premium channels: "))

# For business customers, ask for number of basic connections
if customer_type in ['B', 'b']:
    basic_connections = int(input("Enter the number of basic service connections: "))
else:
    basic_connections = 0  # Default for residential customers

# Calculate the bill
total_bill = calculate_bill(account_number, customer_type, premium_channels, basic_connections)

# Display the results
print("__________Your Information__________\n")

print("______________________________________")
print(f"\nCustomer's account number: {account_number}")
print(f"Billing amount: ¢{total_bill:.2f}")
print("______________________________________\n")
