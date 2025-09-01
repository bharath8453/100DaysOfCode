class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:  # closing bracket
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:  # opening bracket
                stack.append(char)

        return not stack
        
solution = Solution()

print(solution.isValid("()")) 
print(solution.isValid("()[]{}")) 
print(solution.isValid("(]"))  
print(solution.isValid("([])")) 
print(solution.isValid("([)]"))