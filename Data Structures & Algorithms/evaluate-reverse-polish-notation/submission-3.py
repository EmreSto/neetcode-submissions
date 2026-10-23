class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                pop1 = my_stack.pop()
                pop2 = my_stack.pop()
                summination = pop1 + pop2
                my_stack.append(summination)
            elif tokens[i] == "-":
                pop1 = my_stack.pop()
                pop2 = my_stack.pop()
                substract = pop2 - pop1
                my_stack.append(substract)
            elif tokens[i] == "/":
                pop1 = my_stack.pop()
                pop2 = my_stack.pop()
                div = int(pop2 / pop1)
                my_stack.append(div)
            elif tokens[i] == "*":
                pop1 = my_stack.pop()
                pop2 = my_stack.pop()
                multi = pop1 * pop2
                my_stack.append(multi)
            else:
                my_stack.append(int(tokens[i]))
        return int(my_stack.pop())
        