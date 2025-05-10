class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(index, slate):
            #Backtracking case
            if len(slate) == k:
                result.append(slate[:])
                return

            #Base case
            if index == n+1:
                return

            #Recursive case
            #Exclude
            helper(index+1, slate)

            #Include
            slate.append(index)
            helper(index+1, slate)
            slate.pop()

        helper(1, [])
        return result