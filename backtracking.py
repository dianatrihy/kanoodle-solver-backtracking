import board
import piece

def solve_backtracking(board, pieces, piece_index=0):
    board.print_board()
    count_attempts = 0  
    
    if piece_index >= len(pieces):
        print("result: ")
        board.print_board()
        return True, count_attempts

    print(len(pieces))
    piece = pieces[piece_index]
    for orientation in piece.shapes:
        for row in range(board.rows):
            for col in range(board.cols):
                if board.can_place(orientation, row, col):
                    board.place_piece(orientation, row, col, piece.cat)
                    count_attempts += 1  
                    if board.is_feasible():
                        solved, count = solve_backtracking(board, pieces, piece_index + 1)
                        count_attempts += count  
                        if solved:
                            return True, count_attempts
                    else:
                        print("not feasible")
                    board.remove_piece(orientation, row, col)
    return False, count_attempts



# result, attempts = solve_backtracking(board, pieces)
# print("Total attempts:", attempts)
