class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next

            if slow == fast:
                return True
            

        return False


ls = ListNode

sol = Solution()
result =  print(sol.hasCycle(ls))