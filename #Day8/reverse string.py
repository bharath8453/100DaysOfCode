class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap the characters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

sol = Solution()

s1 = ["h","e","l","l","o"]
sol.reverseString(s1)
print(s1)  # ["o","l","l","e","h"]

s2 = ["H","a","n","n","a","h"]
sol.reverseString(s2)
print(s2)  # ["h","a","n","n","a","H"]