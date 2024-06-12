import check

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]

    def can_place(self, piece_shape, row, col):
        for r in range(len(piece_shape)):
            for c in range(len(piece_shape[r])):
                if piece_shape[r][c] == 1:
                    if (row + r >= self.rows or col + c >= self.cols or self.board[row + r][col + c] != 0):
                        return False
        return True

    def place_piece(self, piece_shape, row, col, val):
        for r in range(len(piece_shape)):
            for c in range(len(piece_shape[r])):
                if piece_shape[r][c] == 1:
                    self.board[row + r][col + c] = val
        self.print_board()

    def add_piece(self, piece_shape, row, col):
        self.place_piece(piece_shape, row, col, piece_shape.cat())

    def remove_piece(self, piece_shape, row, col):
        self.place_piece(piece_shape, row, col, 0)

    def is_feasible(self):
        return check.check_board(self.board)

    def print_board(self):
        print('----------------------')
        for row in self.board:
            print(' '.join(map(str, row)))

    def copy(self):
        new_board = Board(self.rows, self.cols)
        new_board.board = [row[:] for row in self.board]
        return new_board
    
    def set_board(self, new_board):
        if len(new_board) != self.rows or any(len(row) != self.cols for row in new_board):
            raise ValueError("Input board dimensions do not match the Board dimensions.")
        self.board = [row[:] for row in new_board]
        self.board = [[cell if cell != '0' else 0 for cell in row] for row in new_board]

    def get_unique_letters(self):
        unique_letters = set()
        for row in self.board:
            for cell in row:
                if cell != 0:
                    unique_letters.add(cell)
        return unique_letters
    
    def list_empty_positions(self):
        empty_positions = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    empty_positions.append((row, col))
        return empty_positions