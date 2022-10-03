 def new_tile(self):
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        while (self.matrix[row][column] != 0):
            row = random.randint(0, 3)
            column = random.randint(0, 3)
        self.matrix[row][column] = random.choice([2, 4])

    # updating the matrix
    def updation(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if (cell_value == 0):
                    self.cells[i][j]["frame"].configure(bg="azure4")
                    self.cells[i][j]["value"].configure(bg="azure4", text=" ")
                else:
                    self.cells[i][j]["frame"].configure(bg=bg_grid_color[cell_value])
                    self.cells[i][j]["value"].configure(
                        bg=bg_grid_color[cell_value],
                        fg=number_colour[cell_value],
                        text=str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    # when you press left
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.new_tile()
        self.updation()
        self.check_end()

    # when you press right
    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.new_tile()
        self.updation()
        self.check_end()

    # when you press up
    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.new_tile()
        self.updation()
        self.check_end()

    # when you press down
    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.new_tile()
        self.updation()
        self.check_end()
