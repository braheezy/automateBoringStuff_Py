import unittest, re
'''
Regex version of strip() from std libary

If no optional arguement is given, trim beginning and
ending whitespace.

If optional arguement given, remove that string.
'''

data = {
    "fifth": "fifth",
    " first ": "first",
    " second": "second",
    "third ": "third",
    "   fourth   ": "fourth",
    ("test string", "test"): " string",
    ("test_string", "t"): "es_sring",
    (" test str  ", "st"): " te r  "
}


def regexStrip(input_string, remove_string=None):
    if remove_string:
        # Remove requested string
        trimRegex = re.compile(f'({remove_string})')
    else:
        # Trim begining and ending whitespace
        trimRegex = re.compile(r'(^\s+)|(\s+$)')

    result = trimRegex.sub("", input_string)
    print(result)
    return result


class TestRegexStrip(unittest.TestCase):
    def testStrip(self):
        for input_value, output_value in data.items():
            if type(input_value) == tuple:
                self.assertEqual(output_value,
                                 regexStrip(input_value[0], input_value[1]))
            else:
                self.assertEqual(output_value, regexStrip(input_value))


if __name__ == "__main__":
    unittest.main()