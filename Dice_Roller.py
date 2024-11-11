from random import randint

print("Welcome to the simple dice roller")

while True:
            dice: int = int(input("How many dice would you like to roll? "))
            roll: str = input("Press ENTER to roll or 'E' to exit ").lower() # pauses the loop
            if roll == "e":
                exit()
            else:
                value: list[int] = [randint(1, 6) for _ in range(dice)] # range(number of dice) rolls -> int value 1-6
                print(value)


