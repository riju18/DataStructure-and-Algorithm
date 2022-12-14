arr = [1, 0, 2, 1, 0]
low, high = 0, len(arr) - 1
i = 0
while i <= high:
    print(f"iteration: {i}")
    if arr[i] == 0:
        print(f"element: {arr[i]}")
        print(f"prev arr: {arr}")
        arr[i], arr[low] = arr[low], arr[i]
        i += 1
        low += 1
        print(f"new arr: {arr}")
    elif arr[i] == 1:
        print(f"element: {arr[i]}")
        i += 1
    else:
        print(f"element: {arr[i]}")
        print(f"prev arr: {arr}")
        arr[i], arr[high] = arr[high], arr[i]
        high -= 1
        print(f"new arr: {arr}")

print(f"final sorted arr: {arr}")

# **************************
# Time complexity: O(N)
# Space complexity: O(1)
# ***************************
