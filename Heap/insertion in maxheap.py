class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        # Insert the new value at the end of the heap
        self.heap.append(val)

        # Bubble up the value to restore the max-heap property
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # While the current node is not the root and its value is greater than its parent's value
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                # Swap the current node with its parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index  # Move to the parent's index
            else:
                break  # The heap property is restored

    def __str__(self):
        return str(self.heap)


# Example usage:
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
max_heap.insert(30)

print("Max heap:", max_heap)
