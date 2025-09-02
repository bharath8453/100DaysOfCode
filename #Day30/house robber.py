class Solution(object):
    def rob(self, nums):
        if not nums:    # if no houses
            return 0
        if len(nums) == 1:    # if only 1 house
            return nums[0]

        prev1, prev2 = 0, 0    # prev1 = max money robbed up to previous house, prev2 = max money robbed up to the house before previous
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1) 
            prev2 = temp

        return prev1

nums = [2,7,9,3,1]
print(Solution().rob(nums))