# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         stack = []
#         cur = head
        
#         # Traverse the list and maintain a decreasing stack
#         while cur:
#             while stack and cur.val > stack[-1]:
#                 stack.pop()
#             stack.append(cur.val)
#             cur = cur.next 

#         # Rebuild the list from the filtered values
#         dummy = ListNode()
#         cur = dummy
#         for val in stack:
#             cur.next = ListNode(val)
#             cur = cur.next
#         return dummy.next


#Reverse twice
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = prev
                prev, cur = cur, tmp
            return prev

        head = reverse(head)
        cur = head
        cur_max = head.val

        while cur and cur.next:
            if cur.next.val < cur_max:
                cur.next = cur.next.next
            else:
                cur_max = cur.next.val
                cur = cur.next
                
        return reverse(head)