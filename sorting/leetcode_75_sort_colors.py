class Solution:
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        curr=0
        right=len(nums)-1

        while curr <=right:
            if nums[curr] == 1:
                curr+=1
            elif nums[curr] == 0:
                self.swap(nums, left, curr)
                curr+=1
                left+=1
            elif nums[curr] == 2:
                self.swap(nums, curr, right)
                right-=1
