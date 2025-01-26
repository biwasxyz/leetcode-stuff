class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
    
        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if the current number's complement is in the map
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of the two numbers
            
            # Otherwise, add the current number and its index to the map
            num_map[num] = i