class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_count, close_count):
            # Base case: valid combination formed
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Add '(' if we can still open more
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()

            # Add ')' if we can close an open parenthesis
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result

solution = Solution()

print(solution.generateParenthesis(3))
print(solution.generateParenthesis(1))
