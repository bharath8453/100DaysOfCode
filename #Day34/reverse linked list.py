class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr      
            curr = nxt      
            
        return prev

def build_linked_list(nums):
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

l1 = build_linked_list([1,2,3,4,5])
sol = Solution()
result = sol.reverseList(l1)
print(linked_list_to_list(result))