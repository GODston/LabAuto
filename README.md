# Auto Interview Analyzer

Consiste en una herramienta de software que permite realizar filtros a los candidatos que desean postularse para aplicar a alguna vacante de alguna empresa, permitiendo que la plataforma realice preguntas preliminares para descargar posibles candidatos que no cumplen con conocimientos minimos o no muestran cierto grado de confianza.

# Comenzando

Para este proyecto se necesito instalar complementos o plugins para python

## Plugins necesarios

_Django_

```
python install -m Django
```

En caso de error se puede intentar con este otro comando
```
pip3 install Django
```
#

_Pyrebase_

```
python install -m pyrebase
```

En caso de error se puede intentar con este otro comando

```
pip3 install pyrebase4
```
#

_Bootstrap 4_

```
pip install django-bootstrap4
```

_Crispy Forms
```
pip install -r requirements.txt
```

## Ejecutar la aplicacion
Para ejecutar la aplicacion basta correr el siguiente comando:

```
python manage.py runserver
```

## Crear modelos de bases de datos

Para crear los modelos de cada una de las apps en la base de datos, es necesario ejecutar los siguientes comandos:

### Para crear las migraciones de dichos modelos:

```
python manage.py makemigrations
```

### Para establecer los modelos como tablas en la base de datos

```
python manage.py migrate
```