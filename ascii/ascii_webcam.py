import cv2
import numpy as np
import threading
from numba import jit

@jit(nopython=True)
def to_ascii_art(frame, images, box_height=12, box_width=16):
    height, width = frame.shape
    for i in range(0, height, box_height):
        for j in range(0, width, box_width):
            roi = frame[i:i + box_height, j:j + box_width]
            best_match = np.inf
            best_match_index = 0
            for k in range(1, images.shape[0]):
                total_sum = np.sum(np.absolute(np.subtract(roi, images[k])))
                if total_sum < best_match:
                    best_match = total_sum
                    best_match_index = k
            roi[:,:] = images[best_match_index]
    return frame

def generate_ascii_letters():
    images = []
    chars = " \\ '(),-./:;[]_`{|}~"
    #chars = ".,-~:;=!*#$@" Optional
    for char in chars:
        img = np.zeros((12, 16), np.uint8)
        img = cv2.putText(img, char, (0, 11), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255)
        images.append(img)
    return np.stack(images)

cap = cv2.VideoCapture(1) # Change the paramter to switch cameras
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 0.1)
images = generate_ascii_letters()

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gb = cv2.GaussianBlur(frame, (5, 5), 0)
    can = cv2.Canny(gb, 127, 31)
    ascii_art = to_ascii_art(can, images)
    cv2.imshow('ASCII ART', ascii_art)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        break

t = threading.Thread(target=cap, daemon=True)
t.start()
t1 = threading.Thread(target=to_ascii_art, daemon=True)
t1.start()
t2 = threading.Thread(target=generate_ascii_letters, daemon=True)
t2.start()

cap.release()
cv2.destroyAllWindows()

