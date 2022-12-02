import random
import pyautogui
import keyboard
import os
import threading


def run():
    # Run script every n seconds
    threading.Timer(0.5, run).start()

    # mouse control
    # close alert window
    pyautogui.moveTo(x=1384, y=879, duration=1)
    pyautogui.click()

    # start game
    pyautogui.moveTo(x=1300, y=817, duration=1)
    pyautogui.click()

def terminate_():
    print('terminated.')
    os._exit(0)

# for stop this program
exit_key = 'esc'
print(f"Press \'{exit_key}\' to exit program")
keyboard.add_hotkey(exit_key, lambda: terminate_())

run()
