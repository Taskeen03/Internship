def sortStack(stack):
    aux_stack = []
    
    while stack:
        tmp = stack.pop()

        while aux_stack and aux_stack[-1] > tmp:
            stack.append(aux_stack.pop())
            
        aux_stack.append(tmp)       
    return aux_stack

stack_input = [34, 3, 31, 98, 92, 23]
result = sortStack(stack_input)
print(result)  