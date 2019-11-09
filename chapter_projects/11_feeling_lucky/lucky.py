#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
# Defines a variable which will store the response from the Google search results
# page where the search term is sliced from the the argument provided
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
# Check that there are no issues with the request
res.raise_for_status()

# Retrieve top search result links (the results appearing on the first SERP)
soup = bs4.BeautifulSoup(res.text)

# Use soup.select to get a list of all elements that match the '.r a' selector
linkElems = soup.select('.r a')
# The number of tabs to open will be either 5 (the default for webbrowser) 
# or the length of the linkElems list returned, whichever is smaller -
# thanks to the min() function (scenarios in which fewer than 5 results 
# are returned)
numOpen = min(5, len(linkElems))
# For each iteration of the loop, use webbrowser.open() to open a new tab in the
# browser.  Note that the href attribute's value in the returned <a> elements do
# not have the initial http://google.com part, so you have to concatenate
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))