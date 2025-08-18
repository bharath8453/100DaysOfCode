class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next        
            fast = fast.next.next   
            if slow == fast:
                return True
        return False

def createLinkedList(values, pos):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        new_node = ListNode(val)
        nodes.append(new_node)
        current.next = new_node
        current = new_node
    
    if pos != -1:
        current.next = nodes[pos]
    
    return head

head = createLinkedList([3,2,0,-4], 1)
print(Solution().hasCycle(head))