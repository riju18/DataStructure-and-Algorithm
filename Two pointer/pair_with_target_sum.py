nums = [3, 2, 4]
arr = nums.copy()
arr.sort()
target = 6
left, right = 0, len(arr) - 1
result = []
while left < right:
    print(f"left: {arr[left]}, right: {arr[right]}")
    if arr[left] + arr[right] == target:
        result = [arr[left], arr[right]]
        break
    elif arr[left] + arr[right] > target:
        right -= 1
    else:
        left += 1
else:
    result = [-1, -1]
result_ind = [nums.index(result[0]), nums.index(result[1])]
print(result_ind)
