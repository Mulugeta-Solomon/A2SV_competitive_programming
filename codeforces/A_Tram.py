n_stops = int(input())

n_entring = []
n_exiting = [] 
for i in range(n_stops):
    exiting, entering = map(int, input().split())
    
    n_entring.append(entering)
    n_exiting.append(exiting)

result = []
sum = 0
for i in range(n_stops):
    sum -= n_exiting[i]
    sum += n_entring[i]
    result.append(sum)

print(max(result))



