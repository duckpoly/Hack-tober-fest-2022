 # To check if any moves r left
    def hori_possible(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    def verti_possible(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False

    # checking if game over
    def check_end(self):
        if any(2048 in row for row in self.matrix):
            messagebox.showinfo("YOU WIN", "your score is {}".format(self.score))
        elif not any(0 in row for row in self.matrix) and not self.hori_possible() and not self.verti_possible():
            messagebox.showinfo("YOU LOOSE", "your final score is {}".format(self.score))
