arr = [10, 20, 30, 40, 50]
n = 2  # Number of times to rotate

length = len(arr)
n = n % length  # To handle cases where n is greater than length

for _ in range(n):
    first = arr[0]  # Save the first element

    # Shift elements to the left
    for i in range(0, length - 1):
        arr[i] = arr[i + 1]

    arr[-1] = first  # Put first element at the end

print("After left rotation:", arr)