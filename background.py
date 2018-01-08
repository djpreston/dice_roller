import time
import cv2

def take_background():
    cam = cv2.VideoCapture(0)
    ret_val, img = cam.read()
    cv2.imshow('my webcam', img)
#    time.sleep(5)
    cv2.waitKey(0)
    cv2.imwrite("background.png", img)

def main():
    take_background()

if __name__ == '__main__':
    main()


