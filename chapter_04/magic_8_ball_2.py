# Imports the random function for use
import random

print('What do you want to ask the magic 8 ball?')
question = input()

# Create a list of possible 8 ball responses
messages = ['Why would you ask me that', 
    'Yea yea, sure sure',
    'Simon says no, bitch', 
    'I think you should ask yourself that question', 
    'Stop talking to a magic 8 ball and do something with your life', 
    'Please just go away', 
    'No way', 
    'No, go away', 
    'Yup.']

# Print the 8 ball response, which is a random message from the messages list.  messages[] says to display the message at the returned index, random.randint(0, len()) returns a random integer between 0 and the total number of strings in the 'messages' list value. Not clear what the - 1 is for yet.
print(messages[random.randint(0, len(messages) - 1)])