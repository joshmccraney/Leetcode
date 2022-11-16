import numpy as np

def dice(n):
    p1 = 0
    for _ in range(n):
        while True:
            roll = np.random.rand()
            if roll > 5/6:
                p1 += 1
                break
            else:
                roll = np.random.rand()
                if roll < 2/6:
                    break

    return p1/n

if __name__ == "__main__":
    n = 1000000
    print(dice(n))

