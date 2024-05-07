class Solution:
    # s, count = '0', 1

    # def NthBinaryString(self, n: int):
    #     if Solution.count == n:
    #         return 
        
    #     temp = list(Solution.s)
    #     for i in range(len(temp)): # invert the string
    #         if temp[i] == '0':
    #             temp[i] = '1'
    #         else:
    #             temp[i] = '0'

    #     temp = ''.join(temp[::-1])

    #     Solution.s = Solution.s + '1' + temp
    #     Solution.count += 1

    #     self.NthBinaryString(n)


    def findKthBit(self, n: int, k: int) -> str:
        if n == 1 or k == 1:
            return '0'
        
        if k-1 > ((2**n - 1) // 2):
            print(k)
            k = 2 * ((2**n - 1) // 2) - k + 2 
            print(k)
            return str(1 - int(self.findKthBit(n - 1, k)))
        elif k - 1 == ((2**n - 1) // 2):
            return '1'
        else:
            return self.findKthBit(n - 1, k)
        


 
        # self.NthBinaryString(n)
        # print(Solution.s)

        # return Solution.s[k-1]
        