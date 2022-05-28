FACE_DETECTOR_PATH=r'...\Library\etc\haarcascades\haarcascade_frontalface_default.xml'

def crop_face(img, scaleFactor=1.001,
              face_detector_path=FACE_DETECTOR_PATH):
    face_cascade = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor, 5)
    for (x,y,w,h) in faces:
        #img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        return roi_color

cropped = crop_face(img, scaleFactor=1.01)
cv2.imshow('1', cropped)

cv2.imwrite(r'с:/temp/res.png', cropped)
