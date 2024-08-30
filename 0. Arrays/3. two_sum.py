class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        storage = {}

        for i in range(len(nums)) :
            diff = target-nums[i]
            if diff in storage:
                return [storage[diff],i] 
            storage[nums[i]] = i


