from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtree_count = [0] * n
        subtree_sum_dist = [0] * n

        def dfs(node, parent):
            count, sum_dist = 1, 0
            for child in graph[node]:
                if child != parent:
                    child_count, child_sum_dist = dfs(child, node)
                    count += child_count
                    sum_dist += child_count + child_sum_dist
            subtree_count[node] = count
            subtree_sum_dist[node] = sum_dist
            return count, sum_dist

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    subtree_sum_dist[child] = subtree_sum_dist[node] - subtree_count[child] + (n - subtree_count[child])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)

        return subtree_sum_dist

# Example usage:
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
solution = Solution()
print(solution.sumOfDistancesInTree(n, edges))  # Output: [8, 12, 6, 10, 10, 10]
