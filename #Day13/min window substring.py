from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        # Count characters in t
        need = Counter(t)
        required = len(need)  # Number of unique chars needed

        # Left and right pointers
        left = 0
        right = 0

        # Formed keeps track of how many unique chars in current window match t's frequency
        formed = 0
        window_counts = {}

        # (window_length, left_index, right_index)
        ans = (float("inf"), 0, 0)

        while right < len(s):
            # Add current character to window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If current char count matches needed char count, increment formed
            if char in need and window_counts[char] == need[char]:
                formed += 1

            # Try to shrink the window from left if all required chars are in it
            while left <= right and formed == required:
                char = s[left]

                # Update answer if this window is smaller
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Remove char from window
                window_counts[char] -= 1
                if char in need and window_counts[char] < need[char]:
                    formed -= 1

                left += 1  # Shrink from left

            right += 1  # Expand to the right

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

s = "a"
t = "a"
solution = Solution()
print(solution.minWindow(s, t)) 