'''
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

import unittest

class TestSnailSort(unittest.TestCase):
    def test_pick_peaks(self):
        self.assertEqual(snail([[]]), [])
        self.assertEqual(snail([[43]]), [43])
        self.assertEqual(snail([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertEqual(snail([[1,2,3],[8,9,4],[7,6,5]]), [1,2,3,4,5,6,7,8,9])

def snail(snail_map):
    result = []
    len_snail = len(snail_map)-1

    if(len_snail == 0):  
        return snail_map[0]

    start_row_idx = 0
    end_row_idx = len_snail
    start_col_idx = 0
    end_col_idx = len_snail

    while start_row_idx <= end_row_idx and start_col_idx <= end_col_idx:
        for i in range(start_col_idx, end_col_idx +1):
            result.append(snail_map[start_row_idx][i])
        start_row_idx += 1

        for i in range(start_row_idx, end_row_idx + 1):
            result.append(snail_map[i][end_col_idx])
        end_col_idx -= 1

        if start_row_idx > end_row_idx: break

        for i in range(end_col_idx, start_col_idx - 1, -1):
            result.append(snail_map[end_row_idx][i])
        end_row_idx -= 1 

        if start_col_idx > end_col_idx: break

        for i in range(end_row_idx, start_row_idx - 1, -1):
            result.append(snail_map[i][start_col_idx])
        start_col_idx += 1  

    return result

import numpy
def recurse(matrix):
    if not len(matrix): return
    for el in matrix[0]: print(el)
    recurse(numpy.rot90(matrix[1:]))


def main():
    unittest.main()
    pass

if __name__ == "__main__":
    main()