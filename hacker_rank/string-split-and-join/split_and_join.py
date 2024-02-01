def split_and_join(line):
    # write your code here
    split_str = line.split(" ")
    join_str = "-".join(split_str)
    
    return join_str
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)