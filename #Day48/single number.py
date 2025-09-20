class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  
        return result



sol = Solution()

nums1 = [2, 2, 1]
print("Input:", nums1, "Output:", sol.singleNumber(nums1)) 

nums2 = [4, 1, 2, 1, 2]
print("Input:", nums2, "Output:", sol.singleNumber(nums2))  

nums3 = [1]
print("Input:", nums3, "Output:", sol.singleNumber(nums3)) 