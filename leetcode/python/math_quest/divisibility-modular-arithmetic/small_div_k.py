"""
Q2. Smallest Integer Divisible by K
Medium
Topics
premium lock icon
Companies
Hint
Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.

 

Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.
 

Constraints:

1 <= k <= 105
"""
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # print("------------------ k = ",k)
        if k%2 == 0:
            return -1
        if k%5 == 0:
            return -1
        n = 1
        len_n = 1
        # print("k = ", k, n%k)
        while n%k != 0:
            n = (n*10 + 1)
            len_n += 1

        # print(" len - > n ->", len(str(n)))
        return len_n #len(str(n))
        
assert Solution().smallestRepunitDivByK(99989) == 99988 # int wont fit use sys.set_int_max_str_digits(0) if return len(str(n))

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0

        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1

assert Solution().smallestRepunitDivByK(1) == 1
assert Solution().smallestRepunitDivByK(2) == -1
assert Solution().smallestRepunitDivByK(3) == 3
assert Solution().smallestRepunitDivByK(4) == -1