class Solution:
    def trap(self, height):
        V = 0
        for i in range(1,len(height)-1):
            L = max( height[:i] )
            R = max( height[i+1:] )
            vol = min(L,R) - height[i]
            if vol > 0:
                V += vol
        return V   

if __name__ == "__main__":
    ob1 = Solution()
    height = [4,2,0,3,2,5]
    print(ob1.trap(height))