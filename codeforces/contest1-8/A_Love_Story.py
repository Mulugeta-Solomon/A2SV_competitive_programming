test_case = int(input())

str_= 'codeforces'

for _ in range(test_case):
    ptr, diff = 0, 0
    s = str(input())


    while ptr < len(str_):
        if s[ptr] != str_[ptr]:
            diff += 1
        
        ptr += 1
    
    print(diff)