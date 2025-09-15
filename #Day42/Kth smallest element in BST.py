class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

def buildTree(values):
    if not values or values[0] is None:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

root1 = buildTree([3,1,4,None,2])
k1 = 1
print("Example 1 Output:", Solution().kthSmallest(root1, k1)) 

root2 = buildTree([5,3,6,2,4,None,None,1])
k2 = 3
print("Example 2 Output:", Solution().kthSmallest(root2, k2))