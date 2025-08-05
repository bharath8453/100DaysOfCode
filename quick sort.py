def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # First element as pivot
    left = [x for x in arr[1:] if x < pivot]  # Elements smaller than pivot
    right = [x for x in arr[1:] if x >= pivot]  # Elements greater or equal to pivot

    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [8, 4, 7, 3, 10, 1]
sorted_arr = quick_sort(arr)
print("Quick Sort:", sorted_arr)