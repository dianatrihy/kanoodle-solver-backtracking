import board
import piece
import multiprocessing
import time

def solve_backtracking(board, pieces, piece_index=0):
    if piece_index >= len(pieces):
        return board.board

    piece = pieces[piece_index]
    for orientation in piece.shapes:
        for row in range(board.rows):
            for col in range(board.cols):
                if board.can_place(orientation, row, col):
                    board.place_piece(orientation, row, col, piece.cat)
                    if board.is_feasible():
                        result = solve_backtracking(board, pieces, piece_index + 1)
                        if result:
                            return result
                    board.remove_piece(orientation, row, col)
    return None

def solve_backtracking_parallel(board, pieces, piece_index=0, max_workers=4):
    if piece_index >= len(pieces):
        return board.board

    piece = pieces[piece_index]
    tasks = []
    for orientation in piece.shapes:
        for row in range(board.rows):
            for col in range(board.cols):
                if board.can_place(orientation, row, col):
                    board_copy = board.copy()
                    board_copy.place_piece(orientation, row, col, piece.cat)
                    if board_copy.is_feasible():
                        tasks.append((board_copy, pieces, piece_index + 1))

    with multiprocessing.Pool(max_workers) as pool:
        results = pool.starmap(solve_backtracking_task, tasks)

    for result in results:
        if result:
            return result
    return None

def solve_backtracking_task(board, pieces, piece_index):
    return solve_backtracking(board, pieces, piece_index)

if __name__ == "__main__":
    board1 = board.Board(5, 11)
    noodles = ["L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    pieces = [piece.Piece(noodle) for noodle in noodles]

    # Apiece = piece.Piece("A")
    # board1.place_piece(Apiece.shapes[0], 2, 0, "A")
    # board1.print_board()

    start_time = time.time()

    result = solve_backtracking(board1, pieces)
    if result:
        print("Solution found:")
        for row in result:
            print(row)
    else:
        print("No solution found.")

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")

    board2 = board.Board(5, 11)
    noodles = ["L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    pieces = [piece.Piece(noodle) for noodle in noodles]

    # Apiece = piece.Piece("A")
    # board2.place_piece(Apiece.shapes[0], 2, 0, "A")
    # board2.print_board()

    start_time = time.time()

    result = solve_backtracking_parallel(board2, pieces)
    if result:
        print("Solution found:")
        for row in result:
            print(row)
    else:
        print("No solution found.")

    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
