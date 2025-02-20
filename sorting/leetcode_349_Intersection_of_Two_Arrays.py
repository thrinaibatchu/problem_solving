class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_set = set()
        result_set = set()

        for val in nums1:
            my_set.add(val)

        for val in nums2:
            if val in my_set:
                result_set.add(val)

        return list(result_set)
