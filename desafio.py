menu = """
    d - deposit
    w - withdraw
    c - check balance
    q - quit

"""

balance = 0
limit = 500
history = ""
whithdraws = 0
WHITHDRAW_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        deposit = int(input("How much do you want to deposit? "))
        balance += deposit
        print(f"Your balance is {balance:.2f}")

    if option == "w":
        value = float(input("Withdraw value? "))

        over_balance = value > balance
        over_limit = value > limit
        over_quantity = whithdraws > WHITHDRAW_LIMIT

        if over_balance or over_limit or over_quantity:
            print("You can't withdraw, not enough money")
            continue
        else:
            balance -= value
            whithdraws += 1
            print(f"Your balance is {balance:.2f}")

    if option == "c":
        print(f"Your balance is {balance:.2f}")
    
    if option == "q":
        print(f"Your balance is {balance:.2f}")
        print(history)
        break
