class Solution:
    def helper(self, slate, i, nums):
        if i == len(nums):
            self.result.append(slate[:])
            return

        #Recursion case
        #Exclude
        self.helper(slate, i+1, nums)

        #Include
        slate.append(nums[i])
        self.helper(slate, i+1, nums)
        slate.pop()
        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result=[]
        self.helper([], 0, nums)
        return self.result