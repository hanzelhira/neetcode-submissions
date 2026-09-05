class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            cur = s[i]
            if cur == "(" or cur == "{" or cur == "[":
                stack.append(cur)
            elif len(stack) == 0:
                return False
            elif cur == ")":
                top = stack[-1]
                if top != "(":
                    return False
                else:
                    stack.pop()
                    continue
            elif cur == "]":
                top = stack[-1]
                if top != "[":
                    return False
                else:
                    stack.pop()
                    continue
            elif cur == "}":
                top = stack[-1]
                if top != "{":
                    return False
                else:
                    stack.pop()
                    continue
        return len(stack) == 0