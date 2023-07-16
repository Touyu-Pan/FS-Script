import pyautogui
import keyboard
import os
import threading


def run():
    # Run script every n seconds
    threading.Timer(1, run).start()

    pyautogui.click(x=1539, y=733)
    pyautogui.click(x=1438, y=636)
    pyautogui.click(x=1331, y=676)
    pyautogui.click(x=1332, y=918)
    pyautogui.click(x=1337, y=918)
    pyautogui.click(x=1451, y=873)


def terminate_():
    print('terminated.')
    os._exit(0)

# for stop this program
exit_key = 'esc'
print(f"Press \'{exit_key}\' to exit program")
keyboard.add_hotkey(exit_key, lambda: terminate_())

run()