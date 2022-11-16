class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(goal - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0: return True
        else: return False
        
if __name__ == "__main__":
    nums = [2,0,2,1,4,1,1]
    ob1 = Solution()
    print(ob1.canJump(nums))