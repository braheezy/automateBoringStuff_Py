import unittest, pyperclip


# Take string from clipboard, add "* " in front, and return to
# clipboard.
def addBullets():
    # get string from clipboard
    inputString = pyperclip.paste()
    if not inputString:
        "Nothing in clipboard"
        return 0
    # Assume a list-like string with newlines at end of line
    inputString = inputString.split('\n')
    for index, line in enumerate(inputString):
        inputString[index] = "* " + line

    inputString = '\n'.join(inputString)

    print(f"{inputString}")

    pyperclip.copy(inputString)


test_data = {
    "input":
    '''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars''',
    "expected_output":
    '''* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars'''
}


class TestBulletPointAdder(unittest.TestCase):
    def setUp(self):
        pyperclip.copy(test_data["input"])

    def testSomething(self):
        addBullets()
        self.assertEqual(test_data["expected_output"], pyperclip.paste())


if __name__ == "__main__":
    unittest.main()