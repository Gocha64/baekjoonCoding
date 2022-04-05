n, m = map(int, input().split())


board = []
for i in range(n):
    board.append(input())

def get_8Board(board, i, j):
    board8 = []
    for k in range(i, i+8):
        board8.append(board[k][j:j+8])
    return board8


def Count_Painting(board):
    #왼쪽 위칸이 흰색
    white = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i + j) % 2 == 0:
                if board[i][j] == 'B':
                    white += 1
            else:
                if board[i][j] == 'W':
                    white += 1

    #왼쪽 위칸이 검은색
    black = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i + j) % 2 == 0:
                if board[i][j] == 'W':
                    black += 1
            else:
                if board[i][j] == 'B':
                    black += 1

    return min(white, black)


min_painting = 64

for i in range(n-7):
    for j in range(m-7):

        count_painting = Count_Painting(get_8Board(board, i, j))
        min_painting = min(count_painting, min_painting)

print(min_painting)