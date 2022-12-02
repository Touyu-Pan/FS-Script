import random
import pyautogui
import keyboard
import os
import threading


def run():
    # Run script every n seconds
    threading.Timer(6, run).start()

    # mouse control
    # close alert window
    pyautogui.moveTo(x=1525, y=953, duration=0.5)
    pyautogui.click()

    pyautogui.moveTo(x=1224, y=806, duration=0.5)
    pyautogui.click()

    pyautogui.moveTo(x=1313, y=822, duration=0.5)
    pyautogui.click()

    # start game
    pyautogui.moveTo(x=1411, y=859, duration=0.5)
    pyautogui.click()

    pyautogui.moveTo(x=1475, y=973, duration=0.5)
    pyautogui.click()

    

def terminate_():
    print('terminated.')
    os._exit(0)

# for stop this program
exit_key = 'esc'
print(f"Press \'{exit_key}\' to exit program")
keyboard.add_hotkey(exit_key, lambda: terminate_())

run()
