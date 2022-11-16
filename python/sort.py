import numpy as np
class Solution:
    def merge(self, m, n):
        arr = np.concatenate((m, n), axis = None)
        for i in range(1, len(arr)):
 
            cur = arr[i]
    
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and cur < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = cur
            
        return(arr)
                



if __name__ == "__main__":
    ob1 = Solution()
    m = np.random.randint(0, 10, 15)
    n = np.random.randint(0, 10, 15)
    print(ob1.merge(m, n))