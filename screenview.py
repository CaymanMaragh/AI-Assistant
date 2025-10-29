import cv2
import os
import mss
import numpy as np
import time
import pytesseract

sct = mss.mss()
monitor = sct.monitors[1]


def start_screen_share():
    frame = np.array(sct.grab(monitor))
    # cv2.imshow("Live Screen", frame)

def take_screenshot():
    os.makedirs("screenshots", exist_ok=True)
    screenshot_count = 0
    frame = np.array(sct.grab(monitor))
    screenshot_count += 1
    filename = f"screenshots/screenshot_{screenshot_count}_{int(time.time())}.png"
    print("CWD:", os.getcwd())
    print("abs target:", os.path.abspath(filename))
    cv2.imwrite(filename, frame)
    print(f"screenshot saved {filename}")
