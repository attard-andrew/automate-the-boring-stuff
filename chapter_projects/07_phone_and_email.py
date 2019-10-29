#! python3
# 07_phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

# Pyperclip used for copy/paste functions, re for regular expressions
import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?	# area code
	(\s|-|\.)?			# separator
	(\d{3})				# first 3 digits
	(\s|-|\.)			# separator
	(\d{4})				# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
	)''', re.VERBOSE)

# Email regex which accepts lower or uppercase letters, numbers, and a few
# special characters within the username (._%+-) withint a character class
# Reminder: the + in use here says to match one or more of the preceding
# characters
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+	# username
	@					# @ symbol
	[a-zA-Z0-9.-]+		# domain name
	(\.[a-zA-Z]{2,4})	# dot-something
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
# Create an array which I assume will store matches
matches = []

# for each group - which I learned earlier is defined by the parentheses and behaves
# similar to an array - and of each match in the phoneRegex string...
for groups in phoneRegex.findall(text):
	# Where area code represent a group [1], the first 3 digits another [3], and
	# so on.  This says to join these groups with a - separator. This is done
	# because although the program will match phone numbers in various formats
	# we want to return them in a standard format
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	# This last bit says if the extension is not blank, then append ' x' + <extension #>
	# to the string.
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	# Then, add (append) the matched phone number to the matches list variable
	matches.append(phoneNum)
	# Same for emails
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to the clipboard.  Assuming the length of the matches list variable
# is great than 0, then copy the matches, joined with newline character as the separator
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	# The print statements here are just to make it easier to see what's going on
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')