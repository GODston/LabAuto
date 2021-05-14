from django.shortcuts import render
from apps.entrevista.models import Entrevista
from apps.entrevista.models import Pregunta
from apps.persona.models import Persona
from django.contrib.auth.forms import UserCreationForm
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

listaPersonas = [
    Persona('1', 'Juan Pablo Almaguer', 'Analista Programador Jr.', '33', '2021-02-24', '2021-03-12'),
    Persona('2', 'Alejandro Fernandez Martinez', 'Marketing Jr.', '40', '2021-02-24', '2021-03-12'),
    Persona('3', 'Gerardo Daniel Cruz', 'Analista Programador Sr.', '45', '2021-02-24', '2021-03-12'),
    Persona('4', 'Esteban Alejandro Gomez', 'Marketing Jr.', '34', '2021-02-24', '2021-03-12'),
    Persona('5', 'Antonio Raul Garcia', 'Analista Programador Jr.', '29', '2021-02-24', '2021-03-12'),
    Persona('6', 'Adrian Favela Lozano', 'Analista Programador Jr.', '25', '2021-02-24', '2021-03-12'),
    Persona('7', 'Guillermo Garza', 'Analista Programador Sr.', '30', '2021-02-24', '2021-03-12'),
]

listaEntrevistas = [
    Entrevista('1', 'Entrevista Analista Jr.', '2020-04-29', '2021-03-23', 30),
    Entrevista('2', 'Entrevista Analista Semi-Sr.', '2020-04-29', '2021-03-23', 30),
    Entrevista('3', 'Entrevista Analista Sr.', '2020-04-29', '2021-03-23', 30),
    Entrevista('4', 'Entrevista Marketing Jr.', '2020-04-29', '2021-03-23', 30),
    Entrevista('5', 'Entrevista Marketing Sr.', '2020-04-29', '2021-03-23', 30),
    Entrevista('6', 'Entrevista Project Manager', '2020-04-29', '2021-03-23', 30),
    Entrevista('7', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30),
    Entrevista('8', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30),
    Entrevista('9', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30),
    Entrevista('10', 'Entrevista Scrum Master', '2020-04-29', '2021-03-23', 30)
]

listaPreguntas = [
    Pregunta('1', 'Que te gusta hacer?'),
    Pregunta('2', 'Cuales son tus aspiraciones?'),
    Pregunta('3', 'Como comenzaste en la carrera?'),
    Pregunta('4', 'Cual es tu motivacion?'),
    Pregunta('5', 'Que es lo que buscas en un ambiente de trabajo?'),
    Pregunta('6', 'Que te gusta hacer?'),
    Pregunta('7', 'Cuales son tus aspiraciones?'),
    Pregunta('8', 'Como comenzaste en la carrera?'),
    Pregunta('9', 'Cual es tu motivacion?'),
    Pregunta('10', 'Que es lo que buscas en un ambiente de trabajo?'),
    Pregunta('11', 'Que te gusta hacer?'),
    Pregunta('12', 'Cuales son tus aspiraciones?'),
    Pregunta('13', 'Como comenzaste en la carrera?'),
    Pregunta('14', 'Cual es tu motivacion?'),
    Pregunta('15', 'Que es lo que buscas en un ambiente de trabajo?')
]

def index(request):
    #ejemplo de como consultar un dato en firebase:
    name_Emp = database.child('Empresa').child('1').child('nombre_Emp').get().val()

    #ejemplo enviar dato de firebase a una vista .html
    return render(request, 'index.html', {
        "name_Emp": name_Emp
    })

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def interviews(request):
    return render(request, 'Brand/interviews.html', {
        "empresa": True,
        "listaEntrevistas": listaEntrevistas
    })

def interview_details(request, id):
    return render(request, 'Brand/interview_details.html', {
        "empresa": True,
        "entrevista": listaEntrevistas[id-1],
        "listaPreguntas": listaPreguntas
    })

def candidates(request):
    return render(request, 'Brand/candidates.html', {
        "empresa": True,
        "listaPersonas": listaPersonas
    })

def candidate_details(request, id):
    return render(request, 'Brand/candidate_details.html', {
        "empresa": True,
        "candidato": listaPersonas[id-1]
    })

def settings(request):
    return render(request, 'Brand/settings.html', {
        "empresa": True
    })