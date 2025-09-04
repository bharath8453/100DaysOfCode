def trap(height):
    # Edge case: If the array is too short, no water can be trapped
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    # Two-pointer approach
    while left < right:
        if height[left] < height[right]:
            # If current left is smaller, process left side
            if height[left] >= left_max:
                left_max = height[left]  # Update left max
            else:
                water_trapped += left_max - height[left]  # Add trapped water
            left += 1
        else:
            # Process right side
            if height[right] >= right_max:
                right_max = height[right]  # Update right max
            else:
                water_trapped += right_max - height[right]  # Add trapped water
            right -= 1

    return water_trapped


print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) 
print(trap([4,2,0,3,2,5]))  
