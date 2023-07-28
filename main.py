import tkinter as tk
from tkinter import messagebox


def show_custom_popup():
    popup = tk.Toplevel(root)
    popup.title("Custom Pop-up")

    # Set the position of the pop-up window
    popup.geometry("400x400+2000+200")  # Width x Height + X_Offset + Y_Offset

    label = tk.Label(popup, text="Click the red x to close")
    label.pack(pady=20)

    popup.mainloop()


if __name__ == "__main__":
    root = tk.Tk()  # Main canvas
    root.title("Simple Pop-up GUI")  # Labelling the main canvas
    root.withdraw()  # Hide the main canvas

    show_custom_popup()

    root.mainloop()




