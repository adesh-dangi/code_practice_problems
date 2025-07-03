# 1480. Running Sum of 1d Array
"""
https://leetcode.com/problems/running-sum-of-1d-array/description/
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
List = list

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        sum_op = output[0]
        for i in nums[1:]:
            sum_op +=i
            output.append(sum_op)
        return output

sol_obj = Solution()

# case1 
nums = [1,2,3,4]
expected = [1,3,6,10]

output = sol_obj.runningSum(nums)
print("Case1 : ", output==expected)

# case2
nums = [1,1,1,1,1]
expected = [1,2,3,4,5]

output = sol_obj.runningSum(nums)
print("Case1 : ", output==expected)

# case3
nums = [3,1,2,10,1]
expected = [3,4,6,16,17]

output = sol_obj.runningSum(nums)
print("Case1 : ", output==expected)




