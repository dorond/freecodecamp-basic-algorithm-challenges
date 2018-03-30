import unittest 
import findlongestword

class TestFindLongestWord(unittest.TestCase):

    def test_should_return_a_number(self):
        text = "The quick brown fox jumped over the lazy dog"
        result = findlongestword.findHowLong(text)
        self.assertIsInstance(result, int, "Expected an int but got a " + str(type(result)))
    
    def test_should_return_6(self):
        text = "The quick brown fox jumped over the lazy dog"
        result = findlongestword.findHowLong(text)
        self.assertEqual(result, 6, "Expected a 6 but got " + str(result))

    def test_should_return_5(self):
        text = "May the force be with you"
        result = findlongestword.findHowLong(text)
        self.assertEqual(result, 5, "Expected a 5 but got " + str(result))

    def test_should_return_6_too(self):
        text = "Google do a barrel roll"
        result = findlongestword.findHowLong(text)
        self.assertEqual(result, 6, "Expected a 6 but got " + str(result))

    def test_should_return_8(self):
        text = "What is the average airspeed velocity of an unladen swallow"
        result = findlongestword.findHowLong(text)
        self.assertEqual(result, 8, "Expected a 8 but got " + str(result))

    def test_long_word_should_return_19(self):
        text = "What if we try a super-long word such as otorhinolaryngology"
        result = findlongestword.findHowLong(text)
        self.assertEqual(result, 19, "Expected a 19 but got " + str(result))
        

if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFindLongestWord))
    unittest.TextTestRunner(verbosity=2).run(suite)