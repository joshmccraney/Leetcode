import numpy as np

# AREA OF CIRCLE WITH RADIUS 1 IS pi AND AREA OF CIRCUMSCRIBING SQUARE IS 4
# THE RATIO OF THE TWO IS pi / 4 = points-in-circle / total-points

class circ:
    def approx(self, n):
        circCount = 0
        for _ in range(n):
            x = np.random.rand()
            y = np.random.rand()

            if x**2 + y**2 <= 1:
                circCount += 1

        return 4 * circCount / n
if __name__ == "__main__":
    n = 10000
    print(circ().approx(n))

    