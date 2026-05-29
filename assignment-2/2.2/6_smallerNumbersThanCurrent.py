def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    return [sorted_nums.index(num) for num in nums]

nums_input = [8, 1, 2, 2, 3]
result = smallerNumbersThanCurrent(nums_input)
print(result)  