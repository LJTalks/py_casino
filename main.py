# https://youtu.be/th4OBktqK1I?si=M_0IxvBlsNJR0FBj
# Enter a deposit
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
        lines = input("How much would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return lines

def main():
    #Get deposit amount  from user
    balance = deposit()
    # Print balance and proceed to game
    print(f"Your balance is ${deposit}. Let's play!")
    # Get number of lines to bet on
    lines = get_no_of_lines()
    #How much they want to bet
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. You are betting ${total_bet} in this game")
    #Continue with the game logic


main()
