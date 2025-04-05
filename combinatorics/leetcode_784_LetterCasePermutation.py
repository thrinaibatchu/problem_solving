class Solution:
    def is_number_str(self, s):
        """Checks if a string can be converted to a float or an integer."""
        try:
            int(s)
            return True
        except ValueError:
            return False

    def helper(self, slate, i, nums, result):
        #Base case
        if i == len(nums):
            result.append("".join(slate))
            return

        #Recursion case
        #number
        if self.is_number_str(nums[i]):
            slate.append(nums[i])
            self.helper(slate, i+1, nums, result)
            slate.pop()

        else:
            #upper case
            slate.append(nums[i].upper())
            self.helper(slate, i+1, nums, result)
            slate.pop()
            
            #lower case
            slate.append(nums[i].lower())
            self.helper(slate, i+1, nums, result)
            slate.pop()

    def letterCasePermutation(self, s: str) -> List[str]:
        result=[]
        self.helper([], 0, list(s), result)
        return result
        