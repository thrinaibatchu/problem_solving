class Solution:
    def helper(self, nums, start, end):
        if start>=end:
            return

        mid=int(start + (end-start)/2)
        self.helper(nums, start, mid)
        self.helper(nums, mid+1, end)

        i=start
        j=mid+1
        aux=[]

        while i<=mid and j<=end:
            if nums[i] < nums[j]:
                aux.append(nums[i])
                i+=1
            else:
                aux.append(nums[j])
                j+=1
        
        while i<=mid:
            aux.append(nums[i])
            i+=1
        
        while j<=end:
            aux.append(nums[j])
            j+=1

        nums[start:end+1]=aux



    def sortArray(self, nums: List[int]) -> List[int]:
        self.helper(nums, 0, len(nums)-1)
        return nums

        