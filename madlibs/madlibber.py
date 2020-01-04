#! /usr/bin/python3
# madlibber: Basic Mad-Libs game.

import argparse, re

KEYWORDS = {
    "ADJECTIVE": "Enter an adjective: ",
    "NOUN": "Enter a noun: ",
    "VERB": "Enter a verb: ",
    "ADVERB": "Enter an adverb: "
}

mad_lib_regex = r'ADJECTIVE|NOUN|ADVERB|VERB'


def madlibber(inputText):
    # inputText is a string of the file text
    '''
    Search the string for a KEYWORD. If found, use it
    to decide which prompt to show the user.
    Use the given REPLACEMENT WORD to substitute
    into the string.
    '''
    # Does a KEYWORD exist?
    obj = re.search(mad_lib_regex, inputText)
    while obj:
        # Ask the correct prompt based on current KEYWORD
        replacementWord = input(KEYWORDS[obj.group(0)])
        # Make sure to only replace the current KEYWORD
        # re.sub() returns a new string.
        inputText = re.sub(mad_lib_regex, replacementWord, inputText, count=1)
        # Keep doing this while more KEYWORDS exist
        obj = re.search(mad_lib_regex, inputText)

    print("Done!", inputText)
    # Write to new file in current dir
    with open('output.txt', 'w') as outFile:
        outFile.write(inputText)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")

    args = parser.parse_args()

    with open(args.input_file) as inFile:
        fileString = inFile.read()
    madlibber(fileString)