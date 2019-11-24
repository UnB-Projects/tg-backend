import numpy as np
from scipy import ndimage
import cv2 as cv2

import face_recognition

def YUVtoRGB(byteArray):

    byteArray = np.concatenate(byteArray, axis=0)

    e = 1280*720
    Y = byteArray[0:e]
    Y = np.reshape(Y, (720,1280))

    s = e
    V = byteArray[s::2]
    V = np.repeat(V, 2, 0)
    V = np.reshape(V, (360,1280))
    V = np.repeat(V, 2, 0)

    U = byteArray[s+1::2]
    U = np.repeat(U, 2, 0)
    U = np.reshape(U, (360,1280))
    U = np.repeat(U, 2, 0)

    RGBMatrix = (np.dstack([Y,U,V])).astype(np.uint8)
    RGBMatrix = cv2.cvtColor(RGBMatrix, cv2.COLOR_YUV2RGB, 3)

    return RGBMatrix

def process_faces(image):
    igor_image = face_recognition.load_image_file("igor.jpg")
    igor_face_encoding = face_recognition.face_encodings(igor_image)[0]

    known_face_encodings = [
        igor_image,
    ]
    known_face_names = [
        "Igor",
    ]
    results = face_recognition.compare_faces([igor_image], image)

    if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")