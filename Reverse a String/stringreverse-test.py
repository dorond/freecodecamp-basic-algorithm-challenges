import unittest 
import stringreverse

class TestStringReverse(unittest.TestCase):

    def test_reverse_string(self):
        #input string: testing
        #expected string: gnitset
        s = "testing"
        expected = "gnitset"

        reverser = stringreverse.StringReverser()
        result = reverser.reverse(s)
        self.assertEqual(expected, result, "Expected string: " + expected + " but got: " + result)
		

if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestStringReverse))
    unittest.TextTestRunner(verbosity=2).run(suite)