the_arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3
repeated_one, win_start, max_length = 0, 0, 0
sub_arr = []
for win_end in range(len(the_arr)):
    right_char = the_arr[win_end]
    print(f"i: {win_end}, right_char: {right_char}")
    if right_char == 1:
        repeated_one += 1
    print(f"repeated_one: {repeated_one}")
    if (win_end-win_start+1-repeated_one) > k:
        if the_arr[win_start] == 1:
            repeated_one -= 1
        win_start += 1
    if (win_end-win_start+1) > max_length:
        sub_arr = the_arr[win_start:win_end+1]
    max_length = max(max_length, win_end-win_start+1)
    print(f"max_length: {max_length}")
print(f"Final max_length: {max_length}")
print(f"Final sub array: {sub_arr}")