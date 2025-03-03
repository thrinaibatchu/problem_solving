class Solution:
    #Using Bubble Sort
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(0, len(nums)-i):
                if j+1<len(nums) and nums[j] > nums[j+1]:
                    nums[j], nums[j+1]=nums[j+1], nums[j]

        return nums