import random

cust_data = {}
new_user_attributes = ["name", "adress", "phone num", "govt id", "amount"]


def new_user():
    acc_num = random.randint(10000, 99999)
    while acc_num in cust_data:
        acc_num = random.randint(10000, 99999)
    new_user_input = []
    for i in range(4):
        user_input = input("Please enter your " + new_user_attributes[i] + ": ")
        new_user_input.append(user_input)
    amount_input = int(input("Please enter the amount: "))
    new_user_input.append(amount_input)
    user_dict = {acc_num: [new_user_input]}
    cust_data.update(user_dict)
    print("""
  Your details are added successfully.
  Your account number is""", acc_num, """
  Please don't lose it.""")


def existing_user():
    valid_actions = ["1", "2", "3"]
    credentials = int(input("Please enter your account number: "))
    while credentials not in cust_data.keys():
        credentials = int(input("Not found. Please enter your correct account numbers: "))
    print("Welcome,", cust_data[credentials][0][0], "! ")
    print("""Enter 1 to check your balance.
Enter 2 to withdraw an amount.
Enter 3 to deposit an amount.""")
    user_action = input()
    while user_action not in valid_actions:
        print("""Invalid input! 
Enter 1 to check your balance.
Enter 2 to withdraw an amount.
Enter 3 to deposit an amount.""")
        user_action = input()
    if user_action == "1":
        print("Your current balance is ", cust_data[credentials][0][4], "$")
    elif user_action == "2":
        withdraw_amount = int(input("Please enter the amount to be withdrawn: "))
        if withdraw_amount > cust_data[credentials][0][4]:
            print("Insufficient balance")
            print("Available amount: ", cust_data[credentials[0][4]])
        else:
            new_amount = cust_data[credentials][0][4] - withdraw_amount
            cust_data[credentials][0][4] = new_amount
            print("Withdraw successful.")
            print("Available balance: ", cust_data[credentials][0][4])
    elif user_action == "3":
        deposit_amount = int(input("Please enter the amount to be deposited: "))
        cust_data[credentials][0][4] = cust_data[credentials][0][4] + deposit_amount
        print("Deposit successful.")
        print("Available amount: ", cust_data[credentials][0][4])


while True:
    valid_inputs = ["1", "2", "3"]
    print("""
Welcome to the Horizon Bank!

Enter 1 if you are a new customer.
Enter 2 if you are an existing customer.
Enter 3 to terminate the application.""")
    app_action = input()
    while app_action not in valid_inputs:
        print("""Invalid input!
Enter 1 if you are a new customer.
Enter 2 if you are an existing customer.
Enter 3 to terminate the application.""")
        app_action = input()
    if app_action == "1":
        new_user()
        print("Thank you for banking with us!")
    elif app_action == "2":
        existing_user()
        print("Thank you for banking with us!")
    elif app_action == "3":
        print("Thank you for banking with us!")
        break
