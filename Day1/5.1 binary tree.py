# Node structure
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary Tree structure
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a node (level order for binary tree, not BST)
    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # Inorder traversal (Left, Root, Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    # Preorder traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')

    # Search for a value
    def search(self, key):
        if self.root is None:
            return False
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if temp.key == key:
                return True
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return False


# ----------- Example Usage -------------
if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(20)
    bt.insert(30)
    bt.insert(40)
    bt.insert(50)

    print("Inorder traversal:")
    bt.inorder(bt.root)

    print("\nPreorder traversal:")
    bt.preorder(bt.root)

    print("\nPostorder traversal:")
    bt.postorder(bt.root)

    print("\n\nSearch for 30:", "Found" if bt.search(30) else "Not Found")
    print("Search for 100:", "Found" if bt.search(100) else "Not Found")