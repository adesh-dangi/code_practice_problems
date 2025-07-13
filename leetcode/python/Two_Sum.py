# https://leetcode.com/problems/two-sum/description/
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):            
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]            
            num_to_index[num] = index
        # If no solution is found, return an empty list (though the problem guarantees one solution
        return []

obj = Solution().twoSum

cases = [
    ([2, 7, 11, 15], 9),  # Output: [0, 1]
    ([3, 2, 4], 6),       # Output: [1, 2]
    ([3, 3], 6),          # Output: [0, 1]
    ([1, 2, 3, 4, 5], 9),  # Output: [3, 4]
    ([5, 5, 11, 15], 20),  # Output : [0, 1]
]
for case in cases:
    result = obj(case[0], case[1])
    print(f"Input: nums = {case[0]}, \t\t target = {case[1]} \t\t| Output: {result}")    