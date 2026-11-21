class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
        So we use a stack, append until we see an operation, once we do see it 
        we just loop over for the stack and haev a total which we modify continuously.


        '''

        stack = []
        result = 0

        for token in tokens:

            if token in '+-*/':
                b = stack.pop()
                a = stack.pop()
                

                if token == '+':
                    stack.append(a + b)
                    
                elif token == '-':
                    stack.append(a - b)
                    
                elif token == '*':
                    stack.append(a * b)
                   
                elif token == '/':
                    stack.append(int(a / b))
                   

            else:
                stack.append(int(token))


        return stack[-1]


        