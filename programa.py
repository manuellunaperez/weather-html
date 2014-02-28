#encoding=utf-8
import json
import os
import requests
from jinja2 import Template
import webbrowser
f = open('template.html','r')
web = open('web.html','w')


def direccion(orientacion):
	if (orientacion > 337.5 and orientacion <= 360) or (orientacion >= 0 and orientacion < 22.5):
		return 'N'
	if orientacion >= 22.5 and orientacion <= 67.5:
		return 'NE'
	if orientacion > 67.5 and orientacion < 112.5:
		return 'E'
	if orientacion >= 112.5 and orientacion <= 157.5:
		return 'SE'
	if orientacion > 157.5 and orientacion < 202.5:
		return 'S'
	if orientacion >= 202.5 and orientacion <= 245.5:
		return 'SO'
	if orientacion > 245.5 and orientacion < 292.5:
		return 'O'
	if orientacion >= 292.5 and orientacion <= 337.5:
		return 'NO'

print ''


html = ''
listaviento = []
listaorientacion = []
listatemp_min = []
listatemp_max = []
provincias = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']


for linea in f:
	html += linea

for provincia in provincias:
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':' %s ,spain' % provincia})
	dicc = json.loads(respuesta.text)
tempmax = int(dicc['main']['temp_max']-273.15)
tempmin = int(dicc['main']['temp_min']-272.15)
viento = int(dicc['wind']['speed']*1.609)
orienta = dicc["wind"]['deg']
orientacion = direccion(orienta)
listaorientacion.append(orientacion)
listatemp_min.append(tempmin)
listatemp_max.append(tempmax)
listaviento.append(viento)


template1 = Template(html)
template1 = template1.render(provincias=provincias,temp_min=listatemp_min,temp_max=listatemp_max,viento=listaviento,direccion=listaorientacion)
web.write(template1)

webbrowser.open('web.html')
