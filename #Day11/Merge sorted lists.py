class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Do not return anything, modify nums1 in-place instead.
        i = m - 1  # pointer for nums1
        j = n - 1  # pointer for nums2
        k = m + n - 1  # pointer for the end of nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements, place them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol = Solution()  # Create an instance
sol.merge(nums1, m, nums2, n)
print(nums1)