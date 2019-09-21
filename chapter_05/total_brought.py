# Create a dictionary of names where the value of the first key is a dictionary containing 
# key:value pairs of the items being brought.

allGuests = {'Alice': {'apples': 5, 'pretzels': 12}, 
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

# Create a function with two input parameters: 'guests' and 'items'
def totalBrought(guests, item):
    # Set a default value for numBrought to 0
    numBrought = 0
    # Where k = the key in the value passed to the 'guests' paramater, and v = its 
    # associated value, provided through the .items() method.  "guests" in this case is the 
    # dictionary "allGuests". So allGuests.items() returns the stored key:value pairs.
    for k, v, in guests.items():
        # Update numBrought to equal the current value of numBrought + v.get(item, 0)
        # v - or the value returned by allGuests.items(), being another dictionary: 
        # 'apples': 5, 'pretzels': 12 etc., then uses the .get method to search the 
        # dictionary keys for the item (provided by the function parameter). If the key
        # is not found, then 0 will be returned and added to numBrought
        numBrought = numBrought + v.get(item, 0)
    # The final statement just returns the summed value of numBrought
    return numBrought

print('Number of things being brought:')
# Walking through one of these lines where the defined function is used:
# Print a bulleted list which sums the total of each item brought. The str() function used just 
# converts the output (being an integer) to a string. The totalBrought() function accepts two 
# parameters, the first being the dictionary allGuests, and the second being the key we are looking
# for in the dictinary, which is what is utilized in the .get method to pull the count of the item brought
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))