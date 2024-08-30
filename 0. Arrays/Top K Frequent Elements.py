class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        countS = {}

        for i in range(len(nums)):
            print(i)
            countS[nums[i]] = 1 + countS.get(nums[i], 0)

        # sorted_dict = dict(sorted(countS.items()))
        # Step 2: Sort the dictionary items based on frequency in descending order.
        sorted_dict = sorted(countS.items(), key=lambda item: item[1], reverse=True)
        count = 0 
        val_list=[]
        for ele,val in sorted_dict:
            count = count+1
            val_list.append(ele)
            if k == count :
                return val_list



val = Solution().topKFrequent([1,1,1,1,2,3,3,3],2)

print(val)