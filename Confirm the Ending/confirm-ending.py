# Check if a string (first argument, str) ends with the given target string (second argument, target).

import unittest 

def confirmEnding(string, target):
    string_length = len(string)
    target_length = len(target)
    index = string_length - target_length
    return string[index:] == target

class TestConfirmEnding(unittest.TestCase):
    
    def test_confirmEnding_should_return_true(self):
        string = "Bastian"
        target = "n"
        result = confirmEnding(string, target)
        self.assertTrue(result, "Expected True but got False")

    def test_confirmEnding_should_return_false(self):
        string = "Connor"
        target = "n"
        result = confirmEnding(string, target)
        self.assertFalse(result, "Expected False but got True")

    def test_confirmEnding_long_sentence_should_return_false(self):
        string = "Walking on water and developing software from a specification are easy if both are frozen"
        target = "specification"
        result = confirmEnding(string, target)
        self.assertFalse(result, "Expected False but got True")
    
    def test_confirmEnding_whole_word_should_return_true(self):
        string = "He has to give me a new name"
        target = "name"
        result = confirmEnding(string, target)
        self.assertTrue(result, "Expected True but got False")

    def test_confirmEnding_string_within_word_should_return_true(self):
        string = "Open sesame"
        target = "same"
        result = confirmEnding(string, target)
        self.assertTrue(result, "Expected True but got False")

    def test_confirmEnding_string_within_word_should_return_false(self):
        string = "Open sesame"
        target = "pen"
        result = confirmEnding(string, target)
        self.assertFalse(result, "Expected False but got True")

    def test_confirmEnding_string_long_sentence_2_should_return_false(self):
        string = "If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing"
        target = "mountain"
        result = confirmEnding(string, target)
        self.assertFalse(result, "Expected False but got True")
    

if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConfirmEnding))
    unittest.TextTestRunner(verbosity=2).run(suite)