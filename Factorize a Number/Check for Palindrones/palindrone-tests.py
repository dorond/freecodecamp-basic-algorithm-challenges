import unittest
import palindrone


class TestPalindrone(unittest.TestCase):

    def test_palindrone_returns_boolean(self):
        result = palindrone.checkPalindrone("eye")
        self.assertIsInstance(result, bool, "Expected a bool in return, got a: " + str(type(result)))

    def test_palindrone_eye_returns_true(self):
        result = palindrone.checkPalindrone("eye")
        self.assertTrue(result, "Expected True but got False")

    def test_palindrone_check_leading_dash_returns_true(self):
        result = palindrone.checkPalindrone("_eye")
        self.assertTrue(result, "Expected True but got False")

    def test_palindrone_check_spaces_returns_true(self):        
        result = palindrone.checkPalindrone("race car")
        self.assertTrue(result, "Expected True but got False")
    
    def test_palindrone_non_palindrone_should_return_false(self):        
        result = palindrone.checkPalindrone("not a palindrome")
        self.assertFalse(result, "Expected False but got True")

    def test_palindrone_check_long_sentence_with_punctuation_should_return_true(self):        
        result = palindrone.checkPalindrone("A man, a plan, a canal. Panama")
        self.assertTrue(result, "Expected True but got False")

if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPalindrone))
    unittest.TextTestRunner(verbosity=2).run(suite)