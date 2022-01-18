def series():
    while True:
        try:
            n = int(input("Enter a positive number here: "))
            n1 = 0
            n2 = 1
            count = 0

            if n == 0:
                return 0
            elif n == 1:
                return 1
            else:
                while count < n - 1:
                    nth = n1 + n2
                    n1 = n2
                    n2 = nth
                    count += 1
            return nth
            break
        except:
            print("Please enter a positive number")

print(series())
