def maxSubArray(nums):
    current_sum = max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  
print(maxSubArray([1]))                    
print(maxSubArray([5,4,-1,7,8])) 

''' dry run-- for example1:
current_sum = -2, max_sum = -2
num = 1  → current_sum = max(1, -2+1) = 1, max_sum = 1
num = -3 → current_sum = max(-3, 1-3) = -2, max_sum = 1
num = 4  → current_sum = max(4, -2+4) = 4, max_sum = 4
num = -1 → current_sum = max(-1, 4-1) = 3, max_sum = 4
num = 2  → current_sum = max(2, 3+2) = 5, max_sum = 5
num = 1  → current_sum = max(1, 5+1) = 6, max_sum = 6
num = -5 → current_sum = max(-5, 6-5) = 1, max_sum = 6
num = 4  → current_sum = max(4, 1+4) = 5, max_sum = 6
'''