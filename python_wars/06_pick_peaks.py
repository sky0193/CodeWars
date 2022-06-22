"""
In this kata, you will write a function that returns the positions and the values of the "peaks" 
(or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] 
has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: 
pos and peaks. Both of these properties should be arrays. 
If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return 
{pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty),
so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks 
(in the context of a mathematical function, we don't know what is after and before and therefore, 
we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. 
In case of a plateau-peak, please only return the position and value of the beginning of the plateau. 
For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)


Result Algorithm:
input:  [0, 1, 2, 5, 1, 0] , size = 6
calculate_neighbouring_diff: [(0-1), (1-2), (2-5), (5-1), (1-0)] -> [-1, -2, -3, 4, 1] , size = 5
change of sign at pos 2 to 3 (from -3 to 4), only from negative sign to positive (positive to negative is minimum)
"""

import unittest

class TestEncryption(unittest.TestCase):
    def test_pick_peaks(self):
        self.assertEqual(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
        self.assertEqual(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
        self.assertEqual(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
        self.assertEqual(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
        self.assertEqual(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
        self.assertEqual(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
        self.assertEqual(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
        self.assertEqual(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
        self.assertEqual(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]),{'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
        self.assertEqual(pick_peaks([]),{"pos":[],"peaks":[]})
        self.assertEqual(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})



def pick_peaks(arr):
    neighbouring_diff_array = [arr[idx] - arr[idx+1] for idx, _ in enumerate(arr) if idx < len(arr) - 1]
    pos = []
    peak = []

    idx = 0
    while idx < len(neighbouring_diff_array)-1:
        if(neighbouring_diff_array[idx] < 0 and neighbouring_diff_array[idx+1] > 0):
            pos.append(idx+1)
            peak.append(arr[idx+1])

        if(neighbouring_diff_array[idx] < 0 and neighbouring_diff_array[idx+1] == 0):
            candidate_pos = idx+1
            candidate_peak = arr[idx+1]
            
            idx = idx + 1

            while idx < len(neighbouring_diff_array) - 1 and neighbouring_diff_array[idx+1] == 0:
                idx = idx + 1
            if(idx ==  len(neighbouring_diff_array) - 1):
                break

            if(neighbouring_diff_array[idx+1] > 0):
                pos.append(candidate_pos)
                peak.append(candidate_peak)
                
        idx = idx + 1
        
                

    result = {"pos": pos, "peaks": peak}
    return result

def pick_peaks_easy(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}

def pick_peaks_zip(arr):
    pos_delta = [pd for pd in enumerate((b - a for a, b in zip(arr, arr[1:])), 1) if pd[1]]
    positions = [a[0] for a, b in zip(pos_delta, pos_delta[1:]) if a[1] > 0 and b[1] < 0]
    return {'pos': positions, 'peaks': [arr[p] for p in positions]}

def main():
    unittest.main()
    pass

if __name__ == "__main__":
    main()