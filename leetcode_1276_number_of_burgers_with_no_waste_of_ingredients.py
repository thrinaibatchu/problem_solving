class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        s = 2 * cheeseSlices - (tomatoSlices/2)
        j = (tomatoSlices/2) - cheeseSlices

        if j == int(j) and s == int(s) and s >= 0 and j >= 0:
            return [int(j), int(s)]
        else:
            return []