class Solution(object):
    def tribonacci(self, n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        tribonacci_nums = [0] * (n + 1)
        tribonacci_nums[0] = 0
        tribonacci_nums[1] = 1
        tribonacci_nums[2] = 1
        
        for i in range(3, n + 1):
            tribonacci_nums[i] = tribonacci_nums[i - 1] + tribonacci_nums[i - 2] + tribonacci_nums[i - 3]
        
        return tribonacci_nums[n]
