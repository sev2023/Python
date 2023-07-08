# https://leetcode.com/problems/add-two-numbers/solution/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        lresult = ListNode(0)
        dummy = lresult
    
        while True:
            l3 = ListNode(l1.val + l2.val)
            
            dummy.next = l3
            print(dummy)
            dummy = l3
            print(dummy, lresult)
            print(l1.val, l2.val)
            if not l1.next or not l2.next: break
            l1 = l1.next
            l2 = l2.next
        return lresult.next
