import cv2
import time
import requests
import random
import json

start_time = time.time()

headers = {"Authorization": "Bearer ya29.A0ARrdaM-Z1fQmUbZpAacNFMKu3K1W4WNL7VE0DBKuSxNchWyOGIJCNDxVtFI8fMXs6GdYxGzZgYi_XjiqKMhzUiYI2LywB0dqmTm2wt4Mq4OPTP9rOHOwn_bJ45mhSuZ-zPV3iLFvhNXzyeLrEb1zlrz4wtDk"}

def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()
def upload_file(img):
    para = {
    "name": "My picture", #file name to be uploaded
    "parents": ["1F6ATb53H1pDZKh-N1wPBLO79wbEOlfMC"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': ('image/jpg',open(img, "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()