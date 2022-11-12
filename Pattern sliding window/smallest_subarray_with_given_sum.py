# Dynamic length
# ===============
import math

arr = [2, 1, 5, 2, 3, 2]
s = 7
win_sum, win_start, min_length = 0, 0, math.inf
sub_arr = []
for win_end in range(len(arr)):
    win_sum += arr[win_end]
    print(f"New win_sum: {win_sum}")
    while win_sum >= s:  # it'll check continuously the min len
        min_length = min(min_length, win_end - win_start + 1)
        print(f"Updated min_length: {min_length}")
        sub_arr.append(arr[win_start:win_end+1])  # store the elements >= s
        win_sum -= arr[win_start]
        print(f"Updated win sum: {win_sum}")
        win_start += 1
if min_length == math.inf:
    print("Got not min length of sum")
else:
    print(f"Final min_length: {min_length}")
    print(f"Final sub arr: {min(sub_arr, key=len)}")  # smallest sub arr
    sub_arr = []  # free the memory
