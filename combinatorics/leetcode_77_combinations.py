class Solution:
    def helper(self, slate, start, n, k, result):
        #Base case
        if len(slate) == k:
            result.append(slate[:])
            return

        #Recursion case
        for i in range(start, n+1):
            slate.append(i)
            self.helper(slate, i+1, n, k, result)
            slate.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.helper([], 1, n, k, result)
        return result
        