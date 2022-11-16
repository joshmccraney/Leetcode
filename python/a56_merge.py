class Solution:
    def merge(self, intervals):
        intervals.sort()
        sol = [intervals[0]]
        newListCt = 0

        for i in range(1,len(intervals)):
            if sol[newListCt][1] >= intervals[i][0] and sol[newListCt][1] <= intervals[i][1]:
                sol[newListCt][1] = intervals[i][1]
            elif sol[newListCt][1] >= intervals[i][0] and sol[newListCt][1] > intervals[i][1]:
                pass
            else:
                sol.append(intervals[i])
                newListCt += 1
        return sol
        
if __name__ == "__main__":
    ob1 = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(ob1.merge(intervals))