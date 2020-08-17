from directKey import LeftRelease, LeftClick
import time
from ScreenRecord import screen_record
import win32api


Auto = True  #If false Runs Color click, If True Runs Auto click

stop = 5  # IN MINUTES)
for x in range(4):
    print(x)
    time.sleep(1)

while time.perf_counter() < (stop*60)+4:

    if Auto:
        LeftClick()
        time.sleep(0.005)
        LeftRelease()
    else:
        (Mx, My) = win32api.GetCursorPos()
        done, pColor = screen_record(Mx, My, False)
        if done:
            break
        elif pColor == (75, 219, 106):  # Color for reaction time test 75,219,106
            LeftClick()
            LeftRelease()
