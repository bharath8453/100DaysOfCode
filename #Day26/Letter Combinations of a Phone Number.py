class Solution(object):
    def letterCombinations(self, digits):

        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            # Base case: combination complete
            if index == len(digits):
                result.append("".join(path))
                return

            # Explore letters for current digit
            for char in phone_map[digits[index]]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return result

solution = Solution()

print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
print(solution.letterCombinations("2"))