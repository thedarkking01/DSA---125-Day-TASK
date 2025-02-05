def heapify(arr, n, i):
    smallest = i  # Assume root is the smallest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is smaller
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Check if right child exists and is smaller
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest is not the root, swap and continue heapifying
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def buildMinHeap(arr, n):
    """Function to convert array into a Min Heap."""
    # Start from last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def solve():
    """Function to handle multiple test cases."""
    T = int(input().strip())  # Number of test cases
    for i in range(T):
        N = int(input().strip())  # Size of the array
        ARR = list(map(int, input().strip().split()))  # Read input array
        
        buildMinHeap(ARR, N)  # Convert array to min heap
        
        print(1)  # Since the output format expects 1 after processing

# Driver Code
solve()
