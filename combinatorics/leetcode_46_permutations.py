class Solution:
    def helper(self, slate, nums, result):
        if len(nums) == 0:
            result.append(slate[:])
        else:
            for i in range(len(nums)):
                slate.append(nums[i])
                self.helper(slate, nums[:i]+nums[i+1:], result)
                slate.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.helper([], nums, result)
        return result
        