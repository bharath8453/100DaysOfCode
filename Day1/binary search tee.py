class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insertNode(self, node, val):
        n = Node(val)
        if self.root is None:
            self.root = n
            print(f'Root node is added: {val}')
            return
        if val < node.val:
            if node.left is None:
                node.left = n
                print(f'Node {val} is added to the left of {node.val}')
            else:
                self.insertNode(node.left, val)
        else:
            if node.right is None:
                node.right = n
                print(f'Node {val} is added to the right of {node.val}')
            else:
                self.insertNode(node.right, val)

    # Inorder Traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

    # Preorder Traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=' ')

    # Search for a value
    def search(self, node, val):
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self.search(node.left, val)
        else:
            return self.search(node.right, val)

if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insertNode(bst.root, v)

    print("\nInorder Traversal:")
    bst.inorder(bst.root)

    print("\nPreorder Traversal:")
    bst.preorder(bst.root)

    print("\nPostorder Traversal:")
    bst.postorder(bst.root)

    print("\n\nSearch for 60:", "Found" if bst.search(bst.root, 60) else "Not Found")
    print("Search for 90:", "Found" if bst.search(bst.root, 90) else "Not Found")

