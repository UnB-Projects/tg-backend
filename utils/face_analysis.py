import numpy as np
from scipy import ndimage
import cv2 as cv2
import os

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

def process_faces(rec_image):
    known_face_encodings = []

    known_face_names = []
    nomeFotos = os.listdir("./media/fotos")
    # rec_image = face_recognition.load_image_file(rec_image)
    rec_enconding = face_recognition.face_encodings(rec_image)[0]
    for nome in nomeFotos:
        image = face_recognition.load_image_file("./media/fotos/" + nome)
        image_enconding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(image_enconding)
        known_face_names.append(nome)

    matches = face_recognition.compare_faces(known_face_encodings, rec_enconding)
    name = "Unknown"
    face_distances = face_recognition.face_distance(known_face_encodings, rec_enconding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]



    print(name)