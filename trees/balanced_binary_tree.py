# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root)[0]

    def dfs(self, node):
        if not node: return True, 0

        l_bool, l_depth = self.dfs(node.left)
        if not l_bool: return False, None

        r_bool, r_depth = self.dfs(node.right)
        if not r_bool: return False, None

        return abs(l_depth - r_depth) <= 1, max(l_depth, r_depth) + 1


# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

# For everysub-tree, we return:
# 1. the truth value of is the sub-tree is height balanced or not
# 2. the max depth of the sub-tree
