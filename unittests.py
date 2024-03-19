import unittest
import PQHeap

class TestPriorityQueue(unittest.TestCase):
    def test_createEmptyPQ(self):
        expected_result = []
        actual_result = PQHeap.createEmptyPQ()
        self.assertEqual(expected_result, actual_result)

    # def test_HeapExtractMin(self):
    #     my_list = [1, 2, 3, 4, 5, 6]
    #     expected_result = # indsæt element med mindst prioritet + ændr listen!
    #     actual_result = HeapExtractMin(my_list)
    #     self.assertEqual(expected_result, actual_result)
    #     self.assertEqual([], my_list)
    
    def test_insert(self):
        my_list = [34, 645, -45, 1, 34, 0]
        expected_result = [-45, 0, 1, 34, 34, 645]

        the_list = PQHeap.create_emptyPQ()
        for element in my_list:
            the_list = PQHeap.insert(the_list, element)
            actual_result = the_list

        self.assertEqual(expected_result, actual_result)
    
    def test_parent(self):
        expected_result = 0
        actual_result = PQHeap.parent(2)
        self.assertEqual(expected_result, actual_result)
        
        expected_result = 1
        actual_result = PQHeap.parent(4)
        self.assertEqual(expected_result, actual_result)

        expected_result = 2
        actual_result = PQHeap.parent(5)
        self.assertEqual(expected_result, actual_result)

    def test_extract_min(self):
        # Initialize variables
        my_list = [-45, 1, 0, 645, 34, 34]
        expected_list = [0, 1, 645, 34, 34]
        expected_min = -45

        # perform test
        min_val = PQHeap.extract_min(my_list)

        # Check result
        self.assertEqual(expected_list, my_list)
        self.assertEqual(expected_min, min_val)

    def test_extract_min_all(self):
        """Tests that extract_min properly extracts min value and keeps list in min-heap structure"""
        # Initialize variables
        my_list = [-45, 1, 0, 645, 34, 34]
        sorted_list = []
        expected_list = [-45, 0, 1, 34, 34, 645]

        # Perform test
        for i in range(len(my_list)):
            sorted_list.append(PQHeap.extract_min(my_list))

        # Check results
        self.assertEqual([], my_list)               # my_list should be empty
        self.assertEqual(sorted_list, expected_list)     # expected_list should be sorted in ascending order

    def test_build_min_heap(self):
        my_list = [4, 1, 7, 3, 8, 5]
        expected_result = [1, 3, 5, 4, 8, 7]

        PQHeap.build_min_heap(my_list)

        self.assertEqual(expected_result, my_list)



if __name__ == '__main__':
    unittest.main()