from random import randint



#     type in Bank to see how much you have
# type in record for W/L
print("Welcome to the Wager game! (Type help for all the commands)")
help = ["Bank", "Play", "Record"]
money = 500
user = input("....")
if user == "help":
    print(help)
dice = randint(1,6)
dice2 = randint(1,6)


def Game():
    for command in help:
        input("...")
        if command == "Bank":
            print(f"You have {money} coins")
        if command == "Play":
            print("You have to roll a dice whoever has the higher number wins!")
            wager = int(input("How many coins would you like to wager?"))
            if wager > money:
                print(f"You don't have enough coins, you currently have {money} coins")
                print('How much would you like to wager?')
            if wager <= money:
                print(f"You have wagered {wager} coins")
                roll = input("Type '1' to roll")
                if roll == '1':
                    print(f"You rolled a {dice}")
                    print(f"Computer rolled a {dice2}")
                else:
                    print("Not a valid command")
def wager_system():
    # make it ask how much you want to wager
    # user enters
    pass



Game()


