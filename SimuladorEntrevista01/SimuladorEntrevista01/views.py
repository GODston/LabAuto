from django.shortcuts import render
import pyrebase

config = {
    "apiKey": "AIzaSyDxM45BMn7cGoQVR-brcPQ_xPLB8VCjXHU",
    "authDomain": "lb-auto.firebaseapp.com",
    "databaseURL": "https://lb-auto-default-rtdb.firebaseio.com",
    "projectId": "lb-auto",
    "storageBucket": "lb-auto.appspot.com",
    "messagingSenderId": "956958028386",
    "appId": "1:956958028386:web:d670731536884ca618173b"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def index(request):
    #ejemplo de como consultar un dato en firebase:
    name_Emp = database.child('Empresa').child('1').child('nombre_Emp').get().val()

    #ejemplo enviar dato de firebase a una vista .html
    return render(request, 'index.html', {
        "name_Emp": name_Emp
    })