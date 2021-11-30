import tkinter as tk

root = tk.Tk()
counter = 0

def change_text():
    global counter
    my_list = [".", "..", "...", ""]
    if counter != 3:
        l.config(text="Loading{}".format(my_list[counter]))
        counter += 1
        root.after(1000, change_text)
    else:
        l.config(text="Loading{}".format(my_list[counter]))
        counter = 0
        root.after(1000, change_text)

l = tk.Label(root, text = "")
l.pack()

change_text()
root.mainloop()