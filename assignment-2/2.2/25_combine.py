def combine(n, k):
    res = []
    
    def backtrack(start, path):
        if len(path) == k:
            res.append(list(path))
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()            
    backtrack(1, [])
    return res

n_input, k_input = 4, 2
result = combine(n_input, k_input)
print(result)  