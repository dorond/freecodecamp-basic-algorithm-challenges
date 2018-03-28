import unittest 
import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize_returns_int(self):
        #Should return type int
        factorizer = factorize.Factorize()
        result = factorizer.factorize(5)
        self.assertIsInstance(result, int, "Expected an int, but got" + str(type(result)))

    def test_factorize(self):
        factorizer = factorize.Factorize()
        expected = 120
        result = factorizer.factorize(5)
        self.assertEqual(result, 120, "Expected: " + str(expected) + " but got: " + str(result))


if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFactorize))
    unittest.TextTestRunner(verbosity=2).run(suite)