import cv2
import numpy as np
from pyzbar.pyzbar import decode


def decoder(image):
    img = cv2.cvtColor(image, 0)
    barcode = decode(img)

    for puzzel in barcode:
        points = puzzel.polygon
        (x, y, width, hight) = puzzel.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 0, 255), 3)

        myData = puzzel.data.decode("utf-8")
        barcodeType =puzzel.type
        string = "Data " + str( myData ) + " | Type " + str(barcodeType)

        cv2.putText(frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        print("Barcode: " +  myData  + " | Type: " + barcodeType)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Image', frame)
    code = cv2.waitKey(1)
    if code == ord('q'):
        break
