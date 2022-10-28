arr = [2, 1, 5, 1, 3, 2]
k = 3  # sub-array length
win_sum, win_start, max_sum = 0, 0, 0
max_sub_array = []  # highest value of sub-array
for win_end in range(len(arr)):
    win_sum += arr[win_end]
    print(f"iteration: {win_end}, win_sum: {win_sum}")
    if win_end >= k - 1:  # sub-array length check
        if win_sum > max_sum:  # current sub-array sum > previous sub-array sum then extract the sub-array
            max_sub_array = arr[win_start:win_end + 1]
            print(f"max sub array: {max_sub_array}")
        max_sum = max(max_sum, win_sum)
        print(f"max_sum: {max_sum}")
        # ******* most important part starts ***********
        win_sum -= arr[win_start]
        print(f"calculated win_sum: {win_sum}")
        win_start += 1
        print(f"win_start: {win_start}")
        # ******* most important part ends ***********

print(f"Max sum: {max_sum}")
print(f"Max sum of sub-array: {max_sub_array}")
