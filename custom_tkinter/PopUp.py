from tkinter import messagebox


class PopUp:
    CONFIRM = "yes"
    DENY = "no"

    # Asks if user wants to watch puzzle being solved or just see final solution.
    # Returns "yes" or "no".
    @staticmethod
    def question():
        return messagebox.askquestion("Watch Solution Unfold?",
                                      "Would you like to watch the solution to the Sudoku board "
                                      "unfold?")

    # Informs user that invalid board was created.
    @staticmethod
    def error(parent):
        return messagebox.showerror("Invalid Board Created",
                                    "You created an invalid Sudoku board; there are no solutions. "
                                    "Please create a new board.", parent=parent)

    # Informs user that no solution exists.
    @staticmethod
    def info():
        return messagebox.showinfo("No Solution Exists",
                                   "The provided Sudoku board has no solutions. Please create a new board.")
