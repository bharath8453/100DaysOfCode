arr = [10, 20, 25, 30, 40]
y = 2  # Index of element to delete (this will remove 25)

# Create a new list with one less element
new_arr = [0] * (len(arr) - 1)

# Copy elements except the one at index y
for i in range(len(new_arr)):
    if i < y:
        new_arr[i] = arr[i]
    else:
        new_arr[i] = arr[i + 1]

print("New list after deletion:", new_arr)