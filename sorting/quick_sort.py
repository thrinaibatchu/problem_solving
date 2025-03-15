class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.helper(nums, 0, len(nums)-1)
        return nums

    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]
    
    def helper(self, nums: List[int], start, end):
        
        if end-start+1<=1:
            return
        
        pindex=random.randint(start, end)
        self.swap(nums, pindex, start)

        orange=start
        for green in range (start+1, end+1):
            if nums[green] <= nums[start]:
                orange+=1
                self.swap(nums, green, orange)
        
        self.swap(nums, start, orange)
        self.helper(nums, start, orange-1)
        self.helper(nums, orange+1, end)