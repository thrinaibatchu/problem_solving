class Solution:
    def helper(self, slate, nums):
        #base case
        if len(nums) == 0:
            self.result.append(slate[:])
            print(slate)
            return
        
        #Recursive case
        for i in range(len(nums)):
            #Taking care of the duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            slate.append(nums[i])
            self.helper(slate, nums[:i]+nums[i+1:])
            slate.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result=[]
        self.helper([], nums)
        return self.result