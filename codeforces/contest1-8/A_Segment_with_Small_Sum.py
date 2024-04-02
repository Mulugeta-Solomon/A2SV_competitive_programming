n, target = map(int, input().split())
arr = list(map(int, input().split()))

left, curr_win_sum, max_len = 0, 0, 0

for right in range(len(arr)):
    curr_win_sum += arr[right]

    while left <= right and curr_win_sum > target:
        curr_win_sum -= arr[left]
        left += 1
        
    max_len = max(max_len, right - left + 1)

print(max_len)