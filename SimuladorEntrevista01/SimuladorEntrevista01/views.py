from django.shortcuts import render
from .models import Entrevista
from .models import Pregunta
from .models import Persona
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
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

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

def act_login(request):
    status_login = ""
    cont = 1

    usr = request.POST.get("txtEmail")
    pss = request.POST.get("txtPassword")
    status_login = "Inicio de Sesion incorrecto"
    dbemp = database.child("Empresa").get()
    for emp in dbemp.each():
        if emp.key() >= 1:
            if usr == database.child("Empresa").child(emp.key()).child("correo").get().val():
                if pss == database.child("Empresa").child(emp.key()).child("contrasena").get().val() and database.child("Empresa").child(emp.key()).child("estatus").get().val() == "1":
                    #código de inicio de sesion-->
                    status_login = "Inicio de Sesion Correcto!"
                    return render(request, 'login.html', {
                        "status_login": status_login
                    })
    #código de error de inicio de sesion -->
    return render(request, 'login.html', {
        "status_login": status_login
    })

def act_register(request):
    #Carga de datos
    status_register = "Error en registro"
    name = request.POST.get("txtNameEmp")
    usr = request.POST.get("txtEmail")
    pss = request.POST.get("txtPassword")
    pssConf = request.POST.get("txtCPassword")
    dbemp = database.child("Empresa").get()
    """
    #Validar campos
    if len(pss) < 1 or len(name) < 1 or len(usr) < 1:
        status_register = "Favor de llenar todos los campos correctamente."
        return render(request, 'register.html', {
            "status_register": status_register
        })
    if len(pss) < 5:
        status_register = "La contraseña debe contener al menos 5 caracteres."
        return render(request, 'register.html', {
            "status_register": status_register
        })
    if pss != pssConf:
        status_register = "Ambas contraseñas deben coincidir."
        return render(request, 'register.html', {
            "status_register": status_register
        })

    #Validar que no esta el correo registrado aun
    
    for emp in dbemp.each():
        if emp.key() >= 1:
            if database.child("Empresa").child(emp.key()).child("correo").get().val() == usr:
                status_register = "Ya esta registrado ese correo, intente con otro."
                return render(request, 'register.html', {
                    "status_register": status_register
                })
    """
    #Agregar los datos
    cont = 1
    for emp in dbemp.each():
        if emp.key() >= 1:
            if database.child("Empresa").child(emp.key()).child("id_Emp").get().val() != str(cont):
                #Se incertan datos en id = str(cont)
                """
                database.child("Empresa").child(str(cont)).child("id_Emp").set(str(cont))
                database.child("Empresa").child(str(cont)).child("estatus").set("1")
                database.child("Empresa").child(str(cont)).child("nombre_Emp").set(name)
                database.child("Empresa").child(str(cont)).child("correo").set(usr)
                database.child("Empresa").child(str(cont)).child("contrasena").set(pss)
                """
                status_register = "Registro de Empresa exitosa en id = " + str(cont)
                return render(request, 'register.html', {
                    "status_register": status_register
                })
            else:
                cont = cont + 1
    #Se incertan datos en id = str(cont)
    """
    database.child("Empresa").child(str(cont)).child("id_Emp").set(str(cont))
    database.child("Empresa").child(str(cont)).child("estatus").set("1")
    database.child("Empresa").child(str(cont)).child("nombre_Emp").set(name)
    database.child("Empresa").child(str(cont)).child("correo").set(usr)
    database.child("Empresa").child(str(cont)).child("contrasena").set(pss)
    """
    status_register = "Registro de Empresa exitosa en id = " + str(cont)
    #Error
    return render(request, 'register.html', {
        "status_register": status_register
    })