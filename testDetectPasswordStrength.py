import unittest, re
'''
Determines if a password is strong. It must follow these rules:
    1. At least 8 characters
    2. Contains both upper and lowercase characters
    3. Has at least 1 digit
'''

passwords = ["qweH8fhu", "qweHgfhu", "qweh8fhu", "", "qwevfhu"]
pass_results = [True, False, False, False, False]

cond1 = ["1234567", "12345678"]
cond2 = [
    "abcdefgh", "ABCDEFGH", "ABCDefgh", "Abcdefgh", "abcdefgH", "ABCdefGH",
    "abdDEFgh", "abcdEfgh"
]
cond3 = ["abcdefgh", "1bcdefgh", "abc2efgh", "abcdefg3"]


def detectPasswordStrength(password):
    conditionResults = [False] * 3
    # Test for condition 1
    if len(password) > 7:
        conditionResults[0] = True

    # Test for condition 2
    upperegex = re.compile(r'[A-Z]')
    loweregex = re.compile(r'[a-z]')
    if upperegex.search(password) and loweregex.search(password):
        conditionResults[1] = True

    # Test for condition 3
    numberRegex = re.compile(r'\d')
    if numberRegex.search(password):
        conditionResults[2] = True

    return conditionResults


class TestDetectPasswordStrength(unittest.TestCase):
    def testCondition1(self):
        self.assertFalse(detectPasswordStrength(cond1[0])[0])

        self.assertTrue(detectPasswordStrength(cond1[1])[0])

    def testCondition2(self):
        self.assertFalse(detectPasswordStrength(cond2[0])[1])
        self.assertFalse(detectPasswordStrength(cond2[1])[1])

        self.assertTrue(detectPasswordStrength(cond2[2])[1])
        self.assertTrue(detectPasswordStrength(cond2[3])[1])
        self.assertTrue(detectPasswordStrength(cond2[4])[1])
        self.assertTrue(detectPasswordStrength(cond2[5])[1])
        self.assertTrue(detectPasswordStrength(cond2[6])[1])
        self.assertTrue(detectPasswordStrength(cond2[7])[1])

    def testCondition3(self):
        self.assertFalse(detectPasswordStrength(cond3[0])[2])

        self.assertTrue(detectPasswordStrength(cond3[1])[2])
        self.assertTrue(detectPasswordStrength(cond3[2])[2])
        self.assertTrue(detectPasswordStrength(cond3[3])[2])

    def testDetection(self):
        for pw, result in zip(passwords, pass_results):
            res = detectPasswordStrength(pw)
            res = res[0] and res[1] and res[2]
            self.assertTrue(
                result == res,
                f"result: {result}, actual: {res}, password: {pw}")


if __name__ == "__main__":
    unittest.main()