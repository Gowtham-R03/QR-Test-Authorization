import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('E1.jpg')
# code = decode(img)
# print(code)
cap = cv2.VideoCapture(0)

while True:

    sucess, img = cap.read()

    for barcode in decode(img):
        # print(barcode.data)  #data in bits 'b
        myData = barcode.data.decode('utf-8')  #converting our data into string
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)

    cv2.imshow("QrCodeResult",img)
    cv2.waitKey(1)
