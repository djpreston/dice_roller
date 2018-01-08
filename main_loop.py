import serial #sudo pip install serial
import time
import cv2
import img_proc_fcn
from simple_com import arduinoCommunicator

if __name__=="__main__":
    d = arduinoCommunicator()
    result = img_proc_fcn.cap_and_proc()
    print result
#    d.blink()
    d.writeCom(255)
    time.sleep(1)
    d.writeCom(255)
    time.sleep(2)
    d.writeCom(0)
