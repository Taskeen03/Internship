def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums_input = [4, 1, 2, 1, 2]
result = singleNumber(nums_input)
print(result)  