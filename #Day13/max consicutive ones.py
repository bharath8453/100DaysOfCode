class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0  # stores the maximum consecutive 1's found so far
        count = 0      # stores current streak of 1's

        for num in nums:
            if num == 1:
                count += 1           # continue streak
                max_count = max(max_count, count)  # update maximum
            else:
                count = 0            # streak breaks when a 0 appears

        return max_count

nums = [1, 1, 0, 1, 1, 1]
solution = Solution()
print(solution.findMaxConsecutiveOnes(nums)) 