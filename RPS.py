import random


def beans():
    user_wins = 0
    computer_wins = 0
    while True:
        rps = ["R", "P", "S"]
        computer = random.choice(rps)
        user = input("Rock paper Scissors First to 10 wins!: Enter: R, P or S ")
        if user == "rock" or "paper" or "scissors":
            print(f"{user} vs {computer}")
        if user == "R" and computer == "P":
            print("Computer won!")
            computer_wins += 1
            print(f"Wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
        if user == "R" and computer == "S":
            print("You win!")
            user_wins+=1
            print(f"Wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
        if user == "R" and computer == "R":
            print("It's a tie")
        if user == "P" and computer == "R":
            print("You win!")
            user_wins += 1
            print(f"Wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
        if user == "P" and computer == "S":
            print("Computer won!")
            computer_wins += 1
            print(f"Wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
        if user == "P" and computer == "P":
            print("It's a tie")
        if user == "S" and computer == "R":
            print("Computer won!")
            computer_wins += 1
            print(f"Wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
        if user == "S" and computer == "P":
            print("You Win!")
            user_wins += 1
            print(f"Wins: {user_wins}")
            print(f"Computer wins: {computer_wins}")
        if user == "S" and computer == "S":
            print("It's a tie")
        if user_wins == 10:
            print("YOU ARE THE CHAMPION!")
            quit()
        if computer_wins == 10:
            print("'YOU ARE A LOSER!")

        # if user != "rock" or "paper" or "scissors":
        #     print("That is not an option!")

    # def validity(self):
    #     if user != "rock" or "paper" or "scissors":
    #         print("That is not an option!")


beans()

