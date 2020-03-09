# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        
        node_before_rev_sublist = dummy
        for _ in range(1, m):
            node_before_rev_sublist = node_before_rev_sublist.next
        
        prev = None
        curr = node_before_rev_sublist.next
        while n >= m:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1
            
        end_of_rev_sublist = node_before_rev_sublist.next
        end_of_rev_sublist.next = curr
        node_before_rev_sublist.next = prev
        
        return dummy.next
        