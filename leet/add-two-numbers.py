# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        lresult = ListNode(0)
        dummy = lresult
        carry = 0
    
        while True:
            l3 = ListNode((l1.val + l2.val + carry)%10)
            carry = (l1.val + l2.val + carry)//10
            
            dummy.next = l3
            dummy = l3

            if not l1.next and not l2.next and not carry: break
            l1 = l1.next or ListNode(0)
            l2 = l2.next or ListNode(0)
        return lresult.next
