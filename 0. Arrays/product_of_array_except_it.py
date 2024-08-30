class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs = [1] * len(nums)
        for i in range(1,len(nums)):
            rs[i] = rs[i-1] * nums[i-1]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            rs[i] *=postfix
            postfix *=nums[i]
        return rs
    
print(Solution().productExceptSelf([1,2,3,4])  )