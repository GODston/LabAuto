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


class Interview(object):
    def __init__(self, id, alias, fechaCreacion, fechaActualizacion, preguntas):
        self.id=id
        self.alias=alias
        self.preguntas=preguntas
        self.fechaCreacion=fechaCreacion
        self.fechaActualizacion=fechaActualizacion

class Person(object):
    def __init__(self, id, nombre, puesto, edad, fechaRegistro, fechaEntrevista):
        self.id=id
        self.nombre=nombre
        self.puesto=puesto
        self.edad=edad
        self.fechaRegistro=fechaRegistro
        self.fechaEntrevista=fechaEntrevista

listPersons = [
    Person('1', 'Juan Pablo Almaguer', 'Analista Programador Jr.', '33', '2021-02-24', '2021-03-12'),
    Person('2', 'Alejandro Fernandez Martinez', 'Marketing Jr.', '40', '2021-02-24', '2021-03-12'),
    Person('3', 'Gerardo Daniel Cruz', 'Analista Programador Sr.', '45', '2021-02-24', '2021-03-12'),
    Person('4', 'Esteban Alejandro Gomez', 'Marketing Jr.', '34', '2021-02-24', '2021-03-12'),
    Person('5', 'Antonio Raul Garcia', 'Analista Programador Jr.', '29', '2021-02-24', '2021-03-12'),
    Person('6', 'Adrian Favela Lozano', 'Analista Programador Jr.', '25', '2021-02-24', '2021-03-12'),
    Person('7', 'Guillermo Garza', 'Analista Programador Sr.', '30', '2021-02-24', '2021-03-12'),
]

listInterviews = [
    Interview('1', 'Entrevista Analista Jr.', '2020-04-29', '2021-03-23', 30),
    Interview('2', 'Entrevista Analista Semi-Sr.', '2020-04-29', '2021-03-23', 30),
    Interview('3', 'Entrevista Analista Sr.', '2020-04-29', '2021-03-23', 30),
    Interview('4', 'Entrevista Marketing Jr.', '2020-04-29', '2021-03-23', 30),
    Interview('5', 'Entrevista Marketing Sr.', '2020-04-29', '2021-03-23', 30),
    Interview('6', 'Entrevista Project Manager', '2020-04-29', '2021-03-23', 30),
    Interview('7', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30),
    Interview('8', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30),
    Interview('9', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30),
    Interview('10', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30)
]

def index(request):
    name_Emp = database.child('Empresa').child('1').child('nombre_Emp').get().val()

    return render(request, 'index.html', {
        "name_Emp": name_Emp
    })

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def interviews(request):
    return render(request, 'Components/Brand/interviews.html', {
        "empresa": True,
        "listInterviews": listInterviews
    })

def candidates(request):
    return render(request, 'Components/Brand/candidates.html', {
        "empresa": True,
        "listPersons": listPersons
    })

def settings(request):
    return render(request, 'Components/Brand/settings.html', {
        "empresa": True
    })