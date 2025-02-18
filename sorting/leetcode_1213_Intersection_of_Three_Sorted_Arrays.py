class Solution:
    def compare_two(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        temp=[]
        while (i<len(arr1) and j<len(arr2)):
            if arr1[i] == arr2[j]:
                temp.append(arr1[i])
                i+=1
                j+=1
            elif(arr1[i]<arr2[j]):
                i+=1
            else:
                j+=1

        return temp

    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        first_compare=self.compare_two(arr1, arr2)
        final_compare=self.compare_two(first_compare, arr3) 
        return final_compare

