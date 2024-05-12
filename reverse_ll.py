class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        start = prev
        end = curr 

        while curr and curr.next:
            if curr.val == left:
                start = prev 
                while curr.val != right:
                    print('curr', curr.val)
                    print('prev', prev.val)

                    nex = curr.next 
                    curr.next = prev
                    prev = curr
                    curr = nex

                    print('curr2', curr.val)
                    print('prev2', prev.val)
                end = curr.next
                end.next = start.next
                start.next = curr
                print('start', start.val)
                print('end', end.val)
                print('curr', curr.val)
                print('prev', prev.val)
            else:
                prev = curr
                curr = curr.next
                
        return dummy.next


# # leetcode
#     def reverseList(self, head, left, right):
#         dummy = ListNode(0, head)

#         leftPrev, cur = dummy, head
#         for i in range(left - 1):
#             leftPrev, cur = cur, cur.next

#         prev = None
#         for i in range(right - left + 1):
#             tmpNext = cur.next 
#             cur.next = prev
#             prev, cur = cur, tmpNext

#         leftPrev.next.next = cur
#         leftPrev.next = prev
#         return dummy.next 



nodelist = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()

new_ll = sol.reverseList(nodelist, 2, 4)

while new_ll:
    print(new_ll.val, end='->')
    new_ll = new_ll.next
