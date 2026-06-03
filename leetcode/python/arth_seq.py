"""
Q1. Can Make Arithmetic Progression From Sequence
Easy
Topics
premium lock icon
Companies
Hint
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

Constraints:

2 <= arr.length <= 1000
-106 <= arr[i] <= 106
"""

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        i,j= 0,1
        diff_ = ""
        diff_old = ""
        ret = True
        while j!=len(sorted_arr):
            diff_old = str(diff_)
            diff_ = str(sorted_arr[j]-sorted_arr[i])
            if diff_.isdigit() and diff_old.isdigit() and diff_ != diff_old :
                ret = False
                break
            i,j = i+1, j+1
        return ret
    
print("output = ", Solution().canMakeArithmeticProgression([3,5,1])) # True
print("output = ", Solution().canMakeArithmeticProgression([1,2,4])) # False
