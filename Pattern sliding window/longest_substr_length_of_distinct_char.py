# longest sub str which not more k distinct char
# ===============================================

the_str = "ABCAC"
k = 2
hash_map = {}
win_start, max_length = 0, 0
sub_str_arr = ''
for win_end in range(len(the_str)):
    right_char = the_str[win_end]
    if right_char not in hash_map:
        hash_map[right_char] = 0
    hash_map[right_char] += 1
    print(f"hash_map: {hash_map}")
    while len(hash_map) > k:  # sub_str length > k
        print(f"length of hash_map: {len(hash_map)}")
        left_char = the_str[win_start]
        print(f"left char: {left_char}")
        hash_map[left_char] -= 1
        if hash_map[left_char] == 0:
            del hash_map[left_char]
        print(f"new hash_map: {hash_map}")
        win_start += 1
    max_length = max(max_length, win_end - win_start + 1)
    sub_str_arr = the_str[win_start: win_end+1]
print(f"max_length: {max_length}")
print(f"longest sub-str: {sub_str_arr}")
