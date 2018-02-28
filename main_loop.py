import serial #sudo pip install serial
import time
import cv2
import img_proc_fcn
from simple_com import arduinoCommunicator

if __name__=="__main__":
  data = [0,0,0,0,0,0]
  for i in range(4):
    d = arduinoCommunicator()
#    d.blink()
    d.writeCom(255)
    time.sleep(2)
    d.writeCom(0)
    time.sleep(0)
    d.writeCom(0)
    time.sleep(0)
    d.writeCom(0)
    time.sleep(4)
    result = img_proc_fcn.cap_and_proc(i)
    print result
    if ((result >= 1) and (result <= 6)):
      data[result-1] = data[result-1]+1
    print data
  print data

