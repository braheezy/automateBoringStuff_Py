'''
Simple grep-like search.add()

Opens all .txt files in current folder and searches for any line that matches a user-supplied regular expression. Prints each line to terminal.

TODO: Enable search in any folder passed through argument
TODO: Recursive search through folders
'''
import re, argparse, os


def regexSearch(searchTerm):
    cwd = os.getcwd()
    # List of all items in the current directory
    dirs = os.listdir(cwd)
    # print(f'dirs: {dirs}')

    # For each item, check if plaintext file
    for item in dirs:
        if os.path.isfile(os.path.join(cwd, item)):
            # Try to search this item
            try:
                with open(item) as file:
                    print(f'checking {item}')
                    fileStrings = file.readlines()
                    for line in fileStrings:
                        matchObj = re.search(searchTerm, line)
                        if matchObj:
                            print(f"found: {line}")
            except UnicodeDecodeError:
                # binary file encountered
                print("binary file encountered")
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("search_term")

    args = parser.parse_args()
    # print(args.search_term)
    regexSearch(args.search_term)