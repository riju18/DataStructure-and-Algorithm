# Fruits into Baskets (medium)
# ===========================

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
    sub_str_arr = fruit[win_start: win_end+1]
print(f"max_length: {max_length}")
print(f"longest sub-arr: {sub_str_arr}")