# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l = self.length(head)
        dummy = ListNode(None)
        dummy.next = head
        
        node_before_rev_sublist = dummy
        while l >= k:
            j = k
            prev = None
            curr = node_before_rev_sublist.next
            while j > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                j -= 1
                
            end_of_sublist = node_before_rev_sublist.next
            node_before_rev_sublist.next = prev
            end_of_sublist.next = curr
            node_before_rev_sublist = end_of_sublist
            
            l -= k
            
        return dummy.next
        
    def length(self, head):
        l = 0
        curr = head
        while curr:
            l +=1 
            curr = curr.next
            
        return l