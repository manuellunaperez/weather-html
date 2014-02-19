#encoding=utf-8
import requests
import json
provincias = ['','Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']
print '1. Almería\n2. Cádiz\n3. Córdoba\n4. Granada\n5. Huelva\n6. Jaén\n7. Málaga\n8. Sevilla'

peticion = int(raw_input("¿De qué ciudad quieres saber la temperatura actual? "))

provincia = '%s' % provincias[peticion]

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':' %s ,spain' % provincia})


dicc = json.loads(respuesta.text)
temperatura = dicc['main']['temp']

print 'La temperatura actual de %s es %s grados centígrados' % (provincias[peticion],temperatura-272.15)
