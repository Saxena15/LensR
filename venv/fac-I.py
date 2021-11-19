# training data

import cv2
import numpy as np



cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
#
# skip = 0
# face_data = []
# dataset_path = './data'
# file_name = input('Enter name of person:')
while True:
    ret, frame =cap.read()
    if ret == False:
        continue
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    # if len(faces) == 0:
    #     continue

    # faces = sorted(faces, key=lambda f: f[2]*f[3])
    # if len(faces) == 0:
    #     continue

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 0, 230), 2)

        offset = 20
        face_section = frame[y - offset:y + h + offset, x - offset:x + w + offset]
        face_section = cv2.resize(face_section, (100, 100))


    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
#
# face_data = np.asarray(face_data)
# np.save(dataset_path+file_name+'.npy', face_data)
# print(face_data.shape)
# np.save(dataset_path+file_name+'.npy',face_data)
# print("Data Successfully save at "+dataset_path+file_name+'.npy')
#


cap.release()
cv2.destroyAllWindows()

