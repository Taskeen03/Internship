def minSubArrayLen(target, nums):
    min_len = float('inf')
    current_sum = 0
    left = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1           
    return min_len if min_len != float('inf') else 0

target_input = 7
nums_input = [2, 3, 1, 2, 4, 3]
result = minSubArrayLen(target_input, nums_input)
print(result)  