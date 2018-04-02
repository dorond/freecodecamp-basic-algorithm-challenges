# Write a function that splits an list (first argument) into groups the 
# length of size (second argument) and returns them as a two-dimensional list of lists.

import unittest 

def chunkListInGroups(l, size):
    result = []

    list_length = len(l)
    num_full_chunks = list_length // size      # Determine how many completed chunks
    left_over_chunk = list_length % size  # Determine how many extra elements in final chunk that is < size

    index = 0
    for i in range(num_full_chunks):
        temp = []
        temp = l[index:index+size]
        result.append(temp)
        index += size
    if left_over_chunk != 0:
        temp = []
        temp = l[index:]
        result.append(temp)
    return result


class TestChunkyMonkey(unittest.TestCase):

    def test_chunk_even_letters_in_2(self):
        list_to_chunk = ["a", "b", "c", "d"]
        size = 2
        expected = [["a", "b"], ["c", "d"]]
        result = chunkListInGroups(list_to_chunk, size)
        self.assertListEqual(result, expected)


    def test_chunk_odd_numbers_in_3(self):
        list_to_chunk = [0, 1, 2, 3, 4, 5]
        size = 3
        expected = [[0, 1, 2], [3, 4, 5]]
        result = chunkListInGroups(list_to_chunk, size)
        self.assertListEqual(result, expected)

    def test_chunk_odd_numbers_in_2(self):
        list_to_chunk = [0, 1, 2, 3, 4, 5]
        size = 2
        expected = [[0, 1], [2, 3], [4, 5]]
        result = chunkListInGroups(list_to_chunk, size)
        self.assertListEqual(result, expected)

    def test_chunk_odd_numbers_in_4(self):
        list_to_chunk = [0, 1, 2, 3, 4, 5]
        size = 4
        expected = [[0, 1, 2, 3], [4, 5]]
        result = chunkListInGroups(list_to_chunk, size)
        self.assertListEqual(result, expected)

    def test_chunk_even_numbers_in_3(self):
        list_to_chunk = [0, 1, 2, 3, 4, 5, 6]
        size = 3
        expected = [[0, 1, 2], [3, 4, 5], [6]]
        result = chunkListInGroups(list_to_chunk, size)
        self.assertListEqual(result, expected)

    def test_chunk_even_numbers_in_4(self):
        list_to_chunk = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        size = 4
        expected = [[0, 1, 2, 3], [4, 5, 6, 7], [8]]
        result = chunkListInGroups(list_to_chunk, size)
        self.assertListEqual(result, expected)

    def test_chunk_even_numbers_in_2(self):
        list_to_chunk = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        size = 2
        expected = [[0, 1], [2, 3], [4, 5], [6, 7], [8]]
        result = chunkListInGroups(list_to_chunk, size)
        self.assertListEqual(result, expected)
   


if __name__ == '__main__':
    # Run the tests and print verbose output to stderr.
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestChunkyMonkey))
    unittest.TextTestRunner(verbosity=2).run(suite)