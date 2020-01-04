'''
Simple grep-like search.add()

Opens all .txt files in current folder and searches for any line that matches a user-supplied regular expression. Prints each line to terminal.

TODO: Enable search in any folder passed through argument
TODO: Recursive search
'''
import re, argparse, os


def regexSearch(searchTerm):
    # List of all items in the current directory
    dirs = os.listdir(os.getcwd())
    print(f'dirs: {dirs}')

    # Grab each item ending in .txt
    for item in dirs:
        if item.endswith(".txt"):
            # Search this item
            with open(item) as file:
                fileString = file.read()
                matchObj = re.findall(searchTerm, fileString)
                print(matchObj)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("search_term")

    args = parser.parse_args()
    print(args.search_term)
    regexSearch(args.search_term)