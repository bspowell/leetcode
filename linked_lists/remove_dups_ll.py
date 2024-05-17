# Given only head of sorted linked list, delete dupes.
# return linked list sorted
# eg. head = [1,1,2], return [1,2]
# 
# Algo:
# 


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def deleteDuplicates(self, head):
#         if not head or not head.next:
#             return head

#         dummy = ListNode(0)
#         dummy.next = head
#         prev = dummy
#         current = head

#         while current:
#             if prev.val == current.next.val:
#                 prev.next = current.next
#             else:
#               prev.next = current
#             current = current.next
            
#         return dummy.next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current is not None and current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))
solution = Solution()
new_head = solution.deleteDuplicates(head)

current = new_head
while current:
  print(current.val, end=" -> ")
  current = current.next
