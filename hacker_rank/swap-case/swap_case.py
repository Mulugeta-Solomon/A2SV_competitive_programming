def swap_case(s):
    swap_case = ''
    for letter in s:
        if letter in [' ', '.', '"', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            swap_case += letter
        else:
            if letter.isupper():
                swap_case += letter.lower()
            else:
                swap_case += letter.upper()
            
            
    return swap_case

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)