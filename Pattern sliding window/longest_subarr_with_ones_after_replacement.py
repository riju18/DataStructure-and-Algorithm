the_arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3
repeated_one, win_start, max_length = 0, 0, 0
for win_end in range(len(the_arr)):
    right_char = the_arr[win_end]
    if right_char == 1:
        repeated_one += 1
    if (win_end-win_start+1-repeated_one) > k:
        if the_arr[win_start] == 1:
            repeated_one -= 1
        win_start += 1
    max_length = max(max_length, win_end-win_start+1)
print(max_length)