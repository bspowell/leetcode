class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return head
        
        odd = head
        even = mover = head.next

        while odd.next and mover.next:
            odd.next = odd.next.next
            mover.next = mover.next.next
            odd = odd.next
            mover = mover.next
            
        odd.next = even

        return head


nodelist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()

new_ll = sol.oddEvenList(nodelist)

while new_ll:
    print(new_ll.val, end='->')
    new_ll = new_ll.next