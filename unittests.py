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



if __name__ == '__main__':
    unittest.main()