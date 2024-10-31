def main():
    coke_machine()


def coke_machine():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        coins = int(input("Insert coins: "))

        if coins not in (25,10,5):
            continue

        amount -= coins
    print(f"Change Owed: {amount * (-1)}")

if __name__ == "__main__":
    main()
