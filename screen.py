import mss
import time
import pytesseract
import cv2
import numpy as np
import os


sct = mss.mss()

monitor = sct.monitors[1]

OCR_INTERVAL = 1.5
last_ocr_time = 0


while True:
    frame = np.array(sct.grab(monitor))

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow("Live Screen (S to save, ESC to escape)", frame)

    if time.time() - last_ocr_time > OCR_INTERVAL:
        last_ocr_time = time.time()
        text = pytesseract.image_to_string(frame)
        if text.strip():
            print("\n[Detected Text]")
            print(text.strip())
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows