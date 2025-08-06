def bubble_sort(arr):
    n = len(arr)

    # Go through the list n-1 times
    for i in range(n - 1):
        # Compare each pair of elements
        for j in range(n - 1 - i):
            # Swap if the element is bigger than the next one
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
print("Before sorting:", numbers)

bubble_sort(numbers)

print("After sorting:", numbers)