import signal
import sys
import tailhead
import time
import win32api, win32con

#oneshot
def left():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def right():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def middle():
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0)

#hold
def left_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
def right_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
def middle_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN,0,0)

#release
def left_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def right_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def middle_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP,0,0)

def handler(signum, frame):
    print("\nExiting wineclick")
    sys.exit(0)

print("Listening for events...")
for line in tailhead.follow_path('wineclick'):
    signal.signal(signal.SIGINT, handler)
    if line is not None:
        if line == "left":
            left()
            print("CLICK: left")
        if line == "right":
            right()
            print("CLICK: right")
        if line == "middle":
            middle()
            print("CLICK: middle")
        if line == "left_down":
            left_down()
            print("HOLD: left")
        if line == "right_down":
            right_down()
            print("HOLD: right")
        if line == "middle_down":
            middle_down()
            print("HOLD: middle")
        if line == "left_up":
            left_up()
            print("RELEASE: left")
        if line == "right_up":
            right_up()
            print("RELEASE: right")
        if line == "middle_up":
            middle_up()
            print("RELEASE: middle")
        if line == "exit":
            break
    else:
        time.sleep(.1)
