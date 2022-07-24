def challenge1():
    # seperate out even and odd numbers

    list = [2, 4, 5, 7, 15, 3, 18, 20, 30, 35, 33]
    even = []
    odd = []

    for i in list:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even: {even}")
    print(f"Odd: {odd}")

def challenge2():
#     Find the sum of all numbers in a list
    list = [20, 5, 7, 17, 9, 20, 35]
    num_sum = 0
    for i in list:
        num_sum += i
    print(num_sum)


def challenge3():
#     Find the sum of all even numbers in a list
    list = [2, 4, 5, 7, 15, 3, 18, 20, 30, 35, 33]
    even =[]
    for i in list:
        if i%2 ==0:
            even.append(i)
    print(even)
    num_sum = 0
    for i in even:
        num_sum+= i
    print(num_sum)


def challenge4():
#     Count the number of even numbers in list
    even = [2, 4, 18, 20, 30]

    count = 0
    for i in range(len(even)):
        count+= 1
    print(count)

# challenge1()
# challenge2()
# challenge3()
challenge4()


