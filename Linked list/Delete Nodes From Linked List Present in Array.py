# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# by single pointer
# class Solution:
#     def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
#         dummy=ListNode(0,head)
#         nums=set(nums)
#         prev=dummy
#         while prev.next:
#             if prev.next.val in nums:
#                 prev.next=prev.next.next
#             else:
#                 prev=prev.next
#         return dummy.next

# by two pointers
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        nums=set(nums)
        prev=dummy
        cur=head
        while cur:
            if cur.val in nums:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return dummy.next