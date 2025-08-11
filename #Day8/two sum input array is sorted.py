class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # +1 because the array is 1-indexed
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1  # Need a bigger sum
            else:
                right -= 1  # Need a smaller sum

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # [1, 2]
print(sol.twoSum([2, 3, 4], 6))
print(sol.twoSum([-1,0], -1))