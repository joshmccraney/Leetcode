class Solution:
    def inset(self, intervals, newInterval):
        intervals.append(newInterval)
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
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    ob1 = Solution()
    print(ob1.inset(intervals, newInterval))