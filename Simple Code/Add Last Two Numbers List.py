def series(n):
    n1 = 0
    n2 = 1
    count = 0
    if n <= 0:
        print('Please enter a positive integer')
        n = int(input('Enter a number here: '))
    elif n >= 0:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count = count + 1

series(120)