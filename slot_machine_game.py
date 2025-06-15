MAX_LINES = 4
MIN_BET = 1
MAX_BET = 100

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

# Betting function
def get_bet():
    while True:
        bet = input(f"Enter an amount to bet (${MIN_BET} - ${MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a valid amount to bet. Bet must be ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a valid number!")
    
    return bet

# main game logic
def game():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough money to bet. Remaining balance is {balance}!")
        else:
            break

    print(f"You're betting ${bet} in {lines} lines. Total bet is ${total_bet}")

game()

