class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1) = points[0]
        (x2, y2) = points[1]
        (x3, y3) = points[2]

        if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x3, y3) == (x1, y1):
            return False

        return (y2-y1)*(x3-x2) != (y3-y2)*(x2-x1)