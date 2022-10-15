# longest sub str which not more k distinct char
# ===============================================

the_str = "cbbebi"
k = 3
hash_map = {}
win_start = 0
max_length = 0
sub_str_arr = []
for win_end in range(len(the_str)):
    right_char = the_str[win_end]
    if right_char not in hash_map:
        hash_map[right_char] = 0
    hash_map[right_char] += 1
    while len(hash_map) > k:  # sub_str > k
        sub_str_arr.append(the_str[win_start: win_end])
        left_char = the_str[win_start]
        hash_map[left_char] -= 1
        if hash_map[left_char] == 0:
            del hash_map[left_char]
        win_start += 1
    max_length = max(max_length, win_end - win_start + 1)
print(f"max_length: {max_length}")
result = list(filter(lambda i: len(i) == max_length, sub_str_arr))
print(f"longest sub-str: {result}")
