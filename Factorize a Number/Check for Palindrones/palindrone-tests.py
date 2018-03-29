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

    def test_palindrone_check_long_sentence_with_spaces_should_return_true(self):        
        result = palindrone.checkPalindrone("never odd or even")
        self.assertTrue(result, "Expected True but got False")

    def test_palindrone_single_word_non_palindrone_should_return_false(self):        
        result = palindrone.checkPalindrone("nope")
        self.assertFalse(result, "Expected False but got True")

    def test_palindrone_single_word_almost_palindrone_should_return_false(self):        
        result = palindrone.checkPalindrone("almostomla")
        self.assertFalse(result, "Expected False but got True")

    def test_palindrone_check_mix_punctuation_numbers_letters_spaces_should_return_true(self):        
        result = palindrone.checkPalindrone("My age is 0, 0 si ega ym.")
        self.assertTrue(result, "Expected True but got False")

    def test_palindrone_mixing_words_and_numbers_should_return_false(self):        
        result = palindrone.checkPalindrone("1 eye for of 1 eye.")
        self.assertFalse(result, "Expected False but got True")

    def test_palindrone_check_lots_of_synbols_and_numbers_should_return_true(self):        
        result = palindrone.checkPalindrone("0_0 (: /-\ :) 0-0")
        self.assertTrue(result, "Expected True but got False")

    def test_palindrone_mixing_words_and_symbols_should_return_false(self):        
        result = palindrone.checkPalindrone("five|\_/|four")
        self.assertFalse(result, "Expected False but got True")

if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPalindrone))
    unittest.TextTestRunner(verbosity=2).run(suite)