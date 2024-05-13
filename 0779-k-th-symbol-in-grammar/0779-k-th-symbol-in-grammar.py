class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1:
            return 0
        
        half_ele = 2 ** (n - 2)

        if k > half_ele:
            return 1 - self.kthGrammar(n, k - half_ele)
        
        else:
            return self.kthGrammar(n - 1, k)
        