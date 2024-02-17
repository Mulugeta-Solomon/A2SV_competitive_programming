
n = int(input())
input_ = []

for _ in range (n):
    name =  input()

    input_.append(name)


def file_management_sys(names):
    look_up = {}
    result = []
    for name in names:
        if name not in look_up:
            look_up[name] = 1
            result.append('OK')
        else:
            look_up[name] += 1
            if look_up[name] > 1:
                result.append(name + str(look_up[name] - 1))

    return result

output_ = file_management_sys(input_)
for result in output_:
    print(result)