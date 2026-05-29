def find_start(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target and (mid == 0 or arr[mid-1] < target):
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_end(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
       
        if arr[mid] == target and (mid == len(arr) - 1 or arr[mid+1] > target):
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

  
def first_and_last(arr, target):
   
    if not arr:
        return [-1, -1]
        
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]

nums = [5, 7, 7, 8, 8, 10]
print(first_and_last(nums, 8))  
print(first_and_last(nums, 6))  