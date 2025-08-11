class Solution:
    def moveZeroes(self, nums):
        # Pointer for position to place the next non-zero
        pos = 0  

        # Step 1: Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Step 2: Fill the remaining positions with zeros
        for i in range(pos, len(nums)):
            nums[i] = 0

sol = Solution()

nums1 = [0, 1, 0, 3, 12]
sol.moveZeroes(nums1)
print(nums1)  # [1, 3, 12, 0, 0]

nums2 = [0]
sol.moveZeroes(nums2)
print(nums2)  # [0]