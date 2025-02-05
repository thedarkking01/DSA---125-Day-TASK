#Problem link = https://www.naukri.com/code360/problems/build-min-heap_1171167?leftPanelTab=0&utm_source=youtube&utm_medium=affiliate&utm_campaign=Lovebabbar&leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *

def buildMinHeap(arr):
    n = len(arr)
    
    # Bottom-up heap construction (iterative approach)
    for i in range(n // 2 - 1, -1, -1):  # Start from the last non-leaf node
        current = i
        while current < n:
            left = 2 * current + 1
            right = 2 * current + 2
            smallest = current
            
            # Check if left child exists and is smaller than current node
            if left < n and arr[left] < arr[smallest]:
                smallest = left
                
            # Check if right child exists and is smaller than current node
            if right < n and arr[right] < arr[smallest]:
                smallest = right
                
            # If current node is not the smallest, swap and continue with the smallest
            if smallest != current:
                arr[current], arr[smallest] = arr[smallest], arr[current]
                current = smallest
            else:
                break
    
    return arr
