class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def generate_decimal_forms(s: str) -> List[str]:
            n = len(s)
            result = []
            # Base cases
            if n == 0:
                return []
            elif n == 1:
                return [s]
            # When length > 1:
            # If the string starts with '0'
            if s[0] == '0':
                # If it also ends with '0', no valid representation exists.
                if s[-1] == '0':
                    return []
                else:
                    # Only possible representation is "0.xxx"
                    return ['0.' + s[1:]]
            
            # If it ends with '0', then no decimal insertion is allowed.
            if s[-1] == '0':
                return [s]
            
            # Otherwise, the integer itself is valid.
            result.append(s)
            # And try inserting a decimal point at all possible positions.
            for i in range(1, n):
                result.append(s[:i] + '.' + s[i:])
            
            return result

        # Remove the outer parentheses.
        s1 = s[1:-1]
        result = []
        # Split s1 into two parts (left and right) at every possible index.
        for i in range(1, len(s1)):
            left = s1[:i]
            right = s1[i:]
            left_output = generate_decimal_forms(left)
            right_output = generate_decimal_forms(right)
            for l in left_output:
                for r in right_output:
                    result.append(f'({l}, {r})')
        
        return result
