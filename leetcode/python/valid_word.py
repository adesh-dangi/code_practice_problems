# 3136. Valid Word
# https://leetcode.com/problems/valid-word

"""
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

 

Constraints:

1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
"""
import string
ALL_UPPER = string.ascii_uppercase
All_Lower = string.ascii_lowercase
ALL_DIGITS = string.digits
ALL_vowels = 'aeiouAEIOU'
ALL_consonants = ''.join(set(ALL_UPPER + All_Lower) - set(ALL_vowels))

class Solution:
    def is_their_consonants(self, word: str) -> bool:
        for i in ALL_consonants:
            if i in word:
                return True
        return False
    
    def is_their_vowels(self, word: str) -> bool:
        for i in ALL_vowels:
            if i in word:
                return True
        return False
            
    def is_their_digits(self, word: str) -> bool:
        for i in ALL_DIGITS:
            if i in word:
                return True
        return False
            
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False  
        if not self.is_their_vowels(word):
            return False
        if not self.is_their_consonants(word):
            return False
        # if not self.is_their_digits(word):
        #     return False
        if "@" in word or "#" in word or "$" in word:
            return False
        return True 


obj = Solution().isValid

cases = [
    ("234Adas", True),
    ("b3", False),
    ("a3$e", False),
    ("abc", True),
    ("123", False),
    ("A1b2C3", True),
    ("aya", True), # leetcode case required not to check digits
]
for case in cases:
    result = obj(case[0])
    print(f"Testing {case[0]}: {result}")
    assert result == case[1], f"Failed for {case[0]}: expected {case[1]}, got {result}"
else:
    print("All test cases passed!")