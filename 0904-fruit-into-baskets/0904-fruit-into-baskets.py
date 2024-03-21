class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left, max_fruit, basket = 0, 0, {}

        for right in range(len(fruits)):
            
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) == 3:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                
                left += 1
            
            max_fruit = max(max_fruit, right - left + 1)
        
        return max_fruit


    