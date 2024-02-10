n, k  = map(int, input().split())

def wrong_substraction (n, k):
    for i in range(k):
        if n%10 == 0:
            n //= 10
        else:
            n -= 1
    return n


print(wrong_substraction(n, k))