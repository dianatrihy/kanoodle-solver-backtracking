import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import piece
import board
import time
import bruteforce
import backtracking

class KanoodleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanoodle Solver")
        
        self.board = board.Board(5, 11)
        self.option = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        self.noodles = ["L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
        self.pieces = [piece.Piece(noodle) for noodle in self.noodles]
        self.selected_piece = None
        self.selected_orientation = None
        self.placed_pieces = set()
        self.color_mapping = self.create_color_mapping()

        self.create_widgets()

    def create_color_mapping(self):
        colors = [
            "#FF6666", "#FFCC66", "#FFFF66", "#CCFF66", "#66FF66",
            "#66FFCC", "#66FFFF", "#66CCFF", "#6666FF", "#CC66FF",
            "#FF66FF", "#FF66CC"
        ]
        return {self.noodles[i]: colors[i] for i in range(len(self.noodles))}

    def create_widgets(self):
        self.frame_controls = ttk.Frame(self.root)
        self.frame_controls.grid(row=0, column=0, padx=10, pady=10)

        self.btn_show_image = ttk.Button(self.frame_controls, text="Show References", command=self.show_image)
        self.btn_show_image.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        self.lbl_piece = ttk.Label(self.frame_controls, text="Choose Piece:")
        self.lbl_piece.grid(row=1, column=0, padx=5, pady=5)
        
        self.cmb_piece = ttk.Combobox(self.frame_controls, values=self.option)
        self.cmb_piece.grid(row=1, column=1, padx=5, pady=5)
        self.cmb_piece.bind("<<ComboboxSelected>>", self.update_orientations)
        
        self.lbl_orientation = ttk.Label(self.frame_controls, text="Choose Orientation:")
        self.lbl_orientation.grid(row=2, column=0, padx=5, pady=5)
        
        self.cmb_orientation = ttk.Combobox(self.frame_controls, state='disabled')
        self.cmb_orientation.grid(row=2, column=1, padx=5, pady=5)
        
        self.lbl_row = ttk.Label(self.frame_controls, text="Row (0-4):")
        self.lbl_row.grid(row=3, column=0, padx=5, pady=5)
        
        self.ent_row = ttk.Entry(self.frame_controls)
        self.ent_row.grid(row=3, column=1, padx=5, pady=5)
        
        self.lbl_col = ttk.Label(self.frame_controls, text="Column (0-10):")
        self.lbl_col.grid(row=4, column=0, padx=5, pady=5)
        
        self.ent_col = ttk.Entry(self.frame_controls)
        self.ent_col.grid(row=4, column=1, padx=5, pady=5)
        
        self.btn_place = ttk.Button(self.frame_controls, text="Place Piece", command=self.place_piece)
        self.btn_place.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.lbl_algorithm = ttk.Label(self.frame_controls, text="Choose Algorithm:")
        self.lbl_algorithm.grid(row=6, column=0, padx=5, pady=5)

        self.cmb_algorithm = ttk.Combobox(self.frame_controls, values=["Backtracking", "Brute Force"], state='readonly')
        self.cmb_algorithm.grid(row=6, column=1, padx=5, pady=5)
        
        self.btn_solve = ttk.Button(self.frame_controls, text="Solve", command=self.solve)
        self.btn_solve.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        
        self.btn_reset = ttk.Button(self.frame_controls, text="Reset", command=self.reset)
        self.btn_reset.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.btn_load_file = ttk.Button(self.frame_controls, text="Load Board from File", command=self.load_board_from_file)
        self.btn_load_file.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        self.frame_board = ttk.Frame(self.root)
        self.frame_board.grid(row=1, column=0, padx=10, pady=10)
        
        self.canvas = tk.Canvas(self.frame_board, width=550, height=250, bg='white')
        self.canvas.pack()

        self.draw_board()

        self.lbl_credit = ttk.Label(self.root, text="Created by dianatrihy   \n                          🐨🐨🐨")
        self.lbl_credit.grid(row=2, column=0, pady=5, sticky="e")

    def update_orientations(self, event):
        selected_piece = self.cmb_piece.get()
        idx = self.noodles.index(selected_piece)
        self.selected_piece = self.pieces[idx]
        
        orientations = [f"Orientation {i+1}" for i in range(len(self.selected_piece.shapes))]
        self.cmb_orientation['values'] = orientations
        self.cmb_orientation['state'] = 'readonly'

    def draw_board(self):
        self.canvas.delete("all")
        cell_size = 50
        for r in range(5):
            for c in range(11):
                x1 = c * cell_size
                y1 = r * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                color = 'white'
                if self.board.board[r][c] != 0:
                    color = self.color_mapping[self.board.board[r][c]]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')
                if self.board.board[r][c] != 0:
                    self.canvas.create_text(x1 + cell_size/2, y1 + cell_size/2, text=self.board.board[r][c], font=('Arial', 20))

    def place_piece(self):
        if not self.selected_piece or self.cmb_orientation.get() == '':
            messagebox.showerror("Error", "Please select a piece and orientation.")
            return
        
        if self.selected_piece.cat in self.placed_pieces:
            messagebox.showerror("Error", f"Piece {self.selected_piece.cat} has already been placed.")
            return
        
        row = int(self.ent_row.get())
        col = int(self.ent_col.get())
        orientation_index = int(self.cmb_orientation.get().split()[1]) - 1
        orientation = self.selected_piece.shapes[orientation_index]
        
        if self.board.can_place(orientation, row, col):
            self.board.place_piece(orientation, row, col, self.selected_piece.cat)
            self.placed_pieces.add(self.selected_piece.cat)
            self.pieces.remove(self.selected_piece)
            self.noodles.remove(self.selected_piece.cat)
            self.draw_board()
            self.cmb_piece.set('')
            self.cmb_orientation.set('')
            self.cmb_orientation['state'] = 'disabled'
            self.ent_row.delete(0, tk.END)
            self.ent_col.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid position or orientation.")

    def load_board_from_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = file.readlines()
                    new_board = [line.strip().split() for line in data]
                    self.board.set_board(new_board)
                    unique = self.board.get_unique_letters()
                    print(unique)
                    print(self.noodles)
                    for u in unique:
                        self.noodles.remove(u)
                    self.pieces.clear()
                    self.pieces = [piece.Piece(noodle) for noodle in self.noodles]
                    self.draw_board()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while loading the file: {str(e)}")
    
    def solve(self):
        algorithm = self.cmb_algorithm.get()
        count = 0
        if not algorithm:
            messagebox.showerror("Error", "Please select an algorithm.")
            return

        start_time = time.time()
        if self.board.is_feasible():
            if algorithm == "Backtracking":
                solved, count = backtracking.solve_backtracking(self.board, self.pieces, 0)
            elif algorithm == "Brute Force":
                solved, count = bruteforce.solve_brute_force(self.board, self.pieces)
            else:
                solved = False

            if not solved:
                messagebox.showinfo("Result", "No solution found.")
            else:
                self.draw_board()
        else:
            messagebox.showerror("Error", "Initial board state is not feasible.")
        end_time = time.time()
        execution_time = end_time - start_time
        messagebox.showinfo("Result", f"Total attempts: {count}\nExecution Time: {execution_time:.2f} seconds")

    def reset(self):
        self.board = board.Board(5, 11)
        self.noodles = ["L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
        self.pieces = [piece.Piece(noodle) for noodle in self.noodles]
        self.placed_pieces.clear()
        self.selected_piece = None
        self.selected_orientation = None
        self.cmb_piece.set('')
        self.cmb_orientation.set('')
        self.cmb_orientation['state'] = 'disabled'
        self.ent_row.delete(0, tk.END)
        self.ent_col.delete(0, tk.END)
        self.draw_board()

    def show_image(self):
        image_window = tk.Toplevel(self.root)
        image_window.title("Kanoodle Image")
        
        img = Image.open("path_to_your_image.jpg")  # Ganti dengan path gambar Anda
        img = img.resize((400, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        
        label = ttk.Label(image_window, image=photo)
        label.image = photo
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = KanoodleApp(root)
    root.mainloop()
