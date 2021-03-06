# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[][]}
def level_order(root)
    dfs(root, 0, [])
end

def dfs(root, level, res)
    return res if !root # Ends up returning everything at the bottom of the tree
    res[level] ||= []
    res[level] << root.val
    dfs(root.left, level + 1, res)
    dfs(root.right, level + 1, res)
end