def containsDuplicate(nums):
    return len(nums) != len(set(nums))

nums_input = [1, 2, 3, 1]
result = containsDuplicate(nums_input)
print(result)  