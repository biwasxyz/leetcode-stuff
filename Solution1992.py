class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(row, col):
            # Mark the current cell as visited
            land[row][col] = -1
            # Update top-left and bottom-right coordinates of the group
            group[0] = min(group[0], row)
            group[1] = min(group[1], col)
            group[2] = max(group[2], row)
            group[3] = max(group[3], col)
            # Explore four neighboring cells
            for drow, dcol in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + drow, col + dcol
                if 0 <= new_row < m and 0 <= new_col < n and land[new_row][new_col] == 1:
                    dfs(new_row, new_col)

        m, n = len(land), len(land[0])
        groups = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    group = [i, j, i, j]  # Initialize group coordinates
                    dfs(i, j)
                    groups.append(group)

        return groups

