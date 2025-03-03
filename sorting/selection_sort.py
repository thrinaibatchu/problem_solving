class Solution:
    #Using Selection Sort Algorithm T(n) = O(n^2)
    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            minElement=nums[i]
            minElementIndex=i

            for j in range(i+1, len(nums)):
                if nums[j] < minElement:
                    minElement=nums[j]
                    minElementIndex=j

            self.swap(nums, i, minElementIndex)

        return nums