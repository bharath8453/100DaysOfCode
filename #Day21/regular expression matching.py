class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        prev = [False] * (n + 1)  # previous row
        curr = [False] * (n + 1)  # current row

        prev[0] = True  # empty string matches empty pattern

        # handle empty string with patterns like a*, a*b*, etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]

        for i in range(1, m + 1):
            curr[0] = False  # non-empty string can't match empty pattern
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    curr[j] = prev[j - 1]
                elif p[j - 1] == '*':
                    curr[j] = curr[j - 2] or (
                        (p[j - 2] == '.' or p[j - 2] == s[i - 1]) and prev[j]
                    )
                else:
                    curr[j] = False
            prev, curr = curr, [False] * (n + 1)  # move to next row

        return prev[n]

# Test cases
sol = Solution()
print(sol.isMatch("aa", "a")) 
print(sol.isMatch("aa", "a*"))  
print(sol.isMatch("ab", ".*"))