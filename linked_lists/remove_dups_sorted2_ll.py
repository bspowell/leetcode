
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.val == curr.next.val:
                    curr = curr.next
                    if curr.next is None:
                        break
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
            
        return dummy.next



# tony

    # if not head:
    #     return head
    
    # curr = head

    # while curr:
    #     if curr.next and curr.next.val == curr.val:
    #         curr.next = curr.next.next
    #     else:
    #         curr = curr.next
    
    # return head
    
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
sol = Solution()

printHead = sol.deleteDuplicates(ll)

while printHead:
  print(printHead.val, end=" -> ")
  printHead = printHead.next