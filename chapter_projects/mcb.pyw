#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to-keyword.
#		 py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#		 py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content. If the total length of arguments is 3 and the first
# argument is 'save' - passed to .lower for case insensitiivty - then assign
# the current clipboard value to a variable named from the second argument and
# store it in mcbShelf
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
# If there are only 2 arguments, then...
elif len(sys.argv) == 2:
	# If the first argument is list, then copy a list of the keys in the shelf
	# (which I recall behaves similar to a dictionary) and convert it to a 
	# string
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	# Otherwise, check if the first argument is saved in mcbShelf. If it is,
	# then copy the value stored at they key (defined by the first argument)
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()