import numpy as np

# CALCULUS IMPLIES p = 2/pi s.t. l = line space = 1 ==> pi = 2/p
class Buffon:
    def approx(self, n):

        # COUNT INTERSECTIONS
        hit = 0

        for i in range(n):

            # GENERATE RANDOM CENTER Y COORDINATE
            y = np.random.rand()

            # GENERATE RANDOM ANGLE MADE WITH NEEDLE AND HORIZONTAL
            angle = np.radians(np.random.rand())*90

            # TOP POINT OF NEEDLE
            yU = y + 0.5*(np.sin(angle))
            # BOTTOM POINT OF NEEDLE
            yL = y - 0.5*(np.sin(angle))

            # IF UPPER OR LOWER INTERSECTION COUNT IT
            if (yU >= 1) or (yL <= 0):
                hit += 1

        return 2/(hit/n)

if __name__ == "__main__":
    ob1 = Buffon()
    n = 10000
    print(ob1.approx(n))
    