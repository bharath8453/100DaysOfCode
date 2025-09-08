from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # Deque will store indices of elements (not values directly)
        # Maintain it in decreasing order of values
        dq = deque()
        result = []

        for i in range(len(nums)):
            # 1. Remove indices that are out of this window
            if dq and dq[0] == i - k:
                dq.popleft()

            # 2. Maintain decreasing order in deque
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Add max (front of deque) to result only if we have full window
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) 
print(sol.maxSlidingWindow([1], 1))   
