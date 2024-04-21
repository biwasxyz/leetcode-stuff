class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        # Build adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Perform DFS
        visited = set()
        return self.dfs(source, destination, graph, visited)
    
    def dfs(self, current, destination, graph, visited):
        if current == destination:
            return True
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                if self.dfs(neighbor, destination, graph, visited):
                    return True
        return False


