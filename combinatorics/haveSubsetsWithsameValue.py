class Solution:
    def helper(self, slate, i, summ, nums):
        #Base case
        if i == len(nums):
            if summ in self.dict:
                self.result = True
            else:
                self.dict[summ]=slate[:]
            return

        #Recursive case
        #exclude
        self.helper(slate, i+1, summ, nums)
        
        #Include
        slate.append(nums[i])
        self.helper(slate, i+1, summ+nums[i], nums)
        slate.pop()

    def subsetswithsamevalue(self, nums: List[int]) -> bool:
        self.dict={}
        self.result=False
        self.helper([], 0, 0, nums)

        return True if self.result else False
        