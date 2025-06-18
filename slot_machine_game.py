import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

# slot machine spin function
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    # creating a single symbols list and append all the values in symbol_count variable to it
    for symbol, symbol_count in symbols:
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # adding values to grid
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

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

