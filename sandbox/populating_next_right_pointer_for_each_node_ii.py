# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return

        head_l = root
        while head_l:
            curr = head_l
            head_l, prev_l = None, None
            while curr:
                if curr.left:
                    if prev_l:
                        prev_l.next = curr.left
                    else:
                        head_l = curr.left
                    prev_l = curr.left
                if curr.right:
                    if prev_l:
                        prev_l.next = curr.right
                    else:
                        head_l = curr.right
                    prev_l = curr.right

                curr = curr.next
        return root
