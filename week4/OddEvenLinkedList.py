# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        last_odd = head
        first_even = head.next
        
        curr = head
        odd_pos = True
        while curr:
            if odd_pos:
                last_odd = curr
            temp = curr.next
            curr.next = None if not temp else temp.next
            
            curr = temp
            odd_pos = not odd_pos
            
        last_odd.next = first_even
        return head
            