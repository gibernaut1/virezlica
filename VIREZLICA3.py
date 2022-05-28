#программа ,которая на фотографии лица,вырезает их квадратиками и складывает вырезанные лица в отдельную папку
from selenium import webdriver#импортируем  из селениума вебдривер ,перед этим устновив вебдрайверекзешник для хрома(скачали из интернета)
import time
import cv2

FACE_DETECTOR_PATH='haarcascade_frontalface_default.xml'  #r'...\Library\etc\haarcascades\haarcascade_frontalface_default.xml'скачиваем хааркаскад для лица из опенсв
img = cv2.imread("780.jpg")#читаем файл
def crop_face(img, scaleFactor=1.001,
              face_detector_path=FACE_DETECTOR_PATH):
    face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#ПЕРЕВОДИМ картинку в серый цвет
    faces = face_cascade.detectMultiScale(gray, scaleFactor, 5)#находим лицо на серой фотографии
    for (x,y,w,h) in faces:
        #img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]#размер квадратика под лицо
        return roi_color
    
a=1.01
e=1
while a < 4:
      cropped = crop_face(img, scaleFactor=a)#перебираем 'a'-от него зависит как вырезается лицо( a может перебираться от 1.01 до 4) 
      cv2.imshow('1', cropped)#показывает вырезанное
      cv2.imwrite('d:\\image1\\' + str(e) + '.jpg', cropped)# присваивает вырезанным лицам номера
      a=a+0.01
      e=e+1
