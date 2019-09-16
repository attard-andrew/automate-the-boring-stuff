# Initial Requirements
# -Write a function named 'collatz'
#    -One Parameter named 'number'
#    -If number is even, print number / 2 and return the value
#    -If number is odd, print and return 3 * number + 1
# -Write a program that lets user type in an integer
#    -Call the collatz() function on the entered number until it returns a value of 1

# ---------------------------------------------

# Create a function with one input parameter 'n'.  The goal is to continue executing the function with 
# the resulting value until it ultimately reaches 1
def collatz(n):
    if n == 1:    # If n is equal to 1, then just print 1 and stop execution
        print(n)
        return
    elif n % 2 == 0:    # If n is an even number, then divide it by 2 and store the value
        new_number = n // 2
        print(new_number)
        collatz(new_number)    # Take the new number and run through the collatz function again
    else:
        new_number = 3 * n + 1
        print(new_number)
        collatz(new_number)

# Ask the user for the initial value to feed into the collatz function
print('Give me a number')
number = int(input())
collatz(number)

# Some things I learned
# -You can call a function within itself (I ran collatz() within itself using a new variable)
# -There's a whole bunch of different ways to accomplish the same goal - there really isn't a 
# single 'right' answer
# -I need to be careful about how I interpret the project requirements - I struggled at first 
# because I believed I was only supposed to use a single variable. In reality - it was just the
# function that was supposed to use a single *parameter*
# -People on the internet told me to use single line comments and break them at around column 100