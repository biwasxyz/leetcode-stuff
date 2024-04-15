# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def answer(node,sum):
            if not node:
                return 0
            sum = sum * 10 + node.val
            if not node.left and not node.right:
                return sum
            return answer(node.left, sum) + answer(node.right, sum)
        return answer(root, 0)
        