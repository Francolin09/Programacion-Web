from django.http import HttpResponse
import datetime
from django.template import Template,Context
#request: para realizar peticiones
#httpresponse: para enviar la rspuesta usando el protocolo http


#Esto es una vista 
def bienvenida(request): #Se pasa un objeto de tipo request como argumento
    return HttpResponse("Bienvenido Don perkin")

def bienvenidaenrojo(request): #Se pasa un objeto de tipo request como argumento
    return HttpResponse("<p style= color:red;>Bienvenido Don perkin</p>")   

def categoriaEdad(request,edad):
    if edad >= 18:
        if edad >= 60:
            categoria="viejito"
        else: categoria="adulto" 
    else:
        if edad<10:
            categoria="mocoso"
        else:
            categoria="lolo"
    resultado="<h1>Categoria de la edad: %s </h1> " %categoria
    return HttpResponse(resultado)  

def obtenerMomento(request):
    respuesta="<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    return HttpResponse(respuesta)   

def obtenerMomentobonito(request):
    respuesta="<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request,nombre,edad):
    contenido = """
    <html>
    <body>
    <p> Nombre: %s <br> Edad: %s</p>
    </body>

    </html>


    """ %(nombre,edad) 

    return HttpResponse(contenido)  

def primeraplantilla(request):
    #Se abre el documento que contienen la plantilla html  
    plantillaExterna = open("C:/miproyecto1/miproyecto1/plantillas/primeraplantilla.html")
    #cargar el documento en una variable de tipo Template 
    template = Template(plantillaExterna.read()) #se debe importar Template
    plantillaExterna.close()
    #crear un contexto
    contexto= Context()  #se debe importar context 
    documento = template.render(contexto)
    return HttpResponse(documento)  


def plantillaParametros(request):
    nombre="Francolin"
    #Se abre el documento que contienen la plantilla html  
    plantillaExterna = open("C:/miproyecto1/miproyecto1/plantillas/plantillaparametros.html")
    #cargar el documento en una variable de tipo Template 
    template = Template(plantillaExterna.read()) #se debe importar Template
    plantillaExterna.close()
    #crear un contexto
    contexto= Context({"nombrecito": nombre})  #se le pasa el valor de nombre en forma de diccionario, es decir en la plantilla html se llamara haciendo referencia a nombrecito
    documento = template.render(contexto)
    return HttpResponse(documento)   


def plantillaListasBucles(request):
    nombre="Francolin"
    lenguajes =["python","Ruby","Javascript","Java","C#","Kotlin"]
    #Se abre el documento que contienen la plantilla html  
    plantillaExterna = open("C:\miproyecto1\miproyecto1\plantillas\plantillaListas.html")
    #cargar el documento en una variable de tipo Template 
    template = Template(plantillaExterna.read()) #se debe importar Template
    plantillaExterna.close()
    #crear un contexto
    contexto= Context({"nombrecito": nombre,"lenguajes ": lenguajes})  #se le pasa el valor de nombre en forma de diccionario, es decir en la plantilla html se llamara haciendo referencia a nombrecito
    documento = template.render(contexto)
    return HttpResponse(documento)         


