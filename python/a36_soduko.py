class Solution:
	def isValid(self, board):
		
		s = set()

		# SWEEP
		for i in range(len(board)):
			for j in range(len(board[0])):
				cur = board[i][j]
				if cur != ".":
					if (i,cur) in s or (cur,j) in s or (i//3, j//3, cur) in s:
						return False
					s.add((i,cur))
					s.add((cur,j))
					s.add((i//3, j//3,cur))
		return True

# DRIVER CODE
if __name__ == "__main__":
	board = [["5","3",".",".","7",".",".",".","."]
	,["6",".",".","1","9","5",".",".","."]
	,[".","9","8",".",".",".",".","6","."]
	,["8",".",".",".","6",".",".",".","3"]
	,["4",".",".","8",".","3",".",".","1"]
	,["7",".",".",".","2",".",".",".","6"]
	,[".","6",".",".",".",".","2","8","."]
	,[".",".",".","4","1","9",".",".","5"]
	,[".",".",".",".","8",".",".","7","9"]]
	ob1 = Solution()
	print(ob1.isValid(board))