import mss
import cv2
import os
import pytesseract
import numpy as np
import time
import keyboard

sct = mss.mss()
monitor = sct.monitors[1]
screenshot_count = 0

# save_dir = os.path.join(os.getcwd(), "screenshots")
os.makedirs("screenshots", exist_ok=True)

while True:
    frame = np.array(sct.grab(monitor))
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow("Live Screen (S to save, ESC to exit)", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27: 
        break
    #Saves screenshot to file
    if key == ord('s'): 
        screenshot_count += 1
        filename1 = f"screenshots/screenshot_{screenshot_count}_{int(time.time())}.png"
        cv2.imwrite(filename1, frame)
        print(cv2.imwrite(filename1, frame))
        print(f"screenshot saved {filename1}")

cv2.destroyAllWindows()