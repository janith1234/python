import requests
import json
headers = {"Authorization": "Bearer ya29.A0ARrdaM9emAQ4_zVTB03T7LbPWw6w6H6GkwmARqDeMYJvjmh2fQkl8gond0uKBKgbA3pLYk2lKUxONr22GRJWu5i_1TdTssjrrnPkPVmDXu82bYObm4hhhnIIgYSOuZmE4B7Y-tQanUZ9tjwc-pm0vpafqZhX"} #put ur access token after the word 'Bearer '
para = {
    "name": "My picture", #file name to be uploaded
    "parents": ["1F6ATb53H1pDZKh-N1wPBLO79wbEOlfMC"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('image/jpg',open("pic.jpg", "rb")) # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
