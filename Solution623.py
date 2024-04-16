# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
    def addOneRow(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, level):
            if not node:
                return
            if level == depth - 1:
                left_child = TreeNode(val)
                right_child = TreeNode(val)
                left_child.left = node.left
                right_child.right = node.right
                node.left = left_child
                node.right = right_child
            else:
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
        
        dfs(root, 1)
        return root
