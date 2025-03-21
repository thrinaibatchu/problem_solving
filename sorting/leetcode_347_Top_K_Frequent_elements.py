class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap={}
        for i in range(len(nums)):
            if nums[i] in hMap:
                hMap[nums[i]]+=1
            else:
                hMap[nums[i]]=1
        
        ans=[]
        for i in range(k):
            highest_index=next(iter(hMap))
            for key, value in hMap.items():
                if value > hMap[highest_index]:
                    highest_index=key
            ans.append(highest_index)
            hMap.pop(highest_index)

        return ans
        