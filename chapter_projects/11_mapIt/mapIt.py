#! python3
# mapIt.py - Launches a map in the browser using an address from the command
# line or clipboard

import webbrowser, sys, pyperclip

# If the arguments passed is great than 1 (meaning that more than just the 
# filename has been passed)
if len(sys.argv) > 1:
	# Then get the address, which is all remaining arguments (sliced, then joined)
	# The remaining arguments are joined since they would otherwise all be 
	# interpreted as separate arguments, ie. '290' 'Brenmer' 'Blvd' instead of
	# '290 Brenmer Blvd'
	address = ' '.join(sys.argv[1:])
else:
	# Instead of getting the address from the command line, take it from the
	# clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.co.uk/maps/place/' + address)