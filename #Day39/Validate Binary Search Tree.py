class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True 

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False

            if not helper(node.left, lower, val):
                return False

            return True

        return helper(root)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print(Solution().isValidBST(root1))

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(Solution().isValidBST(root2)) 