class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         count = 0 
#         countNode = head
#         while countNode:
#             count += 1
#             countNode = countNode.next 
        
#         dummy = ListNode(0, head)
#         prev, curr = dummy, head

#         for i in range(count):
#             if i == (count - n):
#                 prev.next = curr.next
#             else:
#                 prev = curr
#                 curr = curr.next
        
#         return dummy.next 

class Solution(object):
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0, head)
        prev, curr = dummy.next, head

        for i in range(n):
            curr = curr.next
        print(curr.val)

        while curr:
            prev = prev.next
            curr = curr.next 
        
        prev.next = prev.next.next
        
        return dummy.next 


nodelist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()

new_ll = sol.removeNthFromEnd(nodelist, 2)

while new_ll:
    print(new_ll.val, end='->')
    new_ll = new_ll.next



#     # neetcode answer
# def removeNthFromEnd(head, n):
#     dummy = ListNode(0, head)
#     left = dummy
#     right = head

#     while n > 0 and right:
#         right = right.next
#         n -= 1

#     while right:
#         left = left.next
#         right = right.next

#     left.next = left.next.next

#     return dummy.next

# TONY
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         """
        
#         """
#         if not head.next:
#             return None

#         dummy = ListNode()
#         dummy.next = head

#         fast = dummy
#         slow = dummy
#         count = 0

#         while fast:
#             count += 1
#             fast = fast.next

#             if count > n + 1:
#                 slow = slow.next
        
#         slow.next = slow.next.next

#         return dummy.next