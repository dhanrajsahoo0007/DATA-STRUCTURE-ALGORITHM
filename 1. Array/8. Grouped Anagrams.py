import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_map = collections.defaultdict(list)
        
        for string in strs :
            counts = [0]*26
            for c in string:
                counts[ord(c)-ord("a")] += 1
            str_map[tuple(counts)].append(string)
        return str_map.values()
    
input = ["act","pots","tops","cat","stop","hat"]   

print(Solution().groupAnagrams(strs=input))

# (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0):['act', 'cat']
# (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0):['pots', 'tops', 'stop']
# (1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0):['hat']

# output =  dict_values([['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']])


