class Solution:
    def helper(self, slate, candidates, target, index, result):
        if target == 0:
            result.append(sorted(slate))
            return
        elif target < 0:
            return
        else:
            for i in range(index, len(candidates)):
                # if i > index and candidates[i-1] == candidates[i]:
                    # continue
                slate.append(candidates[i])
                self.helper(slate, candidates, target-candidates[i], i, result)
                slate.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        # candidates.sort()
        self.helper([], candidates, target, 0, result)
        return result