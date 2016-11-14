import urllib.request         
import sys
from datetime import datetime
from bs4 import BeautifulSoup

try:    
    response = urllib.request.urlopen("https://recursos-data.buenosaires.gob.ar/ckan2/ecobici/estado-ecobici.xml")
    html = response.read()        #Gets an array of bytes!
    strXML = html.decode()       #Convert to a string
except:
    print ('Error HTTP')
    sys.exit(0)

soup=BeautifulSoup(strXML)

print (soup.find('estacion').find('estacionid').text)

for message in soup.findAll('estacion'):
        f_estid = message.find('estacionid').text
        f_estnom = message.find('estacionnombre').text
        f_bicdisp = message.find('bicicletadisponibles').text
        f_estdisp = message.find('estaciondisponible').text
        f_num = message.find('numero').text
        f_lugar = message.find('lugar').text
        f_anclajetot = message.find('anclajestotales').text
        f_ancdisp = message.find('anclajesdisponibles').text
        print(f_estnom)
