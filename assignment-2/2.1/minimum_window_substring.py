from collections import Counter

def min_window(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
        
    freqt = Counter(t)
    freqs = Counter()
    
    start, end = 0, n + 1 
    satisfied = 0
    left = 0
    
    for right in range(n):

        char_right = s[right]
        freqs[char_right] += 1
        if char_right in freqt and freqs[char_right] == freqt[char_right]:
            satisfied += 1
            
        while satisfied == len(freqt):
            
            if right - left + 1 < end - start:
                start, end = left, right + 1
                
            char_left = s[left]
            
            if char_left in freqt and freqs[char_left] == freqt[char_left]:
                satisfied -= 1
                
            freqs[char_left] -= 1
            left += 1
            
    return s[start:end] if end - start <= n else ""

S = "ADOBECODEBANC"
T = "ABC"
print("Minimum Window Substring:", min_window(S, T))