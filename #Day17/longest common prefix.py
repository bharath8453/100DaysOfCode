class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]

        for word in strs[1:]:
            while word.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return "" 

        return prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))