def kth_permutation(n, k):
    permutation = []
    unused = list(range(1, n + 1))
    
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = i * fact[i - 1]
        
    k -= 1 
    
    while n > 0:
        part_length = fact[n] // n  
        i = k // part_length
        
        permutation.append(unused[i])
        unused.pop(i)  
        
        k %= part_length
        n -= 1
        
    return ''.join(map(str, permutation))

n = 3
k = 3
print(f"The {k}rd permutation of {n} numbers is:", kth_permutation(n, k))