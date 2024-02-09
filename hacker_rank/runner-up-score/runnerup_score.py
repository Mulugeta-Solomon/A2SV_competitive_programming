if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    runner_up = sorted(set(arr))[-2]
    print(runner_up)