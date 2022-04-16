"""
keyboard input
"""

import keyboard

def search_input() -> str or None:
    key = None
    if keyboard.is_pressed('w'):
        key = 'up'

    if keyboard.is_pressed('s'):
        key = 'down'
        
    if keyboard.is_pressed('a'):
        key = 'left'

    if keyboard.is_pressed('d'):
        key = 'right'
    
    return key