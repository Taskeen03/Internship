def letterCasePermutation(s):
    res = []
    
    def backtrack(sub, i):
        if len(sub) == len(s):
            res.append(sub)
            return
        
        if s[i].isalpha():
            backtrack(sub + s[i].lower(), i + 1)
            backtrack(sub + s[i].upper(), i + 1)
        else:
            backtrack(sub + s[i], i + 1)          
    backtrack("", 0)
    return res

s_input = "a1b2"
result = letterCasePermutation(s_input)
print(result)  