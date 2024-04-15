class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxWealth = 0
        for customers in accounts:
            currentWealth = 0
            for banks in customers:
                currentWealth += banks
            maxWealth = max(maxWealth, currentWealth)
        return maxWealth
        
        