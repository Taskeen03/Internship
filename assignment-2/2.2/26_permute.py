def permute(nums):
    res = []
    
    def backtrack(path):
        if len(path) == len(nums):
            res.append(list(path))
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()               
    backtrack([])
    return res

nums_input = [1, 2, 3]
result = permute(nums_input)
print(result)  