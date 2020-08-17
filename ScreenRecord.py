import numpy as np
from PIL import ImageGrab, ImageColor
import cv2
import time
import uuid

def process_img(original_image) : #process image

    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=400, threshold2=200)
    return processed_img


def pixel_color(sc, x, y):  #testcolor

    return sc.load()[x, y]

def screen_record(colorPosX, colorPosY, show):
    last_time = time.time()

    screen = ImageGrab.grab(bbox=None)
    pColor = pixel_color(screen, colorPosX, colorPosY)
    screen = np.array(screen) #grab screen  OG 0,40,850,510   for dmg 770,70,780,80
    new_screen = process_img(screen)

    # SHOW FRAME RATE
    # print('{}fps'.format(1/(time.time() - last_time)))
    last_time = time.time()

    if show:
        cv2.imshow('window', new_screen) #show screen
    if cv2.waitKey(25) & 0xFF == ord('q'): # this key will stop the caps
        cv2.destroyAllWindows()
        return True, pColor
    else:
        return False, pColor



