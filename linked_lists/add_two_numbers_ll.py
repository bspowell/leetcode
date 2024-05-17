

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head1 = l1
        head2 = l2
        sum1 = ''
        sum2 = ''

        while head1:
            sum1 = str(head1.val) + sum1
            head1 = head1.next
        while head2:
            sum2 = str(head2.val) + sum2
            head2 = head2.next
        
        total = int(sum1) + int(sum2)
        total = str(total)

        curr = ListNode(0)
        dummy = curr

        for i in range(len(total) -1, -1, -1):
            curr.next = ListNode(int(total[i]))
            curr = curr.next
        
        return dummy.next


nodelist = ListNode(2, ListNode(4, ListNode(3)))
nodelist2 = ListNode(5, ListNode(6, ListNode(4)))
sol = Solution()

new_ll = sol.addTwoNumbers(nodelist, nodelist2)

while new_ll:
    print(new_ll.val, end='->')
    new_ll = new_ll.next

#Time complexity:
#  time complexity of O(n1+n2) - maybe 0(n1 + n2 + n3)
