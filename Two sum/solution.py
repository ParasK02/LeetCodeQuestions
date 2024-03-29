class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i in range(len(nums)):
            if target-nums[i] in table:
                return [table[target-nums[i]],i]
            else:
                table[nums[i]]=i
            
        return None 
