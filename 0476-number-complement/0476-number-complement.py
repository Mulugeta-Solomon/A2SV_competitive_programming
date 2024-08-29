class Solution:
    def findComplement(self, num: int) -> int:
        def binary(num):
            bin_ = str()
            
            while num != 0:
                remainder = num % 2 
                bin_ += str(remainder)
                num //= 2
            
            return bin_ [::-1]

        def complement(bin_):
            comp = str()
            for val in bin_:
                if int(val) == 1:
                    comp += str(0)
                else:
                    comp += str(1)       
            return comp

        def integer(comp):
            pow = 0
            result = 0

            for i in range(len(comp) - 1, -1, -1):
                result += (int(comp[i]) * (2 ** pow))
                pow += 1
            
            return result
        
        print(binary(num))

        return integer(complement(binary(num)))
        