import sys

# Function to return the sum of a 
# triplet which is closest to x 
def solution(arr, x) : 

    # Sort the array 
    arr.sort()
    
    # To store the closest sum
    closestSum = sys.maxsize; 

    # Fix the smallest number among 
    # the three integers 
    for i in range(len(arr)-2): 

        # Two pointers initially pointing at 
        # the last and the element 
        # next to the fixed element 
        L = i + 1; R = len(arr) - 1;

        # While there could be more pairs to check 
        while (L < R) :

            # Calculate the sum of the current triplet 
            sum = arr[i] + arr[L] + arr[R]; 

            # If the sum is more closer than 
            # the current closest sum 
            if (abs(x - sum) < abs(x - closestSum)) :
                closestSum = sum; 

            # If sum is greater then x then decrement 
            # the second pointer to get a smaller sum 
            if (sum > x) :
                R -= 1; 

            # Else increment the first pointer 
            # to get a larger sum 
            else :
                L += 1; 

    # Return the closest sum found 
    return closestSum; 

# Driver code 
if __name__ == "__main__" : 

    arr = [ -1, 2, 1, -4 ]; 
    x = 1; 
    print(solution(arr, x))