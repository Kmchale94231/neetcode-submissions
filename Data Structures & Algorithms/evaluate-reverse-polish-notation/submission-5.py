class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for i in tokens:
            operand1 = 0
            operand2 = 0
            result = 0

            if i == '+':
                operand1 = num_stack.pop()
                operand2 = num_stack.pop()
                result = operand1 + operand2
                num_stack.append(result)
            
            elif i == '-':
                operand1 = num_stack.pop()
                operand2 = num_stack.pop()
                result += (operand2 - operand1)
                num_stack.append(result)

            
            elif i == '*':
                operand1 = num_stack.pop()
                operand2 = num_stack.pop()
                result += (operand1 * operand2)
                num_stack.append(result)
            
            elif i == '/':
                operand1 = num_stack.pop()
                operand2 = num_stack.pop()
                result += int(operand2 / operand1)
                num_stack.append(result)
            
            else:
                num_stack.append(int(i))
        
        return num_stack[-1]
        
        

