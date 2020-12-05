# Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

def print_board(board):
    for row in board:
        print(row, sep='\n')


N = 8
board = [[0 for _ in range(N)] for _ in range(N)]
print_board(board)
moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, 1)]


def fill_board(board, moves, coords, counter):
    if counter == N*N:
        return True


fill_board(board, moves, 0)
