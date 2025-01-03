class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        
        for i in range(len(nums)):
            find_value = target - nums[i]
            if find_value in hmap:
                return [i, hmap[find_value]]
            else:
                hmap[nums[i]]=i