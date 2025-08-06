def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)

    # Base case: if only one element, return
    if n == 1:
        return

    # One pass: bubble the largest to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call for the remaining unsorted part
    bubble_sort_recursive(arr, n - 1)

# Example usage
numbers = [4, 2, 7, 1, 3]
print("Before sorting:", numbers)

bubble_sort_recursive(numbers)

print("After sorting:", numbers)