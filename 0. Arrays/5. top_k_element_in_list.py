


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ## create a count hashmap and store the values
        store_map = {}
        freq = [[] for c in range(len(nums)+1)]
        for n in nums :
            store_map[n] = 1 + store_map.get(n,0)
        
        for key , val in store_map.items():
            freq[val].append(key)

        # freq = [[], [1], [2], [3], [], [], []]
        res = []
        for i in range(len(freq)-1,0,-1) :
            for n in freq[i] :
                res.append(n)
                if len(res) == k :
                    return res 
