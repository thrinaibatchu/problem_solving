class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        def helper(index, slate):
            if index == len(num):
                expr = ''.join(slate)
                if eval(expr) == target:
                    result.append(expr)
                return

            for i in range(index, len(num)):
                curr_str = num[index : i + 1]

                if i > index and num[index] == '0':
                    break

                # If slate is empty, simply add the current number, without any operator.
                if not slate:
                    slate.append(curr_str)
                    helper(i + 1, slate)
                    slate.pop()
                else:
                    # Otherwise, insert one of the operators before appending the number.
                    for op in ['+', '-', '*']:
                        slate.append(op)
                        slate.append(curr_str)
                        helper(i + 1, slate)
                        slate.pop()  # remove curr_str
                        slate.pop()  # remove operator

        helper(0, [])
        return result