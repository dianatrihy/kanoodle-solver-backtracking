import piece
import board
import backtracking
import time
import bruteforce

# inisiasi
board = board.Board(5, 11)
# noodles = ["A", "L", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
noodles = ["L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
pieces = []

for noodle in noodles:
    pieces.append(piece.Piece(noodle))

# input random piece
n = 0
while n < 2:
    print("what kind of piece do you want to put?")
    print("A B C D E F G H I J K L")
    print()

    char = str(input("input here: "))
    print()
    while noodles.count(char) == 0:
        print("wrong input, make sure input between A-L")
        char = str(input("input again here: "))
        print()

    idx = noodles.index(char)
    orientations = pieces[idx]
    print("what kind of orientation that you want to put?")
    i = 1
    for orientation in orientations.shapes:
        print(i)
        i += 1
        for row in orientation:
            for r in row:
                if r == 1:
                    print(char + " " , end="")
                else:
                    print("0 ", end="")
            print()
        print()

    num = int(input("input here: "))
    print()
    while num <= 0 or num > len(orientations.shapes):
        print("wrong input, make sure input between 1-" + str(len(orientations.shapes)))
        num = int(input("input again here: "))
        print()

    print("where do you want to put the piece?")
    print("row: 0-4, col: 0-10")
    print()
    row = int(input("row: "))
    col = int(input("col: "))

    while row < 0 or row >= 5 or col < 0 or not(board.can_place(orientations.shapes[num-1], row, col)):
        print("wrong input, make sure row: 0-4, col: 0-10 and possible to put in board with that orientation")
        row = int(input("row: "))
        col = int(input("col: "))
        print()

    board.place_piece(orientations.shapes[num-1], row, col, char)
    board.print_board()
    pieces.remove(orientations)
    n += 1

start_time = time.time()

if board.is_feasible():
    # backtracking.solve_backtracking(board, pieces, 0)
    bruteforce.solve_brute_force(board, pieces, 0)
else:
    print("not possible to solve")

end_time = time.time()

# Hitung waktu eksekusi
execution_time = end_time - start_time
print(f"execution time: {execution_time} detik")