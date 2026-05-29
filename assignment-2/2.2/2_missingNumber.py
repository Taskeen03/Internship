def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

nums_input = [3, 0, 1]
result = missingNumber(nums_input)
print(result)  