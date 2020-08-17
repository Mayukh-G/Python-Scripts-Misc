# This is my attempt at writing a code that plays a game
import time
from directKey import PressKey, ReleaseKey, RightClick, RightRelease, LeftClick, LeftRelease

# _________________ Meat ____________________ #

W = 0x57
A = 0x41
S = 0x53
D = 0x44
Space = 0x20
Shift = 0x10
Enter = 0x0D

zero = 0x30
one = 0x31
two = 0x32
three = 0x33
four = 0x34
five = 0x35
six = 0x36
sev = 0x37
eight = 0x38
nine = 0x39

buff = [zero,one,two,three,four,five,six,sev,eight,nine]


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

# time.sleep(1) Russian mafia
# PressKey(S)
# LeftClick()
# time.sleep(0.1)
# ReleaseKey(S)
# LeftRelease()
#
# time.sleep(0.22)

# PressKey(Space)
# ReleaseKey(Space)
# time.sleep(0.05)
# PressKey(D)
# PressKey(Shift)
# time.sleep(0.05)
# RightClick()
# RightRelease()
# ReleaseKey(D)
# ReleaseKey(Shift)
#
# time.sleep(0.68)
#
# PressKey(A)
# ReleaseKey(A)
# PressKey(S)
# time.sleep(0.05)
# LeftClick()
# LeftRelease()
# ReleaseKey(S)
