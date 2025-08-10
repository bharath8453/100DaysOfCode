class Node:
      #A single node in a linked list
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    #Single Linked List with insert & delete operations
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        #Insert a node at the given position (1-based index)
        new_node = Node(data)

        # If inserting at the head
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        # Find the node before the desired position
        current = self.head
        for _ in range(position - 2):
            if current is None:
                print("Position out of range")
                return
            current = current.next

        # Insert the new node
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position):
        #Delete the node at the given position (1-based index)
        if self.head is None:
            print("List is empty")
            return

        # If deleting the head
        if position == 1:
            self.head = self.head.next
            return

        # Find the node before the one to delete
        current = self.head
        for _ in range(position - 2):
            if current is None or current.next is None:
                print("Position out of range")
                return
            current = current.next

        # Delete the node
        if current.next is None:
            print("Position out of range")
        else:
            current.next = current.next.next

    def display(self):
        """Print all nodes in the linked list"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert_at_position(10, 1)  # 10
ll.insert_at_position(20, 2)  # 10 -> 20
ll.insert_at_position(30, 2)  # 10 -> 30 -> 20
ll.display()

ll.delete_at_position(2)      # Delete '30'
ll.display()