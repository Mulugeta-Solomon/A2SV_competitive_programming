input_str =  str(input())

max_count, curr_count = 0, 0

for char in input_str:
    if char == 'O':
        curr_count += 1
        max_count = max(max_count, curr_count)
    else:
        curr_count = 0


print(max_count)