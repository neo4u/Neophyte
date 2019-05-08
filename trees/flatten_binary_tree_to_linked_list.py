# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None

            while root.right:
                root = root.right

            root.right = temp

class Solution:
    def flatten(self, root):
        if not root: return

        self.flatten(root.right)
        tmp = root.right

        if not root.left: return
        self.flatten(root.left)
        tail = root.left

        while tail.right: tail = tail.right

        root.right = root.left
        root.left = None
        tail.right = tmp
