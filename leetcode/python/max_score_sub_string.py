# 1717. Maximum Score From Removing Substrings
# https://leetcode.com/problems/maximum-score-from-removing-substrings

"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""

class Solution:
    def check_one_char_with_others(self, s, find_str, max_score, point):
        stack = []
        for i in s:
            if stack and stack[-1]+i == find_str:
                stack.pop()
                max_score+=point
            else:
                stack.append(i)
        return max_score, "".join(stack)
        
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_score = 0
        # x = ab, y= ba
        map_score = {"ab":x, "ba":y}
        find_str = ["ab","ba"]
        find_first = find_str.pop(int(not((x>y))))
        max_score, s = self.check_one_char_with_others(s, find_first, max_score,map_score[find_first])
        # print("max_score = ", max_score, " first_find = ", find_first)
        max_score, _ = self.check_one_char_with_others(s, find_str[0], max_score,map_score[find_str[0]] )
        return max_score

test_sol_obj = Solution().maximumGain

cases = [
    # string    , x, y , output
    ("cdbcbbaaabab", 4, 5, 19),
    ("aabbaaxybbaabb", 5, 4, 20),
    ("aabb", 5, 4, 10),
    ("ababbaba", 5, 4, 19),
    ("ababbaab", 5, 4, 19),
]

for case in cases[0:1]:
    result = test_sol_obj(case[0], case[1], case[2])
    print("\n\ncase", case[0], "x", case[1], "y", case[2], "output", case[3], " got = ",result)
    assert case[3] == result
else:
    print("All Cases Passed")
