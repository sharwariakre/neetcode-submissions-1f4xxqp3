class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                opright = stack.pop()
                opleft = stack.pop()
                if i == "+":
                    stack.append(opleft + opright)
                elif i == "-":
                    stack.append(opleft - opright)
                elif i == "*":
                    stack.append(opleft * opright)
                elif i == "/":
                    stack.append(int(opleft / opright))
        return stack[-1]
                

