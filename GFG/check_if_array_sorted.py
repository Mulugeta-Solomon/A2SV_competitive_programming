#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        
        right = 2
        left = 0
        
        while right <= len(arr) - 1:
            
            if arr[left] > arr[right-1] or arr[right-1] > arr[right] or arr[left] > arr[right]:
                return False
            
            right += 1
            left += 1
        
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends