# sliding window with dynamic length
# ==================================

the_str = "abccde"
char_map = {}
win_start, max_length = 0, 0
sub_arr = []
for win_end in range(len(the_str)):
    print(f"iteration: {win_end}")
    right_char = the_str[win_end]
    print(f"right char: {right_char}")
    if right_char in char_map:
        win_start = max(win_start, char_map[right_char] + 1)
        print(f"win_start: {win_start}")
    char_map[right_char] = win_end
    print(f"char_map: {char_map}")
    max_length = max(max_length, win_end - win_start + 1)
    print(f"max_length: {max_length}")
    sub_str = the_str[win_start:max(win_start, char_map[right_char] + 1)]  # find out the distinct char of sub_array
    sub_arr.append(sub_str)
print(f"Final max_length: {max_length}")
distinct_sub_arr = list(filter(lambda i: len(i) == max_length, sub_arr))
print(distinct_sub_arr)
