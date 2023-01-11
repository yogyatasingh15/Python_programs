import random

rand_num = random.randint(1,50)
for i in range(10):
    print("Guess the number: ")
    num = input("enter the number \t")
    if int(num) < rand_num:
        print("You are Wrong. Number is greater than your choice")
    elif int(num) > rand_num:
        print("You are Wrong. Number is lesser than your choice")
    elif int(num) == rand_num:
        print("You Won the Game You guess the correct number")