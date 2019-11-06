def boxPrint(symbol, width, height):
	# To prevent the user from providing more than one symbol such as *
	if len(symbol) != 1:
		raise Exception('Symbol must be a single character string.')
	# Both width & height should be at least 2
	if width <= 2:
		raise Exception('Width must be greater than 2.')
	if height <= 2:
		raise Exception('Height must be greater than 2.')
	# Duplicate the symbol by the width - this creates the top of the box
	print(symbol * width)
	# This creates the height of the box, the spaces add the filler, we subtract
	# by 2 since the first & last characters will be filled by the symbol
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	# This creates the bottom of the box
	print(symbol * width)

# This defines a loop with multiple variables 'sym', 'w', 'h' - each which are
# respectively passed in the following arguments
for sym, w, h, in (('*', 4, 4), ('0', 20, 5), ('0', 20, 5), ('x', 1, 3), 
	('ZZ', 3, 3)):
	# For each of the values being looped through above, try to execute the 
	# boxPrint function
	try:
		boxPrint(sym, w, h)
	# If an error is raised, store the message as err, then print it
	except Exception as err:
		print('An exception happened: ' + str(err))