"""
problem:
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

time and space : O(n)
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n = len(candies)
        op = [False]*n
        max_candies = max(candies)
        for index, i in enumerate(candies):
            # print(i, i+extraCandies, max_candies, i + extraCandies >= max_candies, index)
            if i + extraCandies >= max_candies:
                op[index] = True
                # print(op)
        return op
    
candies = [2,3,5,1,3]; extraCandies = 3
print("sol1",Solution().kidsWithCandies(candies, extraCandies))

candies = [4,2,1,1,2]; extraCandies = 1
print("sol2",Solution().kidsWithCandies(candies, extraCandies))

candies = [12,1,12]; extraCandies = 10
print("sol3",Solution().kidsWithCandies(candies, extraCandies))
