# https://youtu.be/th4OBktqK1I?si=M_0IxvBlsNJR0FBj
# Enter a deposit
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        try:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more than 0.")
        except ValueError:
            print("Please enter a valid number.")

    return amount

amount = deposit()

# Cotinue with the gae logic once balance is >0
print(f"Your balance is ${amount}. Let's play!")