
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        # iterate over lists while both nodes are not None
        while list1 and list2:
            if list1.val < list2.val:
              tail.next = list1
              list1 = list1.next
            else: # if list 2 val <= list 1 val
              tail.next = list2
              list2 = list2.next

            tail = tail.next
        
        # if list1, make next node point to the current node on list1 (which points to the rest of the ll)
        # if list2, make next node point to the current node on list2
        if list1:
            tail.next = list1 
        elif list2:
            tail.next = list2
        

        return dummy.next 





list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
new_l = sol.mergeTwoLists(list1, list2)

while new_l:
  print(new_l.val, end='->')
  new_l = new_l.next

# iterate over one ll
#   if curr1 
# if the pointer from one list's value is 