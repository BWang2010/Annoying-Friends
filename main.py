import tkinter as tk
import random







def callback(e):
    x= e.x
    y= e.y
    print("Pointer is currently at %d, %d" %(x,y))

def update_position():
    red_x.place(x=random.randint(0,screen_height), y=random.randint(0,screen_width))
    win.after(1000,update_position)


if __name__ == "__main__":
    global win , red_x
    win = tk.Tk()  # Main canvas
    win.title("Simple Pop-up GUI")  # Labelling the main canvas
    win.overrideredirect(1)  # Remove border
    # Hide the main canvas

    # Set the position of the pop-up window
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win.geometry(f"{screen_width}x{screen_height}")
    label = tk.Label(win, text="Click the red x to close")
    label.pack(pady=20)
    win.bind('<Motion>',callback)
    red_x=tk.Button(win,text="X",bg="red", fg="white",width=2,height = 1,relief="flat",command=win.destroy)
    red_x.pack()
    update_position()
    win.mainloop()


