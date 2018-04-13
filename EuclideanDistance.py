import math

def dis(p1, p2, m):
    s = 0
    for i in range(m) :
        d = (p2[i]-p1[i])
        d = math.pow(d, 2)
        s = s+d
    s = math.sqrt(s)
    return s

def EuclideanDistance(origin, points):
    m = len(points[1])
    distances = []
    for point in points:
        distances.append(dis(origin, point, m))
    return distances