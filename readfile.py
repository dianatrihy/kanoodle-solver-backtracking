def read_pieces_from_file(file_content):
    pieces = {}
    current_piece = None
    current_orientations = []
    lines = file_content.strip().split('\n')

    line_index = 0
    while line_index < len(lines):
        line = lines[line_index].strip()
        if not line:
            line_index += 1
            continue
        if len(line) == 1 and line.isalpha():
            if current_piece is not None:
                pieces[current_piece] = current_orientations
            current_piece = line
            current_orientations = []
        elif line == ';':
            if current_piece is not None:
                pieces[current_piece] = current_orientations
            current_piece = None
        else:
            orientation = []
            while line_index < len(lines) and lines[line_index].strip() and not (len(lines[line_index].strip()) == 1 and lines[line_index].strip().isalpha()) and lines[line_index].strip() != ';':
                orientation.append(list(map(int, lines[line_index].strip().split())))
                line_index += 1
            current_orientations.append(orientation)
            line_index -= 1  # adjust index as it will be incremented at the end of the loop
        line_index += 1

    if current_piece is not None:
        pieces[current_piece] = current_orientations

    return pieces

def get_piece_orientations(piece_letter):
    filename = 'noodles.txt'
    file_content = read_file(filename)
    pieces = read_pieces_from_file(file_content)
    
    return pieces.get(piece_letter, [])

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# # Contoh penggunaan
# filename = 'noodles.txt'
# file_content = read_file(filename)

# pieces = read_pieces_from_file(file_content)
# piece_letter = 'B'
# orientations = get_piece_orientations(pieces, piece_letter)
# print(f"Orientations for piece {piece_letter}:")
# for orientation in orientations:
#     for row in orientation:
#         print(row)
#     print()
