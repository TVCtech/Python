if "ctypes" in dir():
  print("cytpes already imported")
else: import ctypes

# ---------------------------- Stealing Window Focus Setup: ----------------------- # 
'''Setup for window stealing focus win api interaction
some keys have double send key mappings , extend key is a flag to show which one'''
set_to_foreground = ctypes.windll.user32.SetForegroundWindow
keybd_event = ctypes.windll.user32.keybd_event
alt_key = 0x12
extended_key = 0x0001 
key_up = 0x0002

def steal_focus(window):
    '''Performs an alt-tab to get the window to steal focus'''
    keybd_event(alt_key, 0, extended_key | 0, 0)
    set_to_foreground(window.winfo_id())
    keybd_event(alt_key, 0, extended_key | key_up, 0)

def raise_above_all(window):
    '''brings a window to the top'''
    # Restore if window is minimized
    window.state("normal")
    window.deiconify()
    # Bring to top level above all windows
    window.attributes("-topmost", True)
    window.focus_force()
    # Allows other windows to top level again
    window.attributes("-topmost", False)
    steal_focus(window)
    
if __name__ == '__main__':
    print('module will Steal window Focus!')