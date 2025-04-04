class Solution:
    def helper(self, nums, target, start, end):
        #Base case
        if start > end:
            return -1

        #Recursive case
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.helper(nums, target, start, mid-1)
        else:
            return self.helper(nums, target, mid+1, end)

    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, len(nums)-1)