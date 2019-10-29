# Create a function to check if the entered text is a valid phone number
def isPhoneNumber(text):
	# First, check if the length of the text is 12 character ***-***-****
	if len(text) != 12:
		return False
	# Next, for each of the first 3 characters in text, check if they are decimals
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	# Then check if the 4th character (at index 3), is a hyphen. The same is
	# repeated for the rest of the phone number
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

# If we wanted to look for a phone number in a larger string...
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# For the entire length of th message
for i in range(len(message)):
	# Create a variable 'chunk'. Since i starts at 0, the first iteration pulls
	# the part of the string from 0:12, then evaluates it in the isPhoneNumber
	# function. If it matches the structure of a phone number, then print it
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: ' + chunk)
	print('Done')