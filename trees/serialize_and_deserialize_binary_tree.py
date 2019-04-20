# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(root, ans):
            if root is None:
                ans.append("#")
                return
            ans.append(str(root.val))
            dfs(root.left, ans)
            dfs(root.right, ans)

        ans = []
        dfs(root, ans)
        astr = ",".join(ans)
        return astr

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(data, index):
            if index[0] >= len(data):
                return None
            val = data[index[0]]
            if val == '#':
                return None
            root = TreeNode(int(val))
            index[0] += 1
            root.left = dfs(data, index)
            index[0] += 1
            root.right = dfs(data, index)
            return root

        if not data:
            return None
        data = data.split(",")
        index = [0]
        return dfs(data, index)

# Approach 2: BFS pre-order / Iterative approach (Seems faster on LC inputs)
import collections
class Codec:
    def serialize(self, root):
        if not root: return []
        result = []
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if not node:
                result.append('#')
                continue
            else:
                result.append(str(node.val))
            que.extend([node.left, node.right])
        return ' '.join(result)

    def deserialize(self, data):
        if not data: return None
        iterData = iter(data.split(' '))
        root = TreeNode(next(iterData))
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if not node: continue
            val = next(iterData)
            node.left = TreeNode(int(val)) if val != '#' else None
            que.append(node.left)
            val = next(iterData)
            node.right = TreeNode(int(val)) if val != '#' else None
            que.append(node.right)
        return root


# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/

# Approach 1: DFS using pre-order
# Steps:
# 1. Serialize using pre-order traversal using depth first search and represent null by "#"
# 2. Deserialize by traversing the serialized tree and using recursion. O(n).

# Approach 2: BFS using queue and iterative approach and pre_order
# Time: O(n), visit n nodes once
# Space: O(n), store the entire tree in array and string

#     1
#    / \
#   2   3
#      / \
#     4   5

root = TreeNode(1)
l, r = TreeNode(2), TreeNode(3)
r1, r2 = TreeNode(4), TreeNode(5)
root.left, root.right = l, r
r.left, r.right = r1, r2

codec = Codec()
assert codec.serialize(root) == "1,2,#,#,3,4,#,#,5,#,#"
new_root = codec.deserialize("1,2,#,#,3,4,#,#,5,#,#")

assert new_root.val == root.val
assert new_root.left.val == l.val
assert new_root.right.val == r.val
assert new_root.right.left.val == r1.val
assert new_root.right.right.val == r2.val
