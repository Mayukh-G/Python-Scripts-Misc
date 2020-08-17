#auto mine cobblestone

import time
from directKey import LeftRelease, LeftClick

for i in list(range(5))[::-1]:
    print(i+1)
    time.sleep(1)

while True:

    time.sleep(2)
    LeftClick()
    time.sleep(1)
    LeftRelease()

