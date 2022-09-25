#from email.mime import application
#from pickle import NONE
#from ssl import ALERT_DESCRIPTION_USER_CANCELLED, AlertDescription
#from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Paciente
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Importaciones para impresión pdf: XHTML2PDF
import os
#from django.conf import settings

from django.template.loader import get_template
from weasyprint import HTML, CSS
from pacientes import settings

#from django.contrib.staticfiles import finders


# Create your views here.

def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def publicaciones(request):
    return render(request,'paginas/publicaciones.html')



def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pacientes')
    return render(request,'pacientes/crear.html', {'formulario': formulario})

def editar(request,id):
    editarPaciente = Paciente.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=editarPaciente)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('pacientes')
    return render(request,'pacientes/editar.html',{'formulario': formulario})

def eliminar(request, id):
    eliminarpaciente = Paciente.objects.get(id=id) 
    
    eliminarpaciente.delete()
    return redirect('pacientes')

@login_required

def pacientes(request):
    datospacientes = Paciente.objects.all().order_by('habitacion','cama')
    return render(request,'pacientes/index.html', {'pacientes1': datospacientes})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

def imprimirpdf(request, *args, **kwargs):

    try:
    
        
        template = get_template('pacientes/pdfreporte.html')
        

        context = {
        'name_nutri':'María Carla Lázaro',
        #'fecha': datetime.datetime.now(),
        'pacientes': Paciente.objects.all().order_by('habitacion','cama')
        }
        
        html = template.render(context)

        css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.4.1-dist/css/bootstrap.min.css')
        pdf = HTML(string = html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])

        return HttpResponse(pdf, content_type='application/pdf')
    
    except:
        print('parece que hay un error')

    return redirect('/')
    
