n, m = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

def merge_arr(arr_1, n, arr_2, m):
    pointer_1, pointer_2 = 0, 0

    result = []

    while pointer_1 < n and pointer_2 < m:

        if arr_1[pointer_1] > arr_2[pointer_2]:
            result.append(arr_2[pointer_2])
            pointer_2 += 1
        else:
            result.append(arr_1[pointer_1])
            pointer_1 += 1
    
    result.extend(arr_1[pointer_1:])
    result.extend(arr_2[pointer_2:])

    return result

print(*merge_arr(arr_1, n, arr_2, m))



