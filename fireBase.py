import pyrebase
import time
import json
import datetime
firebaseConfig = {
    "apiKey": "AIzaSyBAh2EGtDNhuOP9LF5jw0ViBPmWH71OaMo",
    "authDomain": "raspberry-face-recognition.firebaseapp.com",
    "databaseURL": "https://raspberry-face-recognition.firebaseio.com",
    "projectId": "raspberry-face-recognition",
    "storageBucket": "raspberry-face-recognition.appspot.com",
    "messagingSenderId": "469377065466",
    "appId": "1:469377065466:web:cfe2c3c3933e76c1958443",
    "measurementId": "G-WQVN4Q38MH"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()
path_on_cloud = "checkin/foo.jpg"
path_local = "images/frame.jpg"
def converttime(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def updateData(name):
    state = True
    path_image = storage.child('checkin/foo.jpg').get_url(None)
    storage.child(path_on_cloud).put(path_local)
    data = {}
    users = db.child("Checkout").get()
    num_list = []
    for user in users.each():
        num_list.append(user.val())
    # sort by name (Ascending order)
    num_list.sort(key=lambda x: x['time'], reverse=True)
    if num_list:
        for user in num_list:
            if user["name"] == name and user["checkout"] == False:
                state = False
                data = {"name": name, "time": json.dumps(datetime.datetime.now(), default=converttime), "url": path_image, "checkout": True, "checkin": user["time"]}
                break
            if user["name"] == name and user["checkout"] == True:
                state = True
                break
    if state:
        data = {"name": name, "time": json.dumps(datetime.datetime.now(), default=converttime), "url": path_image, "checkout": False}
    db.child("Checkout").push(data)
    print("uploaded successfully")
