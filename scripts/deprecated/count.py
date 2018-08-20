#! python 3
#  count.py - counts on discord

import sys, pyautogui, time, os

currentCount = int(sys.argv[1])
pyautogui.FailSafeException = True

try:
    #to get to the intended window
    time.sleep(5)
    while True:
        currentCount += 1
        pyautogui.typewrite(str(currentCount))
        pyautogui.press('enter')
        time.sleep(1)

# Handles KeyboardInterrupt properly
except KeyboardInterrupt:
        quit()
        clear = lambda: os.system('clear')
        clear()