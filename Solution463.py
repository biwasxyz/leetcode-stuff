class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4  # Start with the assumption of 4 sides for each land cell
                    # Check each adjacent cell, subtracting 1 from perimeter for each adjacent land cell
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter

# Test cases
sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # Output: 16
print(sol.islandPerimeter([[1]]))  # Output: 4
print(sol.islandPerimeter([[1,0]]))  # Output: 4
