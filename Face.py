import cv2
import sys
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)
img_counter = 1

while True:
    ret, frame = video_capture.read()
    k = cv2.waitKey(1)
    faces = faceCascade.detectMultiScale(
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
        scaleFactor = 1.5,
        minNeighbors = 5 ,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Camera Oficial Davi Lucas',frame)
    if k % 256 == 27:
        break
    elif k % 256 == 32:
        img_name = f"Imagem da Camera_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} foi salvo em seu atual diretório")
        img_counter += 1
video_capture.release()
cv2.destroyAllWindows()