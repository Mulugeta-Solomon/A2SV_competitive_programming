n, m = map(int, input().split())

cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

tower_ptr = 0   
min_radius = 0

for city_ptr in range(n):
    
    while tower_ptr + 1 < m and abs(cities[city_ptr] - towers[tower_ptr] >= abs(cities[city_ptr] - towers[tower_ptr+1])):
        tower_ptr += 1
    
    min_radius = max(min_radius, abs(cities[city_ptr] - towers[tower_ptr]))

print(min_radius)  