import tkinter as tk
import ctypes

#   shortcuts to the WinAPI functionality
set_window_pos = ctypes.windll.user32.SetWindowPos
set_window_long = ctypes.windll.user32.SetWindowLongPtrW
get_window_long = ctypes.windll.user32.GetWindowLongPtrW
get_parent = ctypes.windll.user32.GetParent

#   some of the WinAPI flags
GWL_STYLE = -16  # GetWindowLong - -16 sets a new window style - GetWindowLongPtrA function (winuser.h)

WS_MINIMIZEBOX = 131072 # The window has a minimize button
WS_MAXIMIZEBOX = 65536  # The window has a maximize button

''' z order is the layer of windows'''
SWP_NOZORDER = 4 # retains the current z order
SWP_NOMOVE = 2 # Retains the current position (ignores X and Y parameters).
SWP_NOSIZE = 1 # Retains the current size (ignores the cx and cy parameters). 
SWP_FRAMECHANGED = 32 # Applies new frame styles set using the SetWindowLong function


def hide_minimize_maximize(window):
    hwnd = get_parent(window.winfo_id())            # think get the parents window
    old_style = get_window_long(hwnd, GWL_STYLE)    # getting the old style
    new_style = old_style & ~ WS_MAXIMIZEBOX & ~ WS_MINIMIZEBOX #   building the new style (old style AND NOT Maximize AND NOT Minimize)
    set_window_long(hwnd, GWL_STYLE, new_style) #   setting new style
    set_window_pos(hwnd, 0, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED) #   updating non-client area


def show_minimize_maximize(window):
    hwnd = get_parent(window.winfo_id())
    #   getting the old style
    old_style = get_window_long(hwnd, GWL_STYLE)
    #   building the new style (old style OR Maximize OR Minimize)
    new_style = old_style | WS_MAXIMIZEBOX | WS_MINIMIZEBOX
    #   setting new style
    set_window_long(hwnd, GWL_STYLE, new_style)
    #   updating non-client area
    set_window_pos(hwnd, 0, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED)


def top():
    tp = tk.Toplevel()
    #   tp.geometry('300x300')
    #   tp.iconbitmap('icon.ico')

    hide_minmax = tk.Button(tp, text='hide minimize/maximize', command=lambda: hide_minimize_maximize(tp))
    hide_minmax.pack()

    show_minmax = tk.Button(tp, text='show minimize/maximize', command=lambda: show_minimize_maximize(tp))
    show_minmax.pack()

root = tk.Tk()
root.geometry('400x400')
b = tk.Button(root, text='open window with icon', command=top)
b.pack()

root.mainloop()
