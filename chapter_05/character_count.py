message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

print(count)

# Originally, the variable 'i' was written as 'character'. It was unclear to me how it would know to return a count of each character vs a count of the total number of characters, so I thought perhaps 'character' was something special in Python. To test that, I changed the variable to 'i' - the result was te same. Then I figured it probably had to do with the way the count() function works...which - not necessarily true. While the count function can be passed a specific character (or other things) to count - what's actually happening here is that when a string is passed to a for loop, it's actually looping over each character in the string: so the count is being applied to each character found in the string.