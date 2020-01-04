#! /usr/bin/python3
'''
Search and open results from pypi.org.

    Gets search keywords from the command line arguments.
    Retrieves the search results page.
    Opens a browser tab for each result.
'''
import requests, sys, webbrowser, bs4

# Display something while downloading
print('Searching...')

# Try to download the page using the command line arguments
searchString = 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])
print(f"searchString: {searchString}")
res = requests.get(searchString)
# Make sure it was successful.
res.raise_for_status()


def dump(obj):
    for attr in dir(obj):
        if hasattr(obj, attr):
            print("obj.%s = %s" % (attr, getattr(obj, attr)))


# dump(res)

# Retrieve the top search result links.
soup = bs4.BeautifulSoup(res.content, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
# Only open a max of 5 tabs
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    # Build the link, knowing 'href' is the source link from HTML.
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    # Use webbrowser for the one thing it does, open pages.
    webbrowser.open(urlToOpen)
