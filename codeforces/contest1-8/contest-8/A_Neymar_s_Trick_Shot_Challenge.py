n, x = map(int, input().split())

distance = list(map(int, input().split()))

bounce, count = 0, 1

for i in range(len(distance)):

    bounce += distance[i]
    if bounce > x:
        break
    count += 1

print(count)