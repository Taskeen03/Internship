from collections import Counter

def are_anagrams_counter(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

def are_anagrams_sorted(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

result1 = are_anagrams_counter("listen", "silent")
result2 = are_anagrams_sorted("hello", "world")

print(result1) 
print(result2)