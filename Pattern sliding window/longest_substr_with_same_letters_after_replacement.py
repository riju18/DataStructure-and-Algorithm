# Longest Substring with Same Letters after Replacement
# =====================================================

the_string = "aabccbb"
k = 2
max_repeated_char, win_start, max_length = 0, 0, 0
final_longest_sub_str = ''
hash_map = {}
for win_end in range(len(the_string)):
    right_char = the_string[win_end]
    print(f"i: {win_end}, right_char: {right_char}")
    if right_char not in hash_map:
        hash_map[right_char] = 0
    hash_map[right_char] += 1
    print(f"hash_map: {hash_map}")
    max_repeated_char = max(max_repeated_char, hash_map[right_char])
    print(f"max_repeated_char: {max_repeated_char}")
    if (win_end - win_start + 1 - max_repeated_char) > k:  # to check 2 chars are repeated or not
        win_start += 1  # shrink the window
        print(f"updated win_start: {win_start}")
    max_length = max(max_length, win_end-win_start+1)
    final_longest_sub_str = the_string[win_start:win_end+1]
print(f"max_str_length: {max_length}")
print(f"longest_sub_str: {final_longest_sub_str}")