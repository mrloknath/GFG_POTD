class Solution:
    def doIntersect(self, p1, q1, p2, q2):
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else 2

        def onSegment(p, q, r):
            if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
                return True
            return False

        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return 'true'

        if o1 == 0 and onSegment(p1, p2, q1):
            return 'true'

        if o2 == 0 and onSegment(p1, q2, q1):
            return 'true'

        if o3 == 0 and onSegment(p2, p1, q2):
            return 'true'

        if o4 == 0 and onSegment(p2, q1, q2):
            return 'true'

        return 'false'
