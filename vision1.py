import cv2
import numpy as np


cv2.namedWindow( "result" )

cap = cv2.VideoCapture(0)
hsv_min = np.array((53, 55, 147), np.uint8)
hsv_max = np.array((83, 160, 255), np.uint8)

color_red = (0,0,255)

while True:
    flag, img = cap.read()
    img = cv2.flip(img,1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(img, (x, y), 5, color_red, 2)
        cv2.putText(img, "%d:%d" % (x,y-60), (x-60,y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color_red, 2)

    cv2.imshow('result', img)
 
    ch = cv2.waitKey(5)
    if ch == 27:
        break

cv2.destroyAllWindows()