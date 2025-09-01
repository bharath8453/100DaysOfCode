class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        first = second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

def create_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

head = create_list([1,2,3,4,5])
n = 2
new_head = Solution().removeNthFromEnd(head, n)
print(to_list(new_head))