class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementDict = {}
        for index, num in enumerate(nums):
            complement = target - num #complement is the value needed to reach the sum

            if complement in complementDict:
                return [complementDict[complement], index]
            
            complementDict[num] = index
        
        return []

