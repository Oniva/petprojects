#! python 3
#  pos

import pyautogui, time, os


try:
    while True:
        currentMouseX, currentMouseY = pyautogui.position()
        print("%s, %s" % (currentMouseX, currentMouseY))
        time.sleep(5)
except KeyboardInterrupt:
    quit()
    clear = lambda: os.system('clear')
    clear()














    