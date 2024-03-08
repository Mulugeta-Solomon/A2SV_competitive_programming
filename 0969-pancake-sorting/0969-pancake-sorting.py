class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        result = []

        while len(arr) > 1:
            max_element = max(arr) 
            index = arr.index(max_element)

            if index == 0:
                result.append(len(arr))
                arr = arr[1::][::-1]
                 

            elif index != len(arr) - 1:
                arr = arr[:index+1][::-1] + arr[index+1:]
                result.append(index+1)
                result.append(len(arr))
                arr = arr[1::][::-1]

            else:
                arr = arr[:-1]
        
        return result

