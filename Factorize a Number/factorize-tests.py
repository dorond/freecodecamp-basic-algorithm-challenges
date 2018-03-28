import unittest 
import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize_returns_int(self):
        #Should return type int
        factorizer = factorize.Factorize()
        result = factorizer.factorize(5)
        self.assertIsInstance(result, int, "Expected an int, but got" + str(type(result)))

    def test_factorize_5(self):
        factorizer = factorize.Factorize()
        expected = 120
        result = factorizer.factorize(5)
        self.assertEqual(result, expected, "Expected: " + str(expected) + " but got: " + str(result))

    def test_factorize_10(self):
        factorizer = factorize.Factorize()
        expected = 3628800
        result = factorizer.factorize(10)
        self.assertEqual(result, expected, "Expected: " + str(expected) + " but got: " + str(result))

    def test_factorize_20(self):
        factorizer = factorize.Factorize()
        expected = 2432902008176640000
        result = factorizer.factorize(20)
        self.assertEqual(result, expected, "Expected: " + str(expected) + " but got: " + str(result))

    def test_factorize_0(self):
        factorizer = factorize.Factorize()
        expected = 1
        result = factorizer.factorize(0)
        self.assertEqual(result, expected, "Expected: " + str(expected) + " but got: " + str(result))


if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFactorize))
    unittest.TextTestRunner(verbosity=2).run(suite)