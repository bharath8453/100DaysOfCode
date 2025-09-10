from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:   # left child
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:  # right child
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

sol = Solution()

root1 = build_tree([3,9,20,None,None,15,7])
print(sol.maxDepth(root1))   # Output: 3

root2 = build_tree([1,None,2])
print(sol.maxDepth(root2))