class Solution(object):
    def smallestFromLeaf(self, root):
        '''
        :type root: TreeNode
        :rtype:str
        '''
        if not root:
            return ""
        
        # Helper function for DFS traversal
        def dfs(node, path):
            if not node:
                return

            # convert the node value to corresponding character
            ch = chr(node.val + ord('a'))

            # append the character to the path
            path.append(ch)

            # if it's a leaf node, construct the string and compare
            if not node.left and not node.right:
                # reverse the path to form the string from leaf to root
                curr_str = ''.join(path[::-1])

                # update the smallest string found so far
                if not self.smallest or curr_str < self.smallest:
                    self.smallest = curr_str

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        self.smallest = None
        dfs(root, [])
        return self.smallest
