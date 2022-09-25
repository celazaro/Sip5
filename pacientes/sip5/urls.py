from django.urls import path

from pacientes.settings import MEDIA_ROOT
from.import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('publicaciones', views.publicaciones, name='publicaciones'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('pacientes/crear', views.crear, name='crear'),
    path('pacientes/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('cerrar_sesion',views.cerrar_sesion, name='cerrar_sesion'),
    path('imprimirpdf',views.imprimirpdf, name='imprimirpdf'),
    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)