import unittest 
import returnlargestnumber

class TestReturnLargest(unittest.TestCase):
    
    def test_should_return_list(self):
        values = [[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]
        result = returnlargestnumber.return_largest_number(values)
        self.assertIsInstance(result, list, "Expected list but got " + str(type(result)))
    
    def test_values_group1(self):
        values = [[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]
        expected = [27,5,39,1001]
        result = returnlargestnumber.return_largest_number(values)
        self.assertListEqual(result, expected, "Expected " + str(expected) + " but got " + str(result))

    def test_values_group2(self):
        values = [[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]
        expected = [9, 35, 97, 1000000]
        result = returnlargestnumber.return_largest_number(values)
        self.assertListEqual(result, expected, "Expected " + str(expected) + " but got " + str(result))



if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReturnLargest))
    unittest.TextTestRunner(verbosity=2).run(suite)