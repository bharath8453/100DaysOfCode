def insertion_sort(numbers):
    # Start from the second element (index 1)
    for i in range(1, len(numbers)):
        current = numbers[i]      # The number we want to insert
        position = i - 1

        # Shift elements to the right to make space
        while position >= 0 and numbers[position] > current:
            numbers[position + 1] = numbers[position]
            position -= 1

        # Insert the current number at the correct position
        numbers[position + 1] = current

# Example usage
my_list = [5, 3, 8, 1, 2]
print("Before sorting:", my_list)

insertion_sort(my_list)

print("After sorting:", my_list)