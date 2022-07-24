import random

(words1) = ["fruit", "bird", "ball", "car", "plane", "helicopter", "table", "game", "glide"]
secretword = random.choice(words1)
letters_guessed =""

failure_count = 6

while failure_count > 0:
    guess = input("Enter a letter")

    if guess in secretword:
        print(f"Correct! There is one or more {guess} in the secret word.")
    else:
        failure_count+= 1
        print(f"Incorrect, There are no {guess} in the secret word. {failure_count} turns left.")

    letters_guessed = letters_guessed + guess
    wrongLetterCount = 0
    for letter in secretword:
        if letter in letters_guessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    if wrongLetterCount == 0:
        print(f"Congrats! the secret word was: {secretword}. You won!")
        break








                                                                # secretword = random.choice(words1)




















                                                            # guess = input("What word am I thinking of?: ")
# i = 0
# while i < 3:
#     guess = input(f"What word am I thinking of?: from this list {words1}")
#     if guess == secretword:
#         print("You've won")
#         exit()
#         i+=1
    # while guess != secretword and i < 3:
    #     attempt = input(("Try again: "))
    #     if attempt == secretword:
    #         print("You've won")
    #         exit()
    #     i+=1
# print("You've lost")
#
