# Define an empty list
catNames = []

# While loops will continue as long as the condition is true. In this scenario, the condition is set to "True" - so it will loop infinitely until a break statement is reached. At least - that's my understanding so far.
while True:
    # Ask the user for the name of a cat
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    # Wait for input of the name
    name = input()
    # If no input is received, then break out of the loop
    if name == '':
        break
    # Add then input name to the catNames list value
    catNames = catNames + [name]
# Print "The cat names are:", then add a space + the entered names until the end of the list is reached. My assumption is that applying a for loop to a list will cause it to apply the code block to each index in the list
print('The cat names are:')
for name in catNames:
    print(' ' + name)