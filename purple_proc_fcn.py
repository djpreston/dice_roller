import time
import cv2

def take_image():
    cam = cv2.VideoCapture(0)
    ret_val, img = cam.read()
    return img
#    cv2.imshow('my webcam', img)
#    time.sleep(5)
#    cv2.waitKey(1)
#    cv2.imwrite("background.png", img)

def cap_and_proc(main_i):
    background = cv2.imread("background.png",1)
#    cv2.imshow('subtracted image', background)
#    print background.shape
#    cv2.waitKey(0)
    background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    img = take_image()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_no_bg = cv2.subtract(img, background)
#    img_no_bg_inv = cv2.subtract(background, img)
#replaced    _,img_bin = cv2.threshold(img_no_bg,10,255,cv2.THRESH_BINARY)
    _,img_bin = cv2.threshold(img,215,255,cv2.THRESH_BINARY)
#    _,img_bin_inv = cv2.threshold(img_no_bg_inv,10,255,cv2.THRESH_BINARY)
#    img_bin = img_bin_inv
#    img_bin_inv = cv2.bitwise_not(img_bin_inv)
#    img_bin = cv2.bitwise_or(img_bin, img_bin_inv)
#    img_thresh = img_bin
#    cv2.imshow('name',img_no_bg_inv)
#    cv2.waitKey()
#    img_bin = cv2.floodFill(img_bin, (0,0), 1, (0,)*3, (0,)*3, flags=4|cv2.FLOODFILL_MASK_ONLY, mask=None)
    cv2.floodFill(img_bin, None, (0,0), 255)
    cv2.floodFill(img_bin, None, (630,0), 255)
    cv2.floodFill(img_bin, None, (630,450), 255)
    cv2.floodFill(img_bin, None, (0,450), 255)
#    print img_bin
    params = cv2.SimpleBlobDetector_Params()
    params.filterByInertia = True
    params.minInertiaRatio = 0.3

    cv_ver = (cv2.__version__).split('.')
    if int(cv_ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else :
        detector = cv2.SimpleBlobDetector_create(params)

    
    keypoints = detector.detect(img_bin)
#    print keypoints
    n_dice = len(keypoints)
#    print('You rolled %d'%n_dice)
#    print dir(keypoints)
#    cv2.imshow('subtracted image', img_bin)
    cv2.putText(img_bin,str(n_dice),(20,70),cv2.FONT_HERSHEY_SIMPLEX, 2, 0)
    cv2.imwrite("/home/gmw94193/dice_roller/proc_img/raw%d.png"%main_i, img_bin)
    cv2.imwrite("/home/gmw94193/dice_roller/raw_img/proc%d.png"%main_i, img)
    cv2.imshow('image', img_bin)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    return n_dice

def main():
#    print "main"
    result = cap_and_proc()
    time.sleep(1)
    print result

if __name__ == '__main__':
    main()


