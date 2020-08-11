import cv2
import numpy as np

print("tomek")

capture = cv2.VideoCapture('rtsp://admin:12345678-q@192.168.1.70:554')

print(type(capture))
while(True):
    ret, frame = capture.read()

    print("frame: {}".format(frame))
    print("ret: {}".format(ret))
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()