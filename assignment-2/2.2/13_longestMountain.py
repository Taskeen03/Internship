def longestMountain(arr):
    n = len(arr)
    longest = 0

    for i in range(1, n - 1):
        if arr[i-1] < arr[i] > arr[i+1]:
            left = right = i
            
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
            while right < n - 1 and arr[right] > arr[right+1]:
                right += 1
                
            longest = max(longest, right - left + 1)
            
    return longest

arr_input = [2, 1, 1, 5, 6, 2, 3, 1]
result = longestMountain(arr_input)
print(result)  