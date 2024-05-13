class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverse(self, head, left, right):
        dummy = ListNode(0, head)
        start = dummy
        prev = dummy
        curr = head

        leftNode = dummy
        rightNode = dummy

        while curr.next:
            start = prev
            prev = curr
            curr = curr.next
            # if prev value equals left value
            if prev.val == left:
                leftNode = prev
                # while prev val doesn't equal right value, reverse nodes
                while prev.val != right:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt
                rightNode = prev
        
        # point starting node
        start.next = rightNode
        leftNode.next = curr

        return head


ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
left = 2
right = 4
sol = Solution()

result = sol.reverse(ll, left, right)

while result:
    print(result.val, end='->')
    result = result.next