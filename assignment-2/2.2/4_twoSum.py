def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in seen:
            return [seen[remaining], i]
        seen[num] = i

nums_input = [2, 7, 11, 15]
target_input = 9
result = twoSum(nums_input, target_input)
print(result) 
