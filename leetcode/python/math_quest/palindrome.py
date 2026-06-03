"""
Q3. Palindrome Number
Easy
Topics
premium lock icon
Companies
Hint
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x == 0 :
            return True
        original = x
        reverse = 0
        while x>0:
            reverse = (reverse*10) + (x%10)
            x = x//10
        print("stack = ", stack)
        return original == int(''.join(map(str, stack)))
assert Solution().isPalindrome(121) == True
assert Solution().isPalindrome(-121) == False
assert Solution().isPalindrome(10) == False
assert Solution().isPalindrome(0) == True