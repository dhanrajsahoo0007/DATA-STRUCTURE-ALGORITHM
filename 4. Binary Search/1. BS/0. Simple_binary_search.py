class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0 
        r = len(nums)-1
        while l<=r :
            m = l + ((r-l)//2) # (l + r) // 2 can lead to overflow in programming languages like java and others because of the int restriction
            if nums[m] == target:
                return m 
            elif nums[m] > target :
                r = m-1 
            else :
                l = m+1
        return -1


input_list = [-1,0,3,5,9,12]
target = 30
print(Solution().search(input_list,target))