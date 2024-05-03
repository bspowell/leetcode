# Given only head of sorted linked list, delete dupes.
# return linked list sorted
# eg. head = [1,1,2], return [1,2]
# 
# Algo:
# 


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        
        if self.head is None:
          self.head = new_node
          return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def removeDups(self):
        temp = self.head

        while temp.next:
            if temp.value == temp.next.value:
              temp.next = temp.next.next
        return temp
    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

list = LinkedList()

list.add(1)
list.add(2)
list.add(2)
list.add(3)

print(print())

# node = Node(2)
# print(node.value)
# print(node.next)