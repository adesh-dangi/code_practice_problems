"""
#Two Pointers #String
problem : https://leetcode.com/problems/merge-strings-alternately/description/

solution: https://leetcode.com/problems/merge-strings-alternately/solutions/6850993/solved-in-on-time-by-adesh_brox-lbgj

Intuition
2 word, get min lenght to iterate, get word for suffix left after min lenght iteration

Approach
get min_len, biggest word
iterate in range of min_length pick char from word1,word2 on index of iteration
pick suffix from biggest word after min length
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len, max_len = (len(word1), word2) if len(word1) < len(word2) else (len(word2), word1)
        result = []
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        result.append(max_len[min_len:])
        return ''.join(result)
    
cases = [
    ("a","z"), #min 1
    ("abc", "pqr"), #equal len
    ("ab", "pqrs"), #word1 < word2
    ("abcd", "pq"), #word1 > word2
]
import time

for i in range(len(cases)):
    start = time.time()
    print(Solution().mergeAlternately(cases[i][0], cases[i][1]))
    print("Time: ", time.time() - start)

"""
problem: Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""