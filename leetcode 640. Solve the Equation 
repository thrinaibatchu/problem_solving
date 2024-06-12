class Solution:
    def solveEquation(self, equation: str) -> str:
        def coeff(s):
            if s == 'x':
                return 1
            elif s == '-x':
                return -1
            else:
                return int(s[:-1])

        xterms = []
        cterms = []


        #We need this replacement to make the equation consistent for split in next step
        equation = equation.replace("-", "+-")

        #First Split for dividing lhs and rhs
        lhs, rhs = equation.split("=")

        #Second Split to get all the values into a list
        splitlhs = lhs.split("+")
        splitrhs = rhs.split("+")

        #Processing lhs
        for z in splitlhs:
            if z == "":
                continue
            # xterms in lhs
            elif z[-1] == "x":
                xterms.append(coeff(z))
            # cterms in lhs
            else:
                cterms.append(int(z) * -1)

        #Processing rhs
        for z in splitrhs:
            if z == "":
                continue
            # xterms in rhs
            elif z[-1] == "x":
                xterms.append(coeff(z) * -1)
            # cterms in rhs
            else:
                cterms.append(int(z))

        xcoeff = sum(xterms)
        ccoeff = sum(cterms)

        if xcoeff == 0 and ccoeff == 0:
            return "Infinite solutions"
        elif xcoeff == 0:
            return "No solution"
        else:
            return "x=" + str(int(ccoeff / xcoeff))