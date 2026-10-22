class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                my_stack.append(ch)
            if ch == ")" or ch == "]" or ch == "}":
                if len(my_stack) == 0:
                    return False
                elif my_stack[-1] == "[" and ch == "]":
                    my_stack.pop()
                elif my_stack[-1] == "(" and ch == ")":
                    my_stack.pop()
                elif my_stack[-1] == "{" and ch == "}":
                    my_stack.pop()
                else:
                    return False
        return not my_stack