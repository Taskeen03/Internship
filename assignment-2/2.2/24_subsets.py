def subsets(nums):
    res = []
    
    def backtrack(start, path):
        res.append(list(path))
        for i in range(start, len(nums)):
            path.append(nums[i])      
            backtrack(i + 1, path)    
            path.pop()                         
    backtrack(0, [])
    return res

nums_input = [1, 2, 3]
result = subsets(nums_input)
print(result)  