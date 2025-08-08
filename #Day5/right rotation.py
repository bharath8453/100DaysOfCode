arr = [10, 20, 30, 40, 50]
n = 2  # Number of times to rotate

length = len(arr)
n = n % length  # To handle if n is bigger than length

for _ in range(n):
    last = arr[-1]  # Save the last element

    # Shift elements to the right
    for i in range(length - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last  # Put last element at the front

print("After right rotation:", arr)