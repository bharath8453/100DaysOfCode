def selection_sort(numbers):
    n = len(numbers)

    # Move through the list one by one
    for i in range(n):
        # Assume the current index has the smallest number
        min_index = i

        # Find the smallest number in the remaining list
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        # Swap the smallest with the current position
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Example usage
my_list = [5, 3, 8, 1, 2]
print("Before sorting:", my_list)

selection_sort(my_list)

print("After sorting:", my_list)