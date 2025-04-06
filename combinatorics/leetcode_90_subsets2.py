class Solution:
    def helper(self, slate, index, nums):
        self.result.append(slate[:])

        #Recursion case with implicit base case using for loop
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            slate.append(nums[i])
            self.helper(slate, i+1, nums)
            slate.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result=[]
        self.helper([], 0, nums)
        return self.result