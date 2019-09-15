'''
Requirements
-Write a function named 'collatz'
    -One Parameter named 'number'
    -If number is even, print number / 2 and return the value
    -If number is odd, print and return 3 * number + 1
-Write a program that lets user type in an integer
    -Call the collatz() function on the entered number until it returns a value of 1
'''


def collatz(n):
    if n == 1:
        print(n)
        return
    elif n % 2 == 0:
        new_number = n // 2
        print(new_number)
        collatz(new_number)
    else:
        new_number = 3 * n + 1
        print(new_number)
        collatz(new_number)

print('Give me a number')
number = int(input())
collatz(number)
