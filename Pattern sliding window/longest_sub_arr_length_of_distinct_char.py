# Fruits into Baskets (medium)
# ===========================

# ex #1
# ======
fruit = ['A', 'B', 'C', 'A', 'C']
fruit_map = {}
win_start, max_length = 0, 0
sub_str_arr = ''
for win_end in range(len(fruit)):
    right_char = fruit[win_end]
    if right_char not in fruit_map:
        fruit_map[right_char] = 0
    fruit_map[right_char] += 1
    print(f"fruit_map: {fruit_map}")
    while len(fruit_map) > 2:  # sub_arr length > k
        print(f"length of fruit_map: {len(fruit_map)}")
        left_char = fruit[win_start]
        print(f"left char: {left_char}")
        fruit_map[left_char] -= 1
        if fruit_map[left_char] == 0:
            del fruit_map[left_char]
        print(f"new fruit_map: {fruit_map}")
        win_start += 1
    max_length = max(max_length, win_end - win_start + 1)
    sub_str_arr = fruit[win_start: win_end + 1]
print(f"max_length: {max_length}")
print(f"longest sub-arr: {sub_str_arr}")

# ex # 2
# =======
# longest sub str which not more k distinct char
# ===============================================

the_str = "araaci"
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
    if (win_end - win_start + 1) > max_length:
        sub_str_arr = the_str[win_start: win_end + 1]
    max_length = max(max_length, win_end - win_start + 1)
print(f"max_length: {max_length}")
print(f"longest sub-str: {sub_str_arr}")

