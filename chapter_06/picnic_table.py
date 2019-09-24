# Create a function with 3 parameters: a dictionary of items and the left & right widths
def printPicnic(itemsDict, leftWidth, rightWidth):
    # Print a table header, 'PICNIC ITEMS' that is centered and takes the TOTAL of leftWidth + rightWidth input parameters as the length, then assigns a fill character of '-'
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    # Loop over each key:value pair in the provided dictinoary, then print the key left justified + the value (converted to a string) right justified
    for k, v, in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# Here, we're just creating the dictionary which will be passed to the printPicnic function's 'itemsDict' parameter
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# Executig the function with different input parameters
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)