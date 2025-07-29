# https://leetcode.com/problems/ransom-note/
# 383. Ransom Note

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        for char in ransomNote:
            if magazine_count.get(char, 0) == 0:
                return False
            magazine_count[char] -= 1

        return True

cases = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("abc", "aabbcc", True),
    ("xyz", "xyzz", True),
    ("hello", "oellh", True),
    ("test", "tteest", True),
    ("ransomnote", "noteasransom", True),
    ("leetcode", "codeleet", True),
    ("python", "pythonnn", True),
    ("magazine", "magazinemagazine", True)
]
for case in cases:
    ransomNote, magazine, expected = case
    result = Solution().canConstruct(ransomNote, magazine)
    assert result == expected, f"Failed for {case}: expected {expected}, got {result}"
else:
    print("All test cases passed!")