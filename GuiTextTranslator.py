import time
import cv2
import numpy as np
from mss import mss

start_time = time.time()
mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
with mss() as sct:
    while True:
        last_time = time.time()
        img = sct.grab(mon)
        print('The loop took: {0}'.format(time.time()-last_time))
        cv2.imshow('test', np.array(img))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

# # The simplest use, save a screen shot of the 1st monitor
# with mss() as sct:
#     sct.shot()


# SOME OTHER FUNCTION TO FIND TEXT WINDOW