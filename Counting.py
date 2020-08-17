import time, math
from directKey import PressKey, ReleaseKey


def identify(value):
    if value == 0:
        return zero

    elif value == 1:
        return one

    elif value == 2:
        return two

    elif value == 3:
        return three

    elif value == 4:
        return four

    elif value == 5:
        return five

    elif value == 6:
        return six

    elif value == 7:
        return sev

    elif value == 8:
        return eight

    elif value == 9:
        return nine


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

#buff = [zero, one, two, three, four, five, six, sev, eight, nine]

startVal = 0
endVal = 100
endVal += 1
diff = endVal - startVal

digits = [-1, -1, -1, -1, -1, -1, -1]  # [million, hundred thousand, ten thousand, thousand, hundred, ten, unit]
length = len(digits)

if startVal >= 1000000:  # million
    digits[6] = startVal % 10
    digits[5] = math.floor(startVal/10) % 10
    digits[4] = math.floor(startVal/100) % 10
    digits[3] = math.floor(startVal/1000) % 10
    digits[2] = math.floor(startVal/10000) % 10
    digits[1] = math.floor(startVal/100000) % 10
    digits[0] = math.floor(startVal/1000000) % 10

elif startVal >= 100000:
    digits[6] = startVal % 10
    digits[5] = math.floor(startVal/10) % 10
    digits[4] = math.floor(startVal/100) % 10
    digits[3] = math.floor(startVal/1000) % 10
    digits[2] = math.floor(startVal/10000) % 10
    digits[1] = math.floor(startVal/100000) % 10

elif startVal >= 10000:
    digits[6] = startVal % 10
    digits[5] = math.floor(startVal/10) % 10
    digits[4] = math.floor(startVal/100) % 10
    digits[3] = math.floor(startVal/1000) % 10
    digits[2] = math.floor(startVal/10000) % 10

elif startVal >= 1000:
    digits[6] = startVal % 10
    digits[5] = math.floor(startVal/10) % 10
    digits[4] = math.floor(startVal/100) % 10
    digits[3] = math.floor(startVal/1000) % 10

elif startVal >= 100:
    digits[6] = startVal % 10
    digits[5] = math.floor(startVal/10) % 10
    digits[4] = math.floor(startVal/100) % 10

elif startVal >= 10:
    digits[6] = startVal % 10
    digits[5] = math.floor(startVal/10) % 10

else:
    digits[6] = startVal


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

for j in range(diff):

    for k in range(length):

        if digits[6-k] != -1:

            if digits[6-k] > 9:

                if digits[6-k-1]+1 == 0:
                    digits[6-k-1] += 2

                else:
                    digits[6-k-1] += 1

                digits[6-k] = 0
    k = 0
    for k in range(length):

        if digits[k] != -1:

            PressKey(identify(digits[k]))
            #print(digits[k])
            time.sleep(0.003)
            ReleaseKey(identify(digits[k]))

    PressKey(Enter)
    time.sleep(0.003)
    ReleaseKey(Enter)

    digits[6] += 1

