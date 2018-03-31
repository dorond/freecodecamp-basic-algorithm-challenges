import unittest 
import titlecasesentence


class TestTitleCaseSentence(unittest.TestCase):

    def test_should_return_string(self):
        text = "I'm a little tea pot"
        result = titlecasesentence.covertTitleCase(text)
        self.assertIsInstance(result, str, "Expected string but got " + str(type(result)))

    def test_standard_sentence(self):
        text = "I'm a little tea pot"
        expected = "I'm A Little Tea Pot"
        result = titlecasesentence.covertTitleCase(text)
        self.assertEqual(result, expected, "Expected: " + expected + " but got: " + result)
        
    
    def test_mixed_case(self):
        text = "sHoRt AnD sToUt"
        expected = "Short And Stout"
        result = titlecasesentence.covertTitleCase(text)
        self.assertEqual(result, expected, "Expected: " + expected + " but got: " + result)

    def test_all_uppercase_sentence(self):
        text = "HERE IS MY HANDLE HERE IS MY SPOUT"
        expected = "Here Is My Handle Here Is My Spout"
        result = titlecasesentence.covertTitleCase(text)
        self.assertEqual(result, expected, "Expected: " + expected + " but got: " + result)




if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestTitleCaseSentence))
    unittest.TextTestRunner(verbosity=2).run(suite)