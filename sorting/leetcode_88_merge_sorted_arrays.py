class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k=len(nums1)-1 #Full length of the first list
        j=len(nums2)-1 #Full length of the second list
        i=k-j-1 #Length of the first list with actual values

        #Reverse merging the list using two pointer approach
        while i >= 0 and j >= 0: 
            #Picking the greater number and inserting it into the end. Also, if same number we need to choose from nums1
            if nums1[i] >= nums2[j]: 
                nums1[k] = nums1[i]
                i-=1
                k-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1

        #Gathering the leftovers from the nums2, we don't need to Gather from nums1 because we are already working on nums1
        while j>=0:
            nums1[k]=nums2[j]
            k-=1
            j-=1

