class Solution:
    def findMaxAverage(self, nums, k):
        # Step 1: Calculate sum of the first 'k' elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: Slide the window across the array
        for i in range(k, len(nums)):
            # Subtract element going out, add element coming in
            window_sum += nums[i] - nums[i - k]
            # Update the maximum sum if current window's sum is greater
            max_sum = max(max_sum, window_sum)

        # Step 3: Return maximum average as float
        return max_sum / float(k)  # Ensures floating-point division

# Example usage
nums = [1,12,-5,-6,50,3]
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))