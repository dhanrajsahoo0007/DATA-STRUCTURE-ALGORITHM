"""
140. Word Break II

Hard
Topics
Companies
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        results = []
        n = len(s)

        def dfs(starting_index: int, path: List[str]):
            if starting_index == n:
                results.append(" ".join(path))
                return
            for word in wordDict:
                if s[starting_index:].startswith(word):
                    path.append(word)
                    dfs(starting_index+len(word), path)
                    path.pop()
            return
        dfs(0,[])
        return results