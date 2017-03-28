from django.conf.urls import url

from . import views

app_name = 'calc'
urlpatterns = [
    url(r'^$', views.calculadora, name="calculadora"),
    url(r'^(?P<operando1>-?[0-9]+)(?P<operacion>[\+\-\*\/])(?P<operando2>-?[0-9]+)$', views.operacion, name='sumar'),
]