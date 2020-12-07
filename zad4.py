# Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

def print_board(board):
    for row in board:
        print(row, sep='\n')


N = 7
board = [[0 for _ in range(N)] for _ in range(N)]
total_moves = 0


def fill_board(board, move, coords, counter):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    global total_moves
    if counter == N*N + 1:
        return True

    b, a = coords
    y, x = move
    if b+y >= 0 and a+x >= 0 and b+y < N and a+x < N and board[b+y][a+x] == 0:
        board[b+y][a+x] = counter
        coords = (b+y, a+x)
        counter += 1
        total_moves += 1
        if total_moves % 1000000 == 0:
            print(total_moves)
    else:
        return False

    # if counter == N*N:
    #     return True

    for m in moves:
        if (fill_board(board, m, coords, counter)):
            return True
    counter -= 1
    board[b+y][a+x] = 0
    return False


print(fill_board(board, (0, 0), (0, 0), 1))
print('total:', total_moves)
print_board(board)
