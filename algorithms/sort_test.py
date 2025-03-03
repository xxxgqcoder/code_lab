import unittest

from .sort import insert_sort

class SortTest(unittest.TestCase):
    def test_sort(self):
        # case 1
        a = [2]
        insert_sort(a)
        self.assertEqual(a, [2])
    
        # case 2
        a = [4,3,2,1]
        insert_sort(a)
        self.assertEqual(a, [1,2,3,4])

        # case 2
        a = [4,3,2,1]
        insert_sort(a)
        self.assertEqual(a, [1,2,3,4])





if __name__ == '__main__':
    unittest.main()