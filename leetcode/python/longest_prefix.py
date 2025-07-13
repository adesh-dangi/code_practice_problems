# https://leetcode.com/problems/longest-common-prefix/

List = list
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sort_ls = sorted(strs)
        ans = ""
        for ix, i in enumerate(sort_ls[0]):
            if i == sort_ls[-1][ix]:
                ans+=i
            else:
                break
        return ans

