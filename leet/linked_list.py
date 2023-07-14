# CRAZY LINKED LISTS
#
class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

a = b = Node()
for i in "abcde":
  a.next = Node(i)
  a = a.next

print(b.next.next.val)
