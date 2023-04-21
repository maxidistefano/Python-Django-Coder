from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("hola Django- Coder")

def probandoTemplate(request):
    miHtml = open("C:/cursos/DjangoPython/Proyecto1/plantillas/template.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1
                                        #OJO importar TEMPLATE y CONTEXT, con: from django.template import Template, Context
    miHtml.close()      #Cerramos el archivo

    miContexto = Context()  #En este caso no hay nada ya que no hay parametros, pero igual hay que crearlo
    
    documento = plantilla.render(miContexto)    #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)