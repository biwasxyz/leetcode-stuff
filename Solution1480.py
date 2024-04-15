class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = [0] * len(nums)
        results[0] = nums[0]
        for i in range(1, len(nums)):
            results[i] = nums[i] + results[i-1]
        return results
        