#link = https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=introduction-to-doubly-linked-list
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        if not arr:
            return None
        head=Node(arr[0])
        cur=head
        for i in range(1, len(arr)):
             newnode=Node(arr[i])
             cur.next=newnode
             newnode.prev=cur
             cur=newnode
        return head