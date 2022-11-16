import numpy as np
import statistics
import time

# EXPECTED NUMBER OF TOSSES FOR COIN WITH T WEIGHTED p FOR SEQUENCE HHTH
# t0 = time.time()
class coin:
    # def approx(self, n, p):
    #     lst = []
    #     for _ in range(n):
    #         toss = 0
    #         count = 0
    #         while count < 4:

    #             # THE TOSS
    #             x = np.random.rand()
    #             toss += 1

    #             # LET x < p INDICATE TAILS
    #             # LET x > p INDICATE HEADS

    #             ## AFTER HHT, WE SEEK H
    #             if count == 3:
    #                 if x > p:       # IF HEADS, APPEND lst WITH NUM OF TOSSES
    #                     lst.append(toss)
    #                     count = 4   # MAKE COUNT 4 TO BREAK WHILE LOOP
    #                 else:
    #                     count = 0   # SEQUENCE IS HHTT WHICH IS T, SO COUNT RESTARTS

    #             ## AFTER HH, WE SEEK T
    #             if count == 2:
    #                 if x > p:   
    #                     count = 2   # IF HEADS, WE HAVE HH
    #                 else:
    #                     count = 3   # IF TAILS, WE HAVE HHT

    #             # FIRST TWO HH
    #             if count < 2:
    #                 if x < p: # IF TAILS, RESTART COUNT
    #                     count = 0
    #                 else:   # IF HEADS, WE HAVE H OR HH
    #                     count += 1

    #     return statistics.mean(lst)

        def approx(self, n, p):
            lst = []
            target = "111"
            for _ in range(n):
                count = 0
                str = ""
                while True:
                    # THE TOSS
                    x = np.random.rand()
                    count += 1

                    if x > p:
                        char = "1"
                    else:
                        char = "0"
                    str += char

                    if target in str:
                        lst.append(count)
                        break
            return statistics.mean(lst)               
            
if __name__ == "__main__":
    n = 100000
    p = 0.5
    print(coin().approx(n, p))

# t1 = time.time()
# print(t1-t0)