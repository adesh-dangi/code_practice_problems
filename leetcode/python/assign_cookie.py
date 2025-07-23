# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/
"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.


Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
 

Constraints:

1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1
 
"""
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        satisfied_children = 0
        if not s:
            return satisfied_children
        g.sort(reverse=True); s.sort(reverse=True)
        cookie_picked = 0
        for child in g:
            if child <= s[cookie_picked]:
                satisfied_children += 1
                cookie_picked += 1
                if cookie_picked >= len(s):
                    break
        # print(f"Children: {g}, Cookies: {s}, Satisfied: {satisfied_children}")
        return satisfied_children

obj = Solution().findContentChildren

cases = [
    [[1,2,3], [1,1], 1],
    [[1,2], [1,2,3], 2],
    [[1,2,3], [1,2], 2],
    [[10,9,8,7], [5,6,7,8], 2],
    [[1,2,3], [], 0],
    [[], [1,2,3], 0],
    [[1,2,3], [1,2,3], 3],
    [[1,2,3], [4,5,6], 3],
    [[1,2,3], [0,0,0], 0],
    [[1], [1], 1],
    [[1], [2], 1],
    [[2], [1], 0]]
for g, s, expected in cases:
    result = obj(g, s)
    assert result == expected, f"Expected {expected}, but got {result} for g={g}, s={s}"
else:
    print("All test cases passed!")