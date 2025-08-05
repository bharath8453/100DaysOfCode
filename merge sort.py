def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2
    left_half = merge_sort(arr[:middle_index])
    right_half = merge_sort(arr[middle_index:])

    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    # Add remaining elements from both halves
    merged += left_half[left_index:]
    merged += right_half[right_index:]

    return merged

# Example usage
arr = [8, 4, 7, 3, 10, 1]
sorted_arr = merge_sort(arr)
print("Merge Sort:", sorted_arr)