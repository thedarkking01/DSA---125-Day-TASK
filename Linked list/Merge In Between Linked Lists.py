# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur=list1
        i=0
        while i<a-1:
            cur=cur.next
            i+=1
        
        head=cur
        while i<=b:
            cur=cur.next
            i+=1
        head.next=list2
        while list2.next:
            list2=list2.next
        list2.next=cur
        return list1