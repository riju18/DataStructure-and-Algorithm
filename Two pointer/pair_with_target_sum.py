arr = [1, 2, 3, 4, 6]
target = 6
left, right = 0, len(arr) - 1
result = []
while left < right:
    print(f"left: {arr[left]}, right: {arr[right]}")
    if arr[left] + arr[right] == target:
        result = [left, right]
        break
    elif arr[left] + arr[right] > target:
        right -= 1
    else:
        left += 1
print(result)
