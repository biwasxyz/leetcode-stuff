from collections import defaultdict

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]  # If there's only one node, it's the root of MHT
        
        # Initialize adjacency list representation of the tree
        adj_list = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        # Find initial leaves (nodes with only one edge)
        leaves = [node for node in range(n) if len(adj_list[node]) == 1]
        
        # Iteratively remove leaves until MHT roots are reached
        while n > 2:
            n -= len(leaves)  # Update total nodes count after removing leaves
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()  # Remove edge from the leaf
                adj_list[neighbor].remove(leaf)  # Remove edge from the neighbor
                if len(adj_list[neighbor]) == 1:  # Check if the neighbor becomes a leaf
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves  # Remaining leaves are the roots of MHTs
