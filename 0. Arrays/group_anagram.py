

from collections import defaultdict , UserList

class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    

sol = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])

print(sol)