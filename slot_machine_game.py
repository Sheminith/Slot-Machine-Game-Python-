MAX_LINES = 4

# Deposit money function
def deposit():
    while True:
        amount = input("Enter an amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. Try again!")
        else:
            print("Enter a valid number!")

    return amount

# Get number of lines from user, function
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a valid number!")
    
    return lines

