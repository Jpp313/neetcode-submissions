class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for val in tokens:
            if val == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif val == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b) - int(a))
            elif val == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif val == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a) // int(b))
            else:
                stack.append(val)
        return stack