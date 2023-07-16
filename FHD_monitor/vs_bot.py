import pyautogui
import pydirectinput
import threading
import random
import keyboard
import os

# for 1920*1080 size screen
# run script
def run():
    # Run script every n seconds
    threading.Timer(random.uniform(8.0, 8.3), run).start()

    # mouse controlss
    # close alert window

    pyautogui.click(x=958, y=603)
    key_event_('s')

    # start game
    pyautogui.click(x=1520, y=885)

    # surrender
    pyautogui.click(x=348, y=845)

    # keyboard control
    # movement
    key_event_('up')
    key_event_('down')
    key_event_('d')
    key_event_('left')
    key_event_('right')
    key_event_('d')

    print('done.')


def key_event_(key):
    pydirectinput.keyDown(key)
    threading.Event().wait(random.uniform(0.1, 0.25))
    pydirectinput.keyUp(key)

def terminate_():
    print('terminated.')
    os._exit(0)

# for stop this program
exit_key = 'esc'
print(f"Press \'{exit_key}\' to exit program")
keyboard.add_hotkey(exit_key, lambda: terminate_())

run()

# python C:\Users\Jeff\Desktop\code\myDjango.py