import bf

def solve_brute_force(board, pieces):
    def list_all_placements(board, piece):
        placements = []
        for shape in piece.shapes:
            for row in range(board.rows):
                for col in range(board.cols):
                    if board.can_place(shape, row, col):
                        placements.append((shape, row, col, piece.cat))
        return placements
    
    count_attempts = 0 
    list_all = []
    for piece in pieces:
        placements = list_all_placements(board, piece)
        list_all.append(placements)
        print(piece.cat)

    if len(pieces) == 3:
        state, count_attempts = bf.bf3(board, list_all, count_attempts)
    elif len(pieces) == 4:
        state, count_attempts = bf.bf4(board, list_all, count_attempts)
    elif len(pieces) == 5:
        state, count_attempts = bf.bf5(board, list_all, count_attempts)

    return state, count_attempts

