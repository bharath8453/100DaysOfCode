def recursive_selection_sort(arr, start=0):
    n = len(arr)

    # Base case: if start reaches the end, stop
    if start >= n - 1:
        return

    # Assume the smallest element is at 'start'
    min_index = start

    # Find the index of the smallest element from start to end
    for i in range(start + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    # Swap the smallest element with the first element in this pass
    arr[start], arr[min_index] = arr[min_index], arr[start]

    # Recursively call for the remaining part
    recursive_selection_sort(arr, start + 1)

# Example usage
numbers = [5, 3, 8, 1, 2]
print("Before sorting:", numbers)

recursive_selection_sort(numbers)

print("After sorting:", numbers)