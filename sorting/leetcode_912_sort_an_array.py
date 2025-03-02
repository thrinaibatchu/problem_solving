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
        pivot = nums[pindex]  
        self.swap(nums, pindex, start)
        orange=start+1
        blue=start+1
        green=end

        while (blue <= green):
            if nums[blue] < pivot:
                self.swap(nums, blue, orange)
                orange+=1
                blue+=1
            elif nums[blue] > pivot:
                self.swap(nums, blue, green)
                green-=1
            else:
                blue+=1

        self.helper(nums, start, orange-1)
        self.helper(nums, green+1, end)
