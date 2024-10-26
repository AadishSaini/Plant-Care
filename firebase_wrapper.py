import pyrebase
import json

firebaseConfig = {
  'apiKey': "AIzaSyAVocimJN-xJOtpAVgrSVrFq2S4gDZ9qmQ",
  'authDomain': "plant-care-8fb4b.firebaseapp.com",
  'projectId': "plant-care-8fb4b",
  'storageBucket': "plant-care-8fb4b.appspot.com",
  'messagingSenderId': "1087848959003",
  'appId': "1:1087848959003:web:200a3609b0a34260f57cbe",
  'measurementId': "G-62E54GXB0W",
  "databaseURL": ""

}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login(email, passw):
    try:
        login = auth.sign_in_with_email_and_password(email, passw)
    except Exception as err:
        return [False, json.loads(err.strerror)['error']['message']]
    
    return [True, "Login successful"]


def signup(email, passw):
    try:
        user = auth.create_user_with_email_and_password(email, passw) 
    except Exception as err:
        return [False, json.loads(err.strerror)['error']['message']]
    return [True, "Signup successful"]



