class Solution:
    def swap(self, unique, left, right):
        unique[left], unique[right] = unique[right], unique[left]

    def helper(self, unique, start, end, hMap, k):
        if end-start+1<=1:
            return
        
        pindex=random.randint(start, end)
        pivot_freq = hMap[unique[pindex]]        
        self.swap(unique, pindex, start)
        left=start
        for right in range(start+1, end+1):
            if hMap[unique[right]] < pivot_freq:
                left+=1
                self.swap(unique, left, right)
        self.swap(unique, start, left)
        if left == len(unique)-k:
            return
        elif left > len(unique)-k:
            self.helper(unique, start, left-1, hMap, k)
        else:
            self.helper(unique, left+1, end, hMap, k)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = Counter(nums)  
        unique = list(hMap.keys())

        self.helper(unique, 0, len(unique)-1, hMap, k)
        return unique[-k:]        
