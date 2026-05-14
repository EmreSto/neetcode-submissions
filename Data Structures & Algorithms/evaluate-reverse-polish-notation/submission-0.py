class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        for data in tokens:
            if data not in ["+","-","*","/"]:
                mystack.append(int(data))
            elif data == "+":
                a = mystack.pop()
                b = mystack.pop()
                result = a + b
                mystack.append(result)
            elif data == "*":
                a = mystack.pop()
                b = mystack.pop()
                result = a * b
                mystack.append(result)
            elif data == "-":
                a = mystack.pop()
                b = mystack.pop()
                result = b - a
                mystack.append(result)
            elif data == "/":
                a = mystack.pop()
                b = mystack.pop()
                result =int(b / a)
                mystack.append(result)
        return mystack[0]


        