# https://leetcode.com/problems/fizz-buzz/
# 412. Fizz Buzz
"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
"""
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls = list(range(1,n+1))
        for ix, i in enumerate(ls):
            p3 = i%3==0
            p5 = i%5==0
            # print(i, p3, p5)
            if p3 and p5:
                ls[ix] = "FizzBuzz"
            elif p3:
                ls[ix] = "Fizz"
            elif p5:
                ls[ix] = "Buzz"
            else:
                ls[ix] = str(i)
        return ls

cases = [
    (3, ["1","2","Fizz"]),
    (5, ["1","2","Fizz","4","Buzz"]),
    (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
]

for case in cases:
    op = Solution().fizzBuzz(case[0])
    assert op == case[1], f"Expected {case[1]}, but got {op}"
else:
    print("All tests passed!!")