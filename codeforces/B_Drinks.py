total_drink = int(input())

volume_fraction_orange = list(input().split())

volume_fraction_orange = [int(value) for value in volume_fraction_orange] 


total_orange_percent = float(sum(volume_fraction_orange) / total_drink)

print("{:.12f}".format(total_orange_percent))

