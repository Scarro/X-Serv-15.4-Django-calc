from django.conf.urls import url

from . import views

app_name = 'calc'
urlpatterns = [
	url(r'^(?P<numero1>\-?\d+)\+(?P<numero2>\-?\d+)$', views.suma, name="suma"),
	url(r'^(?P<numero1>\-?\d+)\-(?P<numero2>\-?\d+)$', views.resta, name="resta"),
	url(r'^(?P<numero1>\-?\d+)\*(?P<numero2>\-?\d+)$', views.multiplicacion, name="multiplicacion"),
	url(r'^(?P<numero1>\-?\d+)\/(?P<numero2>\-?\d+)$', views.division, name="division"),
]