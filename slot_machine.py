import random

MAX_LINE = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3
symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def winner_check(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol != symbol_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines


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
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("Enter the amount $")
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Enter amount greater then 0")
        else:
            print("Please enter a valid number")
    return amount


def number_of_bets():
    while True:
        lines = input(f"Enter the line of bet between 1 to {MAX_LINE}: ")
        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter amount greater then 0")
        else:
            print("Please enter a valid number")
    return lines


def get_bet():
    while True:
        amount = input("Enter the amount of bet on each line $")
        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Enter amount greater then 0")
        else:
            print("Please enter a valid number")
    return amount


def spin(balance):
    lines_of_bet = number_of_bets()
    while True:
        bet = get_bet()
        total_bet = lines_of_bet * bet
        if total_bet > balance:
            print(
                f"You do not have enough to bet that. Your current balance is ${balance}"
            )
        else:
            break
    print(
        f"You are betting ${bet} on {lines_of_bet} lines. Total bet is equal to:${total_bet}"
    )

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winning, winning_lines = winner_check(slot, lines_of_bet, bet, symbol_value)
    print(f"You won ${winning}.")
    print(f"You won on lines:", *winning_lines)

    return winning - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press enter to start or (q) to quit: ")
        if answer.lower() == "q":
            break
        balance += spin(balance)
    print(f"Your current balance is ${balance}")


main()
