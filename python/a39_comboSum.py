class Solution:
    def combinationSum(self, candidates, target):
        output = []
        length = len(candidates)
            
        def traverse(comb, start_index):
            if sum(comb) == target:
                output.append(comb[:])
                return
                
            if sum(comb) > target:
                return
                
            for index in range(start_index, length):
                comb.append(candidates[index])
                traverse(comb, index)
                comb.pop()
        
        traverse([], 0)
        return output

if __name__ == "__main__":
    ob1 = Solution()
    candidates = [2,7]
    target = 7
    print(ob1.combinationSum(candidates, target))