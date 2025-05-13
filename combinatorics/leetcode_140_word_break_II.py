class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        result=[]

        def helper(index, slate):
            if slate and slate[-1] not in word_set:
                return

            if index == len(s):
                result.append(' '.join(slate))
                return

            for curr in range(index, len(s)):
                curr_str = s[index:curr+1]

                slate.append(curr_str)
                helper(curr+1, slate)
                slate.pop()
        
        helper(0, [])
        return result
        