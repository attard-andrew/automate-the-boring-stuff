'''
Requirements
-Write a function named 'collatz'
    -One Parameter named 'number'
    -If number is even, print number / 2 and return the value
    -If number is odd, print and return 3 * number + 1
-Write a program that lets user type in an integer
    -Call the collatz() function on the entered number until it returns a value of 1
'''

# Define function that follows the collatz sequence, a mathematical sequence that will eventually return a value of 1
def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number // 2
            return print(str(number))
        else:
            3 * number + 1
        return print(str(number))

# Ask the user for the initial input value for the sequence
print('Enter an integer')
number = int(input())
# As long as the return value does not = 1, print the number
collatz(number)
