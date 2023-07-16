import pyautogui
import keyboard
import os
import threading


def run():
    # Run script every n seconds
    threading.Timer(1, run).start()

    pyautogui.click(x=1217, y=555)
    pyautogui.click(x=1121, y=455)
    pyautogui.click(x=1012, y=498)
    pyautogui.click(x=1015, y=733)
    pyautogui.click(x=1018, y=736)
    pyautogui.click(x=1134, y=691)


def terminate_():
    print('terminated.')
    os._exit(0)

# for stop this program
exit_key = 'esc'
print(f"Press \'{exit_key}\' to exit program")
keyboard.add_hotkey(exit_key, lambda: terminate_())

run()