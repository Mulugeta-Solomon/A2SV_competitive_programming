#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        if len(A) != len(B):
            return False
        
        count_A = {}
        count_B = {}
        
        for num in A:
            if num not in count_A.keys():
                count_A[num] = 1
            else:
                count_A[num] += 1
        
        for num in B:
            if num not in count_B.keys():
                count_B[num] = 1
            else:
                count_B[num] += 1
        
        return count_A == count_B
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends