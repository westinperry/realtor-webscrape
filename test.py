import pyautogui
import time

def click_and_hold(x, y, hold_time):
    """
    Click and hold the mouse at the specified (x, y) coordinates for a given amount of time.

    :param x: The x-coordinate for the mouse click.
    :param y: The y-coordinate for the mouse click.
    :param hold_time: The amount of time in seconds to hold the mouse button down.
    """
    pyautogui.moveTo(x, y)   # Move the mouse to the specified coordinates
    pyautogui.mouseDown()    # Press the mouse button down
    time.sleep(hold_time)    # Wait for the specified hold time
    pyautogui.mouseUp()      # Release the mouse button

click_and_hold(1400, 1600, 1)