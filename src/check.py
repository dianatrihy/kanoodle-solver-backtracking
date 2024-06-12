def check_single_zero(board, i, j):
    """Check if the single 0 at board[i][j] is surrounded by 1s or board edges"""
    if board[i][j] != 0:
        return False

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[0]):
            if board[ni][nj] == 0:
                return False
    return True

def check_two_zeros(board, i, j, orientation):
    """Check if two consecutive 0s at board[i][j] are surrounded by 1s or board edges"""
    if orientation == "horizontal":
        if j + 1 >= len(board[0]) or board[i][j] != 0 or board[i][j + 1] != 0:
            return False
        if (i > 0 and (board[i - 1][j] == 0 or board[i - 1][j + 1] == 0)) or \
            (i < len(board) - 1 and (board[i + 1][j] == 0 or board[i + 1][j + 1] == 0)) or \
            (j > 0 and board[i][j - 1] == 0) or (j + 2 < len(board[0]) and board[i][j + 2] == 0):
            return False
    elif orientation == "vertical":
        if i + 1 >= len(board) or board[i][j] != 0 or board[i + 1][j] != 0:
            return False
        if (j > 0 and (board[i][j - 1] == 0 or board[i + 1][j - 1] == 0)) or \
            (j < len(board[0]) - 1 and (board[i][j + 1] == 0 or board[i + 1][j + 1] == 0)) or \
            (i > 0 and board[i - 1][j] == 0) or (i + 2 < len(board) and board[i + 2][j] == 0):
            return False
    return True

def check_three_zeros(board, i, j, orientation):
    """Check if three consecutive 0s at board[i][j] are surrounded by 1s or board edges"""
    if orientation == "horizontal":
        if j + 2 >= len(board[0]) or board[i][j] != 0 or board[i][j + 1] != 0 or board[i][j + 2] != 0:
            return False
        if (i > 0 and (board[i - 1][j] == 0 or board[i - 1][j + 1] == 0 or board[i - 1][j + 2] == 0)) or \
            (i < len(board) - 1 and (board[i + 1][j] == 0 or board[i + 1][j + 1] == 0 or board[i + 1][j + 2] == 0)) or \
            (j > 0 and board[i][j - 1] == 0) or (j + 3 < len(board[0]) and board[i][j + 3] == 0):
            return False
    elif orientation == "vertical":
        if i + 2 >= len(board) or board[i][j] != 0 or board[i + 1][j] != 0 or board[i + 2][j] != 0:
            return False
        if (j > 0 and (board[i][j - 1] == 0 or board[i + 1][j - 1] == 0 or board[i + 2][j - 1] == 0)) or \
            (j < len(board[0]) - 1 and (board[i][j + 1] == 0 or board[i + 1][j + 1] == 0 or board[i + 2][j + 1] == 0)) or \
            (i > 0 and board[i - 1][j] == 0) or (i + 3 < len(board) and board[i + 3][j] == 0):
            return False
    return True

def check_five_zeros(board, i, j, orientation):
    """Check if five consecutive 0s at board[i][j] are surrounded by 1s or board edges"""
    if orientation == "horizontal":
        if j + 4 >= len(board[0]) or board[i][j] != 0 or board[i][j + 1] != 0 or \
            board[i][j + 2] != 0 or board[i][j + 3] != 0 or board[i][j + 4] != 0:
            return False
        if (i > 0 and (board[i - 1][j] == 0 or board[i - 1][j + 1] == 0 or board[i - 1][j + 2] == 0 or \
                        board[i - 1][j + 3] == 0 or board[i - 1][j + 4] == 0)) or \
            (i < len(board) - 1 and (board[i + 1][j] == 0 or board[i + 1][j + 1] == 0 or board[i + 1][j + 2] == 0 or \
                                    board[i + 1][j + 3] == 0 or board[i + 1][j + 4] == 0)) or \
            (j > 0 and board[i][j - 1] == 0) or (j + 5 < len(board[0]) and board[i][j + 5] == 0):
            return False
    elif orientation == "vertical":
        if i + 4 >= len(board) or board[i][j] != 0 or board[i + 1][j] != 0 or \
            board[i + 2][j] != 0 or board[i + 3][j] != 0 or board[i + 4][j] != 0:
            return False
        if (j > 0 and (board[i][j - 1] == 0 or board[i + 1][j - 1] == 0 or board[i + 2][j - 1] == 0 or \
                        board[i + 3][j - 1] == 0 or board[i + 4][j - 1] == 0)) or \
            (j < len(board[0]) - 1 and (board[i][j + 1] == 0 or board[i + 1][j + 1] == 0 or board[i + 2][j + 1] == 0 or \
                                    board[i + 3][j + 1] == 0 or board[i + 4][j + 1] == 0)) or \
            (i > 0 and board[i - 1][j] == 0) or (i + 5 < len(board) and board[i + 5][j] == 0):
            return False
    return True

def check_two_by_three_zeros(board, i, j):
    """Check if a 2x3 block of 0s at board[i][j] is surrounded by 1s or board edges"""
    # Check 2x3 block
    if i + 1 < len(board) and j + 2 < len(board[0]) and \
        board[i][j] == 0 and board[i][j + 1] == 0 and board[i][j + 2] == 0 and \
        board[i + 1][j] == 0 and board[i + 1][j + 1] == 0 and board[i + 1][j + 2] == 0:
        if (i > 0 and (board[i - 1][j] == 0 or board[i - 1][j + 1] == 0 or board[i - 1][j + 2] == 0)) or \
            (i + 2 < len(board) and (board[i + 2][j] == 0 or board[i + 2][j + 1] == 0 or board[i + 2][j + 2] == 0)) or \
            (j > 0 and (board[i][j - 1] == 0 or board[i + 1][j - 1] == 0)) or \
            (j + 3 < len(board[0]) and (board[i][j + 3] == 0 or board[i + 1][j + 3] == 0)):
            return False
        return True

    # Check 3x2 block
    if i + 2 < len(board) and j + 1 < len(board[0]) and \
        board[i][j] == 0 and board[i][j + 1] == 0 and \
        board[i + 1][j] == 0 and board[i + 1][j + 1] == 0 and \
        board[i + 2][j] == 0 and board[i + 2][j + 1] == 0:
        if (i > 0 and (board[i - 1][j] == 0 or board[i - 1][j + 1] == 0)) or \
            (i + 3 < len(board) and (board[i + 3][j] == 0 or board[i + 3][j + 1] == 0)) or \
            (j > 0 and (board[i][j - 1] == 0 or board[i + 1][j - 1] == 0 or board[i + 2][j - 1] == 0)) or \
            (j + 2 < len(board[0]) and (board[i][j + 2] == 0 or board[i + 1][j + 2] == 0 or board[i + 2][j + 2] == 0)):
            return False
        return True

    return False

def check_board(board):
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            if check_single_zero(board, i, j):
                return False
            if check_two_zeros(board, i, j, "horizontal") or check_two_zeros(board, i, j, "vertical"):
                return False
            if check_three_zeros(board, i, j, "horizontal") or check_three_zeros(board, i, j, "vertical"):
                return False
            if check_five_zeros(board, i, j, "horizontal") or check_five_zeros(board, i, j, "vertical"):
                return False
            if check_two_by_three_zeros(board, i, j):
                return False
            
    return True

# board = [
#     [0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 0]
# ]

# single_zero, two_zeros, three_zeros = check_board(board)
# print(f"Single zero surrounded by 1s: {single_zero}")
# print(f"Two consecutive zeros surrounded by 1s: {two_zeros}")
# print(f"Three consecutive zeros surrounded by 1s: {three_zeros}")
