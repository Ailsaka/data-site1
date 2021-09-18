import win32api
import win32gui
import win32con
from ctypes import *
import time

VK_CODE = {
    'blackspace': 0x08,
    # 'b': 0x42,
    'b': 0x08,
}


def key_press(s=''):
    for c in s:
        win32api.keybd_event(VK_CODE[c], 0, 0, 0)
        win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)


class POINT(object):
    """docstring for POINT"""
    def __init__(self, arg):
        super(POINT, self).__init__()
        self.arg = arg


def mouse_move(x, y):
    windll.user32.SetCursorPos(x, y)


def mouse_click(x=None, y=None):
    if x is not None and y is not None:
        mouse_move(x, y)
        time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


if __name__ == '__main__':
    while True:
        mouse_click(500, 500)
        time.sleep(60)
