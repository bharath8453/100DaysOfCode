def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)

    # Base case: if the array has 1 or 0 elements, it's already sorted
    if n <= 1:
        return

    # Sort the first n-1 elements recursively
    recursive_insertion_sort(arr, n - 1)

    # Insert the nth element into the sorted part
    last = arr[n - 1]
    j = n - 2

    # Move elements one step ahead to make space
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last

# Example usage
numbers = [4, 2, 7, 1, 3]
print("Before sorting:", numbers)

recursive_insertion_sort(numbers)

print("After sorting:", numbers)