class Solution:
     def nQueen(self, n):
        # code here
        ans = []
        def queen(board, r):
            if r == n:
                ans.append(board[:])
                return
            for c in range(1, n+1):
                board.append(c)
                for p in range(r):
                    if board[p] == c or abs(board[p]-c) == abs(r-p):
                        break
                else:
                    queen(board, r+1)
                board.pop()
        
        queen([], 0)
        return ans
