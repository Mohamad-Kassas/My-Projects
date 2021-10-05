import string, random


def generate_password(len):
    special = str(input("Do you want special characters? (Y/N): ").upper())
    password = ""
    abc = list(string.ascii_lowercase)
    ABC = list(string.ascii_uppercase)
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["_", ".", "$", "#"]
    list1 = [abc, ABC, numbers, special_characters]
    list2 = [abc, ABC, numbers]
    for i in range(len):
        if special == "Y":
            choice1 = random.choice(list1)
            choice2 = random.choice(choice1)
            password = password + choice2
        elif special == "N":
            choice1 = random.choice(list2)
            choice2 = random.choice(choice1)
            password = password + choice2
    print("The password is: " + password)


generate_password(10)
