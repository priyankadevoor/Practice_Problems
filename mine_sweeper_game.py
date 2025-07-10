import random

def mine_sweeper(mines, rows, cols):

    board = [ [0] * cols for _ in range(rows)]
    count = 0
    
    while count < mines:
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        if board[row][col] != '*':
            board[row][col] = '*'
            count += 1
    
    
    for r in range(rows):
        for c in range(cols):
            dirs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r+1, c+1), (r+1, c-1), (r-1, c+1)]
            if board[r][c] == '*':
                for nr, nc in dirs:
                    if 0<=nr<rows and 0<=nc<cols and board[nr][nc] != '*':
                        board[nr][nc] += 1

    for r in range(rows):
        print(board[r])

mine_sweeper(5, 5, 5)