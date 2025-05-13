class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def helper(index, slate):
            #Backtracking case
            if slate and (not isPalindrome(slate[-1])):
                    return

            #Base case
            if index == len(s):
                result.append(slate[:])
                return
            
            for curr in range(index, len(s)):
                curr_str = s[index:curr+1]
                slate.append(curr_str)
                helper(curr+1, slate)
                slate.pop()
        
        helper(0, [])
        return result  