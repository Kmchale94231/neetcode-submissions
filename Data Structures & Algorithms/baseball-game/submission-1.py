class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 

        for i in operations:
            add = 0
            if i.lstrip("-").isdigit():
                stack.append(int(i))
                
            elif i == '+':
                add += sum(stack[-2:])
                stack.append(add)
                
            elif i == 'D':
                add = stack[-1] * 2
                stack.append(add)
            
            elif i == 'C':
                stack.pop()
                
        return sum(stack)
