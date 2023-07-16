import random
import pyautogui
import keyboard
import os
import threading

def kb():
    threading.Timer(random.uniform(0.1, 0.12), kb).start()
    pyautogui.click()

def terminate_():
    print('terminated.')
    os._exit(0)

# for stop this program
exit_key = 'esc'
print(f"Press \'{exit_key}\' to exit program")
keyboard.add_hotkey(exit_key, lambda: terminate_())

kb()


