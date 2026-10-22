class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                popped_num = my_stack.pop()
                popped_num1 = my_stack.pop()
                summing = int(popped_num+popped_num1)
                my_stack.append(summing)
            elif tokens[i] == "-":
                popped_num = my_stack.pop()
                popped_num1 = my_stack.pop()
                substract = int(popped_num1-popped_num)
                my_stack.append(substract)
            elif tokens[i] == "*":
                popped_num = my_stack.pop()
                popped_num1 = my_stack.pop()
                multi = int(popped_num*popped_num1)
                my_stack.append(multi)
            elif tokens[i] == "/":
                popped_num = my_stack.pop()
                popped_num1 = my_stack.pop()
                div = int(popped_num1/popped_num)
                my_stack.append(div)
            else:
                my_stack.append(int(tokens[i]))
        return int(my_stack.pop())
                
        