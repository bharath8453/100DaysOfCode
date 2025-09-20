class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= (n - 1) 
            count += 1
        return count

sol = Solution()

n1 = 11  # binary: 1011
print("Input:", n1, "Output:", sol.hammingWeight(n1)) 

n2 = 128  # binary: 10000000
print("Input:", n2, "Output:", sol.hammingWeight(n2))

n3 = 2147483645
print("Input:", n3, "Output:", sol.hammingWeight(n3))