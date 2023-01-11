arr = [2, 3, 3, 3, 6, 9, 9]
next_non_dup = 1
dup_ind = []
left = 1
while left < len(arr):
    if arr[left] != arr[next_non_dup - 1]:  # check consecutive 2 elements are different
        arr[next_non_dup] = arr[left]  # no change
        next_non_dup += 1
    else:
        dup_ind.append(left)
    left += 1
print(f"total unique elements: {next_non_dup}")
print(f"duplicate index: {dup_ind}")
# **************************
# Time complexity: O(N)
# Space complexity: O(1)
# ***************************
