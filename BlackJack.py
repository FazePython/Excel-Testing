import random
vals = [2, 3, 4, 5, 6, 7, 8, 9]
face = ['J', 'Q', 'K', 'A']
all = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K','A']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
# vals[8] = 10
# vals[9] = 10
# vals[10] = 10
# vals[11] = 11
computer = random.choice(all)
computer2 = random.choice(all)
def dealer():
    for row in all:
        computer2 = 'X'
    print(f"Dealer has {computer} {computer2}")
    # total = 0
    # for num in all:
    #     if num == 'J' or 'Q' or 'K':
    #         t += 10
    #     if num == 'A':
    #         t += 11



    # total =  + t

    computer2 = random.choice(all)
    if computer and computer2 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        
        total = computer + computer2
    if computer and computer2 == 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 'J' or 'Q' or 'K' or'A':
        if computer and computer2 == 'J' or 'Q' or 'K':
            total+= 10
        # total = t
    print(f"{computer} {computer2} for a total of {total}")
    # print(total)


dealer()
# print(f"{random.choice(vals)} {random.choice(suits)}")


# print(five, __hidden)

# for poin
# score = val[i]

# computer = str(random.choice(vals)) + random.choice(suits)
# player = str(random.choice(vals)) + random.choice(suits)

# print(computer)
# print(player)

