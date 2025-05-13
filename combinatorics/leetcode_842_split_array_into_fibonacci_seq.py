class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        result=[]
        def helper(index, slate):   
            if len(slate) >=3 and slate[-1] != slate[-2] + slate[-3]:
                return 

            if index == len(num) and len(slate) >= 3:
                result.append(slate[:])
                return
            
            for curr in range(index, len(num)):
                curr_str = num[index:curr+1]

                if (len(curr_str) > 1 and curr_str[0] == '0') or (int(curr_str) > 2**31 - 1):
                    break
                
                slate.append(int(curr_str))
                helper(curr+1, slate)
                slate.pop()

        helper(0, [])
        return result[0] if result else []  