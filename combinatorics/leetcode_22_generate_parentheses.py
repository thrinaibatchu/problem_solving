class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(numLeft, numRight, slate):
            #Backtracking case with constraint
            if numRight < numLeft:
                return
                 
            #Base case
            if numLeft == 0 and numRight == 0:
                result.append(''.join(slate))
                return

            #recursion case
            #Left Parantheses
            if numLeft > 0:
                slate.append("(")
                helper(numLeft-1, numRight, slate)
                slate.pop()

            #Right Parantheses
            if numRight > 0:
                slate.append(")")
                helper(numLeft, numRight-1, slate)
                slate.pop()
        
        result = []
        helper(n, n, [])
        return result