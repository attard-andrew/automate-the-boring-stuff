# the_collatz_sequence.py fulfills the minimum requirements outlined for that exercise. Now I want
# to put on my BA hat and think about:
#   -How users might actually interact with the program and what issues may arise
#   -Based on what I've learned and what I know (or think I know) about user behaviour, how can I
#    improve it?

# Thoughts on improvements:
#   -I use the print() function to ask the user for a number, but I've seen people online attaching text
#    to the input() function - so I think I can eliminate the print()
#   -I ask the user for number, but what if they give me text? I assume I'll get an error. Since I've 
#    learned a bit about exception handling, I can attempt a try/except statement
#   -After adding the exception handling, I decided to add a for loop to give the user multiple chances
#    to enter a number, with increasingly angry messages

# --------------------------------------------

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

# This loop update needs some work, since the function will loop within the range even if an integer is
# provided.  Second - i will increment in either scenario too, so if the first incorrect input is
# received on the third try, then "Are you stupid?" will still be received.
for i in range(5):
    # print(i) 
    try:
        number = int(input('Please enter an integer\n, you have 4 tries'))
        collatz(number)
    except ValueError:
        if i == 0:
            print('Sorry, you did not enter a number - please try again')
        elif i == 1:
            print('You didn\'t enter a number again.')
        elif i == 2:
            print('Are you stupid?')
        elif i == 3:
            print('You get one more chance.')
        elif i == 4:
            print('Fuck this.')