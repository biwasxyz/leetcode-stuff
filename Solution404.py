class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def isLeaf(node):
            return node and not node.left and not node.right
        
        def dfs(node, is_left):
            if not node:
                return 0
            if isLeaf(node) and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root.left, True) + dfs(root.right, False) if root else 0