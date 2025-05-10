class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()

        def helper(row, slate):
            #base case
            if row == n:
                result.append(slate[:])
                return

            #recursive case
            for col in range(n):
                if col in cols or (row + col) in pos_diagonals or (row-col) in neg_diagonals:
                    continue
                
                #Choose
                cols.add(col)
                pos_diagonals.add(row+col)
                neg_diagonals.add(row-col)
                slate.append(col)
                
                #Explore
                helper(row+1, slate)

                #Unchoose
                cols.remove(col)
                pos_diagonals.remove(row+col)
                neg_diagonals.remove(row-col)
                slate.pop()

        helper(0, [])   
        final_result = []
        for solution in result:
            board=[]
            for row in range(n):
                line = ['.'] * n
                line[solution[row]] = 'Q'
                board.append(''.join(line))
            final_result.append(board)        
        
        return final_result