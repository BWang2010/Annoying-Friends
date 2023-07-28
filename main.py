import tkinter as tk
from tkinter import messagebox

if __name__ == "__main__":
    root = tk.Tk()  # Main canvas
    root.title("Simple Pop-up GUI")  # Labelling the main canvas

    popup_button = tk.Button(root, text="Show Pop-up", command=messagebox.showinfo("Pop-up", "Pop-up checking"))  # Click button to activate pop-up
    popup_button.pack(pady=20)

    root.mainloop()



