# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# 1342. Number of Steps to Reduce a Number to Zero
"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_c = 0
        while num!=0:
            if num%2==0:
                num = num//2
            else:
                num = num -1
            step_c+=1
        return step_c

cases = [
    (14,6),
    (8,4),
    (123,12),

]

for case in cases:
    op = Solution().numberOfSteps(case[0])
    assert op==case[1]
else:
    print("all test cases passed")