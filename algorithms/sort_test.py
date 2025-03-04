import unittest

from .sort import insert_sort, quick_sort


class SortTest(unittest.TestCase):

    def test_sort(self):
        # case 1
        a = [2]
        insert_sort(a)
        self.assertEqual(a, [2])

        # case 2
        a = [4, 3, 2, 1]
        insert_sort(a)
        self.assertEqual(a, [1, 2, 3, 4])

        # case 2
        a = [4, 3, 2, 1]
        insert_sort(a)
        self.assertEqual(a, [1, 2, 3, 4])


class QuickSortTest(unittest.TestCase):

    def test_quick_sort(self):
        # case 1: short list
        a = [1]
        quick_sort(a, 0, len(a) - 1)
        self.assertEqual(a, [1])

        # case 2: len 3 list
        a = [4, 1, 7]
        quick_sort(a, 0, len(a) - 1)
        self.assertEqual(a, [1, 4, 7])

        # case 3: sorted list
        a = [8, 7, 5, 4, 2, 1]
        quick_sort(a, 0, len(a) - 1)
        self.assertEqual(a, [1, 2, 4, 5, 7, 8])

        # case 4: norm random list
        a = [5, 4, 2, 6, 7, 8, 9, 3, 1, 4]
        quick_sort(a, 0, len(a) - 1)
        self.assertEqual(a, [1, 2, 3, 4, 4, 5, 6, 7, 8, 9])

        # case 5: all equal element
        a = [4,4,4,4,4]
        quick_sort(a, 0, len(a) - 1)
        self.assertEqual(a, [4,4,4,4,4])



if __name__ == '__main__':
    unittest.main()
