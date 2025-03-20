class Solution:
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]

    def helper(self, nums, start, end, index):
        #base case
        if end-start+1<=1:
            return

        #recursive case
        pindex=random.randint(start, end)
        pivot=nums[pindex]
        self.swap(nums, start, pindex)
        left=start
        curr=start
        right=end
        
        while curr<=right:
            if nums[curr] == pivot:
                curr+=1
            elif nums[curr] > pivot:
                self.swap(nums, curr, right)
                right-=1
            else:
                self.swap(nums, curr, left)
                left+=1
                curr+=1
                
        #using quick select approach where we traverse into either one of the partitions instead of both as in quick sort algo.
        if index < left:
            self.helper(nums, start, left-1, index)
        elif index > left:
            self.helper(nums, right+1, end, index)
        else:
            return

    def findKthLargest(self, nums: List[int], k: int) -> int:
        index=len(nums)-k
        self.helper(nums, 0, len(nums)-1, index)
        return nums[index]