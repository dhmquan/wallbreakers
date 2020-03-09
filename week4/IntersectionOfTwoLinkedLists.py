# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = self.length(headA)
        lenB = self.length(headB)

        longerList = None
        shorterList = None
        if lenA > lenB:
            longerList = headA
            shorterList = headB
        else:
            longerList = headB
            shorterList = headA
            
        diff = abs(lenA - lenB)
        
        while diff > 0:
            longerList = longerList.next
            diff -= 1
            
        while longerList and shorterList:
            if longerList is shorterList:
                return longerList
            
            longerList = longerList.next
            shorterList = shorterList.next
        
        return None
        
    def length(self, head):
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
            
        return l