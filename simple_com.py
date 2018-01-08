import serial
import time

class arduinoCommunicator():
    def __init__(self, com="/dev/ttyUSB0", baud=9600, timeout=5):
        self.ser = serial.Serial(com, baud, timeout=timeout)
   
    def writeCom(self, text):
        self.ser.writelines("%s\n"%text)

    def readCom(self):
        self.ser.flushInput()
        text = self.ser.readline()
        return  text

    def blink(self):
        for i in range(5):
            self.ser.writelines("255\n")
            time.sleep(.5)
            self.ser.writelines("0\n")
            time.sleep(.5)


if __name__=="__main__":
    d = arduinoCommunicator()
#    d.blink()
    print "starting detector"
    while True:
        q = raw_input("write a number")
        if q == "quit":
            break
        else:
            d.writeCom(q)
        print d.readCom()


