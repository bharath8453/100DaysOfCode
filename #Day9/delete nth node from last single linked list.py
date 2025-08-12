class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        fast, slow = fast.next, slow.next

    # Delete the node
    slow.next = slow.next.next
    return dummy.next

# Helper to print list
def show(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Before:")
show(head)

head = delete_nth_from_end(head, 2)
print("After:")
show(head)