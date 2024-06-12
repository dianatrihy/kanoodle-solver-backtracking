import board
import piece
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

    # placement0 = list_all[0][0]
    # shape0 = placement0[0]
    # row0 = placement0[1]
    # col0 = placement0[2]
    # placement1 = list_all[1][0]
    # shape1 = placement1[0]
    # row1 = placement1[1]
    # col1 = placement1[2]
    # placement2 = list_all[2][0]
    # shape2 = placement2[0]
    # row2 = placement2[1]
    # col2 = placement2[2]
    # placement3 = list_all[3][0]
    # shape3 = placement3[0]
    # row3 = placement3[1]
    # col3 = placement3[2]

    # flag0 = False
    # flag1 = False
    # flag2 = False
    # flag3 = False

    # for placement0 in list_all[0]:
    #     if flag0:
    #         board.remove_piece(shape0, row0, col0)
    #         flag0 = False
    #     shape0 = placement0[0]
    #     row0 = placement0[1]
    #     col0 = placement0[2]
    #     cat0 = placement0[3]
    #     if board.can_place(shape0, row0, col0):
    #         board.place_piece(shape0, row0, col0, cat0)
    #         flag0 = True
    #         count_attempts += 1
    #         if not(board.is_feasible()):
    #             board.remove_piece(shape0, row0, col0)
    #             continue

    #     for placement1 in list_all[1]:
    #         if flag1:
    #             board.remove_piece(shape1, row1, col1)
    #             flag1 = False
    #         shape1 = placement1[0]
    #         row1 = placement1[1]
    #         col1 = placement1[2]
    #         cat1 = placement1[3]
    #         if board.can_place(shape1, row1, col1):
    #             board.place_piece(shape1, row1, col1, cat1)
    #             flag1 = True
    #             count_attempts += 1
    #             if not(board.is_feasible()):
    #                 board.remove_piece(shape1, row1, col1)
    #                 continue

    #         for placement2 in list_all[2]:
    #             if flag2:
    #                 board.remove_piece(shape2, row2, col2)
    #                 flag2 = False
    #             shape2 = placement2[0]
    #             row2 = placement2[1]
    #             col2 = placement2[2]
    #             cat2 = placement2[3]
    #             if board.can_place(shape2, row2, col2):
    #                 board.place_piece(shape2, row2, col2, cat2)
    #                 flag2 = True
    #                 count_attempts += 1
    #                 if not(board.is_feasible()):
    #                     board.remove_piece(shape2, row2, col2)
    #                     continue

    #             for placement3 in list_all[3]:
    #                 shape3 = placement3[0]
    #                 row3 = placement3[1]
    #                 col3 = placement3[2]
    #                 cat3 = placement3[3]
    #                 if board.can_place(shape3, row3, col3):
    #                     board.place_piece(shape3, row3, col3, cat3)
    #                     count_attempts += 1
    #                     if len(list_empty_positions(board)) == 0:
    #                         return True, count_attempts
    #                     else:
    #                         board.remove_piece(shape3, row3, col3)
    #                 board.print_board()

    
    # for placement0 in list_all[0]:
    #     # board.remove_piece(shape0, row0, col0)
    #     # board.remove_piece(shape1, row1, col1)
    #     # board.remove_piece(shape2, row2, col2)
    #     shape0 = placement0[0]
    #     row0 = placement0[1]
    #     col0 = placement0[2]
    #     cat0 = placement0[3]
    #     if board.can_place(shape0, row0, col0):
    #         board.place_piece(shape0, row0, col0, cat0)
    #         count_attempts += 1
    #         if not(board.is_feasible()):
    #             board.remove_piece(shape0, row0, col0)
    #             continue

    #     for placement1 in list_all[1]:
    #         shape1 = placement1[0]
    #         row1 = placement1[1]
    #         col1 = placement1[2]
    #         cat1 = placement1[3]
    #         if board.can_place(shape1, row1, col1):
    #             board.place_piece(shape1, row1, col1, cat1)
    #             count_attempts += 1
    #             if not(board.is_feasible()):
    #                 board.remove_piece(shape1, row1, col1)
    #                 continue

    #         for placement2 in list_all[2]:
    #             shape2 = placement2[0]
    #             row2 = placement2[1]
    #             col2 = placement2[2]
    #             cat2 = placement0[3]
    #             if board.can_place(shape2, row2, col2):
    #                 board.place_piece(shape2, row2, col2, cat2)
    #                 count_attempts += 1
    #                 if not(board.is_feasible()):
    #                     board.remove_piece(shape2, row2, col2)
    #                     continue

    #             for placement3 in list_all[1]:
    #                 shape3 = placement3[0]
    #                 row3 = placement3[1]
    #                 col3 = placement3[2]
    #                 cat3 = placement3[3]
    #                 if board.can_place(shape3, row3, col3):
    #                     board.place_piece(shape3, row3, col3, cat3)
    #                     count_attempts += 1
    #                     if len(list_empty_positions(board)) == 0:
    #                         return True, count_attempts
    #                     else:
    #                         board.remove_piece(shape3, row3, col3)
    #                 board.print_board()

    # return False, count_attempts


    
    
    
    
    
    
    
    
    
    
    
    
    
    




    
    
    
    
    
    
    
    # count_attempts = 0 

    # board.print_board()
    # if piece_index >= len(pieces):
    #     print("result: ")
    #     board.print_board()
    #     return True, count_attempts

    # piece = pieces[piece_index]
    # for orientation in piece.shapes:
    #     for row in range(board.rows):
    #         for col in range(board.cols):
    #             if board.can_place(orientation, row, col):
    #                 board.place_piece(orientation, row, col, piece.cat)
    #                 count_attempts += 1 
    #                 solved, count = solve_brute_force(board, pieces, piece_index + 1)
    #                 count_attempts += count  
    #                 if solved:
    #                     return True, count_attempts
    #                 board.remove_piece(orientation, row, col)
    # return False, count_attempts

