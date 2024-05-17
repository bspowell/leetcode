import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Fast and Slow pointers
class Solution(object):
    def isPalindrome(self, head):
        fast = head
        slow = head

        # find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half 
        prev = None
        while slow: 
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


# solution with an array
# class Solution(object):
#     def isPalindrome(self, head):
#         current = head
#         arr = []
        
#         while current:
#             arr.append(current.val)
#             current = current.next

#         left, right = 0, len(arr) - 1

#         while left <= right:
#             if arr[left] != arr[right]:
#                 return False
#             left += 1
#             right -= 1
        
#         return True

nodelist = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
sol = Solution()
print(sol.isPalindrome(nodelist))