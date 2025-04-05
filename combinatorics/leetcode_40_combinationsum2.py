class Solution:
    def helper(self, slate, candidates, target, index, result):
        #Base case
        if target == 0:
            result.append(sorted(slate))
            return
        elif target < 0:
            return

        #Recursive case
        else:
            for i in range(index, len(candidates)):
                #Optimized case when we have duplicate candidates
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                slate.append(candidates[i])
                self.helper(slate, candidates, target-candidates[i], i+1, result)
                slate.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        #Need this to optimize for duplicate candidates
        candidates.sort()
        self.helper([], candidates, target, 0, result)
        return result