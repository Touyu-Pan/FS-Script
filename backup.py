from asyncore import loop
import pyautogui
import pydirectinput
import threading
import random
import keyboard
import os

# run script
def run():
    # Run script every n seconds
    threading.Timer(random.uniform(8.0, 8.3), run).start()

    # mouse control
    # close alert window
    pyautogui.click(x=1278, y=783)
    key_event_('s')
    
    # start game
    pyautogui.click(x=1840, y=1065)

    # surrender
    pyautogui.click(x=668, y=1025)

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