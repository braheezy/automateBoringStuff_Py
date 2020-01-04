import unittest

testData = {
    "input": [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']],
    "output":
    '''  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose'''
}
'''
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

'''


class TestTablePrinter(unittest.TestCase):
    def setUp(self):
        pass

    def testPrintTable(self):
        self.assertEqual(testData["output"], printTable(testData["input"]))


def printTable(table):
    colWidths = [0] * len(testData['input'])
    # Find longest string in each row
    for index, line in enumerate(table):
        for word in line:
            if len(word) > colWidths[index]:
                colWidths[index] = len(word)
    print(colWidths)

    # right justify each inner list to colWidth value
    i = 0
    for i, line in enumerate(table):
        for j, word in enumerate(line):
            table[i][j] = word.rjust(colWidths[i])
        i += 1
    #print(table)

    # convert 2-d array to table, making sure to "rotate"
    final_string = ""
    for i in range(len(table[0])):
        for row in table:
            final_string += row[i] + " "
        final_string = final_string.rstrip()
        final_string += '\n'
    final_string = final_string.rstrip('\n')
    print(final_string)
    return final_string


if __name__ == "__main__":
    unittest.main()
