# Create a dictionary called birthdays with key-value pairs of name: birthday
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# Until a name in the dictionary is entered or no name is entered, ask the user to enter a name
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

# If the name is available, then display it
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
# If the name is not available, then ask for it and add it to the dictionary where <name> is the new index or key and <bday> is the associated value
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')