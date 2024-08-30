# https://youtu.be/th4OBktqK1I?si=M_0IxvBlsNJR0FBj
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
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

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i !=len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more than 0.")
        else:
            print("Please enter a valid number.")

    return amount

def get_no_of_lines():

    while True:
        lines = input("How many lines would you like to bet on? (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return amount

def main():
    #Get deposit amount  from user
    balance = deposit()
    # Print balance and proceed to game
    #print(f"Your balance is ${deposit}. Let's play!")
    # Get number of lines to bet on
    lines = get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
    
        if total_bet > balance:
            print(f"You do not have enough funds, your current balance is ${balance}")
        else:
            break #could add option to increase balance/add funds here

    print(f"You are betting ${bet} on {lines} lines. You are betting ${total_bet} in this game")
    #Continue with the game logic

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
