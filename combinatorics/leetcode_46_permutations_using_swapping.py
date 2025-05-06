class Solution:
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

    def helper(self, nums, index, slate, result):
        #base case
        if index == len(nums):
            result.append(slate[:])
            return

        #internal case
        for i in range(index, len(nums)):
            slate.append(nums[i])
            self.swap(nums, index, i)
            self.helper(nums, index+1, slate, result)
            self.swap(nums, index, i)
            slate.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper(nums, 0, [], result)
        return result