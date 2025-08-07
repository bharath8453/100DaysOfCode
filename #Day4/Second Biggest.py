def find_second_largest(nums):
    first = second = None

    for num in nums:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num

    return second

# Example
nums = [12, 45, 2, 41, 31]
print("Second largest is:", find_second_largest(nums))