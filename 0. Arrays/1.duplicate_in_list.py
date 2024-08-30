class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    



input_list = [-1,0,3,3,3,5,9,12]
target = 30
print(Solution().containsDuplicate(input_list))