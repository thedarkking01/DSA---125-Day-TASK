def sum_array(arr):
    if not arr:  # Base case: if the array is empty
        return 0
    else:
        return arr[0] + sum_array(arr[1:])  # Recursive case: sum the first element and the rest of the array