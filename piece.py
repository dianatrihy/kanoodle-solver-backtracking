import readfile as rf

class Piece:
    def __init__(self, cat):
        self.cat = cat
        self.shapes = rf.get_piece_orientations(cat)

    def get_cat(self):
        return self.cat

    def get_shapes(self):
        return self.shapes
    
    

