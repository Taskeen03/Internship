def containsNearbyDuplicate(nums, k):
    seen = set()
    for i, num in enumerate(nums):
        if i > k:
            seen.remove(nums[i - k - 1])
        if num in seen:
            return True
        seen.add(num)
    return False

nums_input = [1, 2, 3, 1]
k_input = 3
result = containsNearbyDuplicate(nums_input, k_input)
print(result)  