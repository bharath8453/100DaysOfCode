class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def buildTree(values):
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

sol = Solution()

p = buildTree([1, 2, 3])
q = buildTree([1, 2, 3])
print(sol.isSameTree(p, q))  

p = buildTree([1, 2])
q = buildTree([1, None, 2])
print(sol.isSameTree(p, q)) 

p = buildTree([1, 2, 1])
q = buildTree([1, 1, 2])
print(sol.isSameTree(p, q))