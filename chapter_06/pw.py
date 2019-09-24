#! python3
# pw.py - An insecure password locker program.

# Create a dictionary of passwords for different platforms
PASSWORDS = {'email': 'F7mJ5432LjissS954xny', 'blog': 'Vddfi532Jjvx35Yio', 'facebook': 'fdjsio5423IfjdsSO34'}

# import the sys module - used for accepting command line arguments - and the pyperclip module, used for copying data to the clipboard
import sys, pyperclip
# If the number of arguments provided to the command line is less than 2 (where the program name is argument 1 & the key to search is argument 2), then print a message explaining the proper input
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# Assigns a variable to specify that the argument at index 1 is the account name. ie: pw.py[0] email[1]
account = sys.argv[1]   # first command line arg is the account name

# If the account provided is in the passwords dictionary, then copy the value for the key specified (determined by the 'account' passed in)
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    # Give a success message the the account was copied to the clipboard
    print('Password for ' + account + ' copied to clipboard.')
else:
    # If no account with the entered name is found, then print a failure message
    print('There is no account named ' + account)