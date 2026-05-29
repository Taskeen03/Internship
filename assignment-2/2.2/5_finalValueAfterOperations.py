def finalValueAfterOperations(operations):
    return sum(1 if op[1] == '+' else -1 for op in operations)

operations_input = ["--X", "X++", "X++"]
result = finalValueAfterOperations(operations_input)
print(result)  