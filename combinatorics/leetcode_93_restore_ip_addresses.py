class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def helper(index, slate):
            if len(slate) > 4:
                return  

            if index == len(s) and len(slate) == 4:
                result.append('.'.join(slate))
                return

            for curr in range(index, len(s)):
                curr_str = s[index:curr+1]

                if (curr > index and s[index] == '0') or int(curr_str) > 255:
                    break
                slate.append(curr_str)
                helper(curr+1, slate)
                slate.pop()
        
        helper(0, [])
        return result