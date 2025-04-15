# time complexity: O(n)
# space  complexity: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        # the stack to keep track of opening brackets
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False
            elif s[i] == "}":
                if stack and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
            elif s[i] == "]":
                if stack and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
            else:
                return False

        if not stack:
            return True
        else:
            return False


input = Solution()
print(input.isValid("}"))