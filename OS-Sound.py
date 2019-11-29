import os
import win32api, win32con, win32gui
import time

os.system('{0}\\System32\\control.exe mmsys.cpl'.format(
    os.environ['WINDIR'],))

time.sleep(1)
SoundWindow = win32gui.GetForegroundWindow()
win32gui.MoveWindow(SoundWindow, 400, 250, 410, 460, 1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y)

def click1(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)


click(490, 540)  # simulate right click at 490, 540 pixels
click1(510, 600) # simulate mouse click at 510, 600 pixels 

time.sleep(.5)
win32gui.PostMessage(SoundWindow, win32con.WM_CLOSE, 0, 0)