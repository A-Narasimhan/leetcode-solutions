class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board),len(board[0])
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,1),(1,-1)]

        for i in range(n):
            for j in range(m):
                l_n = 0
                for dx,dy in directions:
                    ni,nj = i+dx,j+dy

                    if 0 <= ni < n and 0 <= nj < m:
                        if board[ni][nj] in [1,2]:
                            l_n += 1
                if board[i][j] == 1:
                    if l_n < 2 or l_n > 3:
                        board[i][j] = 2
                else:
                    if l_n == 3:
                        board[i][j] = 3
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] =0
                elif board[i][j] == 3:
                    board[i][j] = 1