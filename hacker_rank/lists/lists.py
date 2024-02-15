if __name__ == '__main__':
    N = int(input())

    arr = []

    for i in range(N):
        c = input().split()
        if c[0] == 'print':
            print(arr)
        if c[0] == 'sort':
            arr.sort()
        if c[0] == 'reverse':
            arr.reverse()
        if c[0] == 'append':
            arr.append(int(c[1]))
        if c[0] == 'insert':
            element, pos = int(c[2]), int(c[1])
            arr.insert(pos, element)
        if c[0] == 'pop':
            arr.pop()
        if c[0] == 'remove':
            if int(c[1]) in arr:
                arr.remove(int(c[1]))