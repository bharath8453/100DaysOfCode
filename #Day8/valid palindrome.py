class Solution:
    def isPalindrome(self, s):
        # Step 1: Convert to lowercase
        s = s.lower()

        # Step 2: Keep only letters and digits
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char

        # Step 3: Check if cleaned string is same as its reverse
        return cleaned == cleaned[::-1]

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(sol.isPalindrome("race a car"))  # False