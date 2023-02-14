import time
import numpy as np
import mss
import cv2 as cv
import mouse


def draw():
    cv.imshow('Wind', screen)
    if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            return False
    return True

sct = mss.mss()


ball_img = cv.imread(f'ball_1.png')
ball = cv.cvtColor(ball_img, cv.COLOR_BGR2GRAY)


monitor = {'top': 110, 'left': 132, 'width': 40, 'height': 450}

counter = 0


while True:
    screen = cv.cvtColor(np.array(sct.grab(monitor)), cv.COLOR_BGR2GRAY)

    result = cv.matchTemplate(ball, screen, cv.TM_CCOEFF).max()

    if result > 2_500_000:
        mouse.click()

        time.sleep(0.3)
        print(counter, 'BALL!', result)
        counter += 1

    
    if not draw():
        break
