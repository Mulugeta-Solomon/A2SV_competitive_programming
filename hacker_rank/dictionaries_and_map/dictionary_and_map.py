# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

phonebook = {}

for _ in range(n):
    name, phone = input().split()
    phonebook.update({name: phone})
    

for _ in range(n):
    name = str(input())
    number = phonebook.get(name)
    if not number:
        print("Not found")
    else:
        print("{}={}".format(name, number))