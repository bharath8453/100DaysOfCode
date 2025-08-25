class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sort to enable two-pointer approach
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate first numbers

            left, right = i + 1, n - 1  # Two pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])  # Found a triplet

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate left values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate right values

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # Need a larger sum
                else:
                    right -= 1  # Need a smaller sum

        return result

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4])) 
print(sol.threeSum([0,1,1])) 
print(sol.threeSum([0,1,1])) 