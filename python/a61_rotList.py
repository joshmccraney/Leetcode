class Solution:
    def rotateRight(self, head, k):
        n = len(head)
        new = [None] * n

        if k > n:
            k = k%n - 1

        for i in range(n):
            if i + k < n:
                new[k+i] = head[i]
            else:
                new[i+k-n] = head[i]
        return new

if __name__ == "__main__":
    ob1 = Solution()
    head = [1,2,3,4,5]
    k = 2
    print(ob1.rotateRight(head, k))