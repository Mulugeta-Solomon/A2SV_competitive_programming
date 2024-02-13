n, m = map(int, input().split())

ip_command, ip_name = {}, {}
for _ in range(n + m):
    name, ip = input().split()

    if ip[-1] == ';':
        ip_command[name] = ip
    else:
        ip_name[ip] = name

for command, ip in ip_command.items():
    print(f"{command} {ip} #{ip_name[ip[:-1]]}" )


# n, m = map(int, input().split())

# ip_to_name = {}
# for _ in range(n):
#     name, ip = input().split()
#     ip_to_name[ip] = name


# for _ in range(m):
#     command, ip = input().split()
#     name = ip_to_name[ip[:-1]]
#     print(f"{command} {ip[:-1]}; #{name}")
