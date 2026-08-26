def equilateral(sides):  
    return sides[0] == sides[1] == sides[2] if isValidTriangle(sides) else False


def isosceles(sides):
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2] if isValidTriangle(sides) else False


def scalene(sides):
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2] if isValidTriangle(sides) else False

def isValidTriangle(sides):
    if sides[0] == 0 or sides[1] == 0 or sides[2] == 0:
        return False
    return sides[0]+sides[1] >= sides[2] and sides[1]+sides[2] >= sides[0] and sides[0]+sides[2] >= sides[1]
