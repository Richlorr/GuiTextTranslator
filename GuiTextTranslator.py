import time
import cv2
import numpy as np
from mss import mss

times_arr = np.zeros(shape=(10,1))
i = 0

start_time = time.time()
mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
with mss() as sct:
    while True:
        last_time = time.time()
        img = sct.grab(mon)
        curr_time = time.time()
        print('The loop took: {0}'.format(time.time()-last_time))
        cv2.imshow('test', np.array(img))
        try:
            times_arr.append(curr_time)
        except:
            print(times_arr)
            cv2.destroyAllWindows()
            break
        if cv2.waitKey(25) & 0xFF == ord('q') or i>=10000:
            print(times_arr)
            cv2.destroyAllWindows()
            break
print(times_arr)

# # The simplest use, save a screen shot of the 1st monitor
# with mss() as sct:
#     sct.shot()


# SOME OTHER FUNCTION TO FIND TEXT WINDOW