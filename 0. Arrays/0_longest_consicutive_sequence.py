## tried the base approach with sorting the array 


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_list = sorted(nums)
        current_len = 1
        max_len= 1
        for i in range(len(sorted_list)) :
            if sorted_list[i] == sorted_list[i-1]+1:
                current_len +=1
            else:
                current_len = 1
            
            max_len = max(max_len,current_len)

        return max_len
    
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))