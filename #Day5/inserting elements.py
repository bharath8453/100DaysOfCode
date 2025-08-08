arr = [1,2,3,4,5]
x = 4
y = 2
new_list = [0]*(len(arr)+1)
for i in range(len(new_list)):
    if i < y:
        new_list[i] = arr[i]
    elif i==y:
        new_list[i] = x
    else:
        new_list[i] = arr[i-1]

print("new list",new_list)

'''arr = [10, 20, 30, 40]
x = 25
y = 2

# Make space for one extra element
new_arr = [0] * (len(arr) + 1)

# Copy elements and insert x at position y
for i in range(len(new_arr)):
    if i < y:
        new_arr[i] = arr[i]
    elif i == y:
        new_arr[i] = x
    else:
        new_arr[i] = arr[i - 1]

print("New list:", new_arr)'''
 