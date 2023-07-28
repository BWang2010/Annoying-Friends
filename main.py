import tkinter as tk
from tkinter import messagebox


if __name__ == "__main__":
    root = tk.Tk()  # Main canvas
    root.title("Simple Pop-up GUI")  # Labelling the main canvas
    root.withdraw()  # Hide the main canvas

    messagebox.showinfo("Pop-up", "Click the red x to close")

    root.mainloop()



