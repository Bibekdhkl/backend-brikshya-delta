import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("/Users/arjun/Desktop/VERTEX_Dharan/project_main/app/services/firebase/credentials.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {"databaseURL": "https://esp8266-data-transfer-default-rtdb.firebaseio.com/"})

    # just creating a reference shortcut
ref = db.reference("/")

def get_sensor_data():

    # db.reference() is used to get the data returns string of the getting info.
    sensor_data = db.reference("/test").get()

    
    
    return sensor_data
