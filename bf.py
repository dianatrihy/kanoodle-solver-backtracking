def bf4(board, list_all, count_attempts):
    placement0 = list_all[0][0]
    shape0 = placement0[0]
    row0 = placement0[1]
    col0 = placement0[2]
    placement1 = list_all[1][0]
    shape1 = placement1[0]
    row1 = placement1[1]
    col1 = placement1[2]
    placement2 = list_all[2][0]
    shape2 = placement2[0]
    row2 = placement2[1]
    col2 = placement2[2]
    placement3 = list_all[3][0]
    shape3 = placement3[0]
    row3 = placement3[1]
    col3 = placement3[2]

    flag0 = False
    flag1 = False
    flag2 = False

    for placement0 in list_all[0]:
        if flag0:
            board.remove_piece(shape0, row0, col0)
            flag0 = False
        shape0 = placement0[0]
        row0 = placement0[1]
        col0 = placement0[2]
        cat0 = placement0[3]
        if board.can_place(shape0, row0, col0):
            board.place_piece(shape0, row0, col0, cat0)
            flag0 = True
            count_attempts += 1
            if not(board.is_feasible()):
                board.remove_piece(shape0, row0, col0)
                continue

        for placement1 in list_all[1]:
            if flag1:
                board.remove_piece(shape1, row1, col1)
                flag1 = False
            shape1 = placement1[0]
            row1 = placement1[1]
            col1 = placement1[2]
            cat1 = placement1[3]
            if board.can_place(shape1, row1, col1):
                board.place_piece(shape1, row1, col1, cat1)
                flag1 = True
                count_attempts += 1
                if not(board.is_feasible()):
                    board.remove_piece(shape1, row1, col1)
                    continue

            for placement2 in list_all[2]:
                if flag2:
                    board.remove_piece(shape2, row2, col2)
                    flag2 = False
                shape2 = placement2[0]
                row2 = placement2[1]
                col2 = placement2[2]
                cat2 = placement2[3]
                if board.can_place(shape2, row2, col2):
                    board.place_piece(shape2, row2, col2, cat2)
                    flag2 = True
                    count_attempts += 1
                    if not(board.is_feasible()):
                        board.remove_piece(shape2, row2, col2)
                        continue

                for placement3 in list_all[3]:
                    shape3 = placement3[0]
                    row3 = placement3[1]
                    col3 = placement3[2]
                    cat3 = placement3[3]
                    if board.can_place(shape3, row3, col3):
                        board.place_piece(shape3, row3, col3, cat3)
                        count_attempts += 1
                        if len(board.list_empty_positions()) == 0:
                            return True, count_attempts
                        else:
                            board.remove_piece(shape3, row3, col3)
                    # board.print_board()

    return False, count_attempts

def bf5(board, list_all, count_attempts):
    placement0 = list_all[0][0]
    shape0 = placement0[0]
    row0 = placement0[1]
    col0 = placement0[2]

    flag0 = False
    flag1 = False
    flag2 = False
    flag3 = False

    for placement0 in list_all[0]:
        if flag0:
            board.remove_piece(shape0, row0, col0)
            flag0 = False
        shape0, row0, col0, cat0 = placement0
        if board.can_place(shape0, row0, col0):
            board.place_piece(shape0, row0, col0, cat0)
            flag0 = True
            count_attempts += 1
            if not(board.is_feasible()):
                board.remove_piece(shape0, row0, col0)
                continue

        for placement1 in list_all[1]:
            if flag1:
                board.remove_piece(shape1, row1, col1)
                flag1 = False
            shape1, row1, col1, cat1 = placement1
            if board.can_place(shape1, row1, col1):
                board.place_piece(shape1, row1, col1, cat1)
                flag1 = True
                count_attempts += 1
                if not(board.is_feasible()):
                    board.remove_piece(shape1, row1, col1)
                    continue

            for placement2 in list_all[2]:
                if flag2:
                    board.remove_piece(shape2, row2, col2)
                    flag2 = False
                shape2, row2, col2, cat2 = placement2
                if board.can_place(shape2, row2, col2):
                    board.place_piece(shape2, row2, col2, cat2)
                    flag2 = True
                    count_attempts += 1
                    if not(board.is_feasible()):
                        board.remove_piece(shape2, row2, col2)
                        continue

                for placement3 in list_all[3]:
                    if flag3:
                        board.remove_piece(shape3, row3, col3)
                        flag3 = False
                    shape3, row3, col3, cat3 = placement3
                    if board.can_place(shape3, row3, col3):
                        board.place_piece(shape3, row3, col3, cat3)
                        flag3 = True
                        count_attempts += 1
                        if not(board.is_feasible()):
                            board.remove_piece(shape3, row3, col3)
                            continue

                    for placement4 in list_all[4]:
                        shape4, row4, col4, cat4 = placement4
                        if board.can_place(shape4, row4, col4):
                            board.place_piece(shape4, row4, col4, cat4)
                            count_attempts += 1
                            if len(board.list_empty_positions()) == 0:
                                return True, count_attempts
                            else:
                                board.remove_piece(shape4, row4, col4)
                        board.print_board()

    return False, count_attempts
