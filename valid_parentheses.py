class Solution(object):

    def is_valid(self, string: str) -> bool:
        rules = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in string:
            if char in rules.keys():
                stack.append(char)
            elif len(stack) > 0 and rules.get(stack[-1]) == char:
                stack.pop()
            else:
                return False

        return len(stack) == 0


sol = Solution()

print(sol.is_valid("{[]}"))
