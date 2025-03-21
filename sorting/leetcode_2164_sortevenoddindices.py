class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]

        for i in range(0, len(nums), 2):
            even.append(nums[i])

        for i in range(1, len(nums), 2):
            odd.append(nums[i])

        even.sort()
        odd.sort(reverse=True)
        i, j, curr = 0, 0, 0

        while curr < len(nums):
            if curr % 2 == 0:
                nums[curr]=even[i]
                i+=1
                curr+=1
            else:
                nums[curr]=odd[j]
                j+=1
                curr+=1
        return nums

