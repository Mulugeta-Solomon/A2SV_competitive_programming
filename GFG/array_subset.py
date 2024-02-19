#User function Template for python3

def isSubset( a1, a2, n, m):
    
    look_up_a1 = {}
    look_up_a2 = {}
    
    for num in a1:
        if num in look_up_a1:
            look_up_a1[num] += 1
        else:
            look_up_a1[num] = 1
    for num in a2:
        if num in look_up_a2:
            look_up_a2[num] += 1
        else:
            look_up_a2[num] = 1
    
    if all(key in look_up_a1 and look_up_a2[key] <= look_up_a1[key] for key in look_up_a2):
        return "Yes"
    
    return "No"
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends