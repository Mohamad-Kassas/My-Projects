import numpy as np
import random


def decimal_check(a):
    test = (a - int(a))
    return test


def difficulty():
    global x
    print("Enter the first letter of your selection (B,E,M,H,I)")
    print("Max number: Beginner:25/Easy:50/Medium:100/Hard:500/Insane:1000")
    selection = str(input("Select the difficulty you want: Beginner/Easy/Medium/Hard/Insane ")).upper()
    if selection == "B":
        x = 25
    elif selection == "E":
        x = 50
    elif selection == "M":
        x = 100
    elif selection == "H":
        x = 500
    elif selection == "I":
        x = 1000
    return x


def guess_the_number(x):
    range = np.arange(1, x)
    num = random.choice(range)
    print("Can you guess what is the mysterious number?")
    while True:
        try:
            guess = float(input("Enter your guess: "))
            break
        except ValueError:
            print("Invalid input. Try again")
    while guess != num:
        if guess > num:
            print("Your guess is too high")
            division = guess % num
            if division != 0:
                div2 = guess / division
                div3 = num / division
            if division == 0:
                print("But your guess can be divided by the mysterious number")
            elif decimal_check(div2) == 0 and decimal_check(div3) == 0:
                print("But your guess and the mysterious number can be divided by", division)
            elif decimal_check(num / 2) == 0:
                print("But the mysterious number can be divided by 2")
        if guess < num:
            print("Your guess is too low")
            multiple = num % guess
            if multiple == 0:
                print("But the mysterious number is a multiple of your guess")
            elif decimal_check(num / 3) == 0:
                print("But the mysterious number can be divided by 3")
        while True:
            try:
                guess = float(input("Enter you guess: "))
                break
            except ValueError:
                print("Invalid input. Try again")
    print("You guessed right! The mysterious number was", num)


difficulty()
guess_the_number(x)
