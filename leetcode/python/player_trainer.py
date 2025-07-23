# Maximum Matching of Players With Trainers
#  https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
"""
You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

Example 1:

Input: players = [4,7,9], trainers = [8,2,5,8]
Output: 2
Explanation:
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.
Example 2:

Input: players = [1,1,1], trainers = [10]
Output: 1
Explanation:
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.
 

Constraints:

1 <= players.length, trainers.length <= 105
1 <= players[i], trainers[j] <= 109
"""
from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        match_count = 0
        trainer_i = 0
        for i in players:
            if i <= trainers[trainer_i]:
                match_count += 1
                trainer_i += 1
                if trainer_i == len(trainers):
                    break
        # print(players, trainers, match_count)
        return match_count

obj = Solution().matchPlayersAndTrainers

cases = [
    ([4, 7, 9], [8, 2, 5, 8], 2),
    ([1, 1, 1], [10], 1),
    ([1, 2, 3], [3, 2, 1], 3),
    ([5, 6, 7], [8, 9], 2),
    ([10, 20, 30], [15, 25, 35], 3),
    ([1, 2, 3], [4, 5, 6], 3),
    ([10, 20, 30], [5, 15, 25], 2),
    ([1, 2, 3], [1, 2, 3], 3),
    ([10, 20], [5, 15], 1),
    ([1], [1], 1),
    ([1, 2, 3], [2, 3, 4], 3),
    ([5, 10, 15], [10, 20, 30], 3),
    ([1, 1, 1], [1, 1, 1], 3),
    ([100, 200], [150, 250], 2),
    ([1, 2], [3, 4], 2),
    ([1, 2, 3], [1, 2, 3, 4], 3),
    ([5, 6, 7], [8, 9, 10], 3),
    ([10, 20, 30], [20, 30, 40], 3),
    ([1, 2, 3], [0, 1, 2], 2),
]
for i in cases:
    assert obj(*i[:-1]) == i[-1], f"Failed for case {i}"
else:
    print("All test cases passed!")