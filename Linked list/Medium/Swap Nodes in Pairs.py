# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur=head
        # while cur and cur.next:
        #     cur.val,cur.next.val=cur.next.val,cur.val
        #     cur=cur.next.next
        # return head

        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            # saved pointers
            nxtpt=cur.next.next
            second=cur.next
            
            #reversed
            second.next=cur
            cur.next=nxtpt
            prev.next=second

            #update ptr
            prev=cur
            cur=nxtpt

        return dummy.next