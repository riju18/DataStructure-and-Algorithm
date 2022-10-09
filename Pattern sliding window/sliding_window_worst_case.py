# ***************************
# Time complexity: big O(N*K)
# ***************************
arr = [2, 1, 5, 1, 3, 2]
k = 3
max_sum = 0
max_sub_array = []
for i in range(len(arr)-k):
    win_sum = 0
    for j in range(i, i+k):
        win_sum += arr[j]
    if win_sum > max_sum:
        max_sub_array = arr[i: i+k]
    max_sum = max(max_sum, win_sum)
print(max_sum)
print(max_sub_array)
