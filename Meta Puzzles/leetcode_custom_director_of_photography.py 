# Problem: Director of Photography (Custom / Meta-style)
# Link: N/A (commonly used in Meta screening assessments)
# Concepts: Sliding Window, Pattern Matching, Frequency Counting
# Approach: For each 'A' in the string, count 'P' and 'B' within bounded left/right windows.
#           Compute valid artistic photo triplets using the formula:
#           (P_left * B_right) + (B_left * P_right)
# Time Complexity: O(N * (Y - X + 1)) in worst-case where every char is 'A'
# Space Complexity: O(1) additional space

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    def helper(pos):
        l_end = pos - X
        l_start = max(0, pos - Y)
        r_start = pos + X
        r_end = min(pos + Y, len(C) - 1)

        pl_count = bl_count = pr_count = br_count = 0

        for i in range(l_start, l_end + 1):
            if C[i] == 'P':
                pl_count += 1
            elif C[i] == 'B':
                bl_count += 1

        for i in range(r_start, r_end + 1):
            if C[i] == 'P':
                pr_count += 1
            elif C[i] == 'B':
                br_count += 1

        return (pl_count * br_count) + (bl_count * pr_count)

    result = 0
    for i in range(N):
        if C[i] == 'A':
            result += helper(i)
    return result