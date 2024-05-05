class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev






nodelist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
