from distutils import extension
from operator import not_
from os import close, remove, write
import os
import time  
from datetime import date, datetime, timedelta,timezone
import shutil 
from shutil import copy2, copytree
from shutil import copy
from shutil import move
import glob
from os import remove
import urllib.request
from PIL import Image

espacio="-------------"
now = datetime.now()
fecha1= time.strftime("%Y-%m-%d")
fecha2= time.strftime("%Y-%m-%d-%H%M")
print(fecha1)
print(fecha2)
print(espacio)
url1 = "https://www.wpc.ncep.noaa.gov/mike/gfs/crb_p24i_gfs00f024.gif"
file1 = "GFS24hrs.png"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()

espacio="-------------"
now = datetime.now()
fecha1= time.strftime("%Y-%m-%d")
fecha2= time.strftime("%Y-%m-%d-%H%M")
print(fecha1)
print(fecha2)
print(espacio)
url1 = "https://www.wpc.ncep.noaa.gov/mike/gfs/crb_p24i_gfs00f036.gif"
file1 = "GFS36hrs.png"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()

espacio="-------------"
now = datetime.now()
fecha1= time.strftime("%Y-%m-%d")
fecha2= time.strftime("%Y-%m-%d-%H%M")
print(fecha1)
print(fecha2)
print(espacio)
url1 = "https://www.wpc.ncep.noaa.gov/mike/gfs/crb_p24i_gfs00f048.gif"
file1 = "GFS48hrs.png"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()

espacio="-------------"
now = datetime.now()
fecha1= time.strftime("%Y-%m-%d")
fecha2= time.strftime("%Y-%m-%d-%H%M")
print(fecha1)
print(fecha2)
print(espacio)
url1 = "https://www.wpc.ncep.noaa.gov/mike/gfs/crb_p24i_gfs00f072.gif"
file1 = "GFS72hrs.png"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()

espacio="-------------"
now = datetime.now()
fecha1= time.strftime("%Y-%m-%d")
fecha2= time.strftime("%Y-%m-%d-%H%M")
print(fecha1)
print(fecha2)
print(espacio)
url1 = "https://www.wpc.ncep.noaa.gov/mike/gfs/crb_p24i_gfs00f084.gif"
file1 = "GFS84hrs.png"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()

espacio="-------------"
now = datetime.now()
fecha1= time.strftime("%Y-%m-%d")
fecha2= time.strftime("%Y-%m-%d-%H%M")
print(fecha1)
print(fecha2)
print(espacio)
url1 = "https://www.wpc.ncep.noaa.gov/mike/gfs/crb_p24i_gfs00f096.gif"
file1 = "GFS96hrs.png"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()

url2 = "http://capma.seneam.gob.mx/banco/MAPASUP.jpg"
file2 = "MAPASUP.png"
r = urllib.request.urlopen(url2)
f = open(file2,"wb")
f.write(r.read())
f.close()

url3 = "http://189.254.33.151/pron/modelo/pcp_pron_24hrs.png"
file3 = "fecha-SGIRPC-LLUVIA-24.png"
r = urllib.request.urlopen(url3)
f = open(file3,"wb")
f.write(r.read())
f.close()

espacio="-------------"
now = datetime.now()
fechaaire= time.strftime("%Y%m%d")
print(fechaaire)
print(espacio)
urlrain = "http://aire.cdmx.gob.mx/images/WRF/CDMX/"+fechaaire+"/rain_pronos_t_"+fechaaire+".gif"
print(urlrain)
url1 = urlrain
file1 = "AIRE-PRECIPITACION.gif"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()


print(espacio)
urltmp = "http://aire.cdmx.gob.mx/images/WRF/CDMX/"+fechaaire+"/t2m_pronos_t_"+fechaaire+".gif"
url1 = urltmp
file1 = "AIRE-TEMPERATURA.gif"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()

print(espacio)
urlwind = "http://aire.cdmx.gob.mx/images/WRF/CDMX/"+fechaaire+"/pronos_vientos_"+fechaaire+".gif"
url1 = urlwind
file1 = "AIRE-VIENTO.gif"
r = urllib.request.urlopen(url1)
f = open(file1,"wb")
f.write(r.read())
f.close()




dirMIKEOUT= r"C:\Users\videowall_03\Pictures\SGIRPC"
if not os.path.exists(dirMIKEOUT):
    os.makedirs(dirMIKEOUT)
    print("Directorio", dirMIKEOUT, "creado")

dirMIKEOUT= r"C:\Apache24\htdocs\imgpronos"
if not os.path.exists(dirMIKEOUT):
    os.makedirs(dirMIKEOUT)
    print("Directorio", dirMIKEOUT, "creado")


ImagenSGIRPC= Image.open(r"C:\Users\videowall_03\Pictures\fecha-SGIRPC-LLUVIA-24.png")
ImagenSGIRPC.save(r"C:\Users\videowall_03\Pictures\SGIRPC\fecha-SGIRPC-LLUVIA-24.png")


os.chdir(r"C:\Users\videowall_03\Pictures\SGIRPC")
print(os.getcwd())

for f in os.listdir():
    print(f)
    texto, extension = os.path.splitext(f)
    cambio1= texto.replace("fecha","{}".format(fecha2))
    print(cambio1)
    nuevo1 = f"{cambio1}{extension}"
    print(nuevo1)
    os.rename(f,nuevo1)

print(espacio)

ImagenSGIRPClluvia= Image.open(r"C:\Users\videowall_03\Pictures\fecha-SGIRPC-LLUVIA-24.png")
ImagenSGIRPClluvia.save(r"C:\Apache24\htdocs\imgpronos\SGIRPC-LLUVIA-24.png")

ImagenGFS24hrs= Image.open(r"C:\Users\videowall_03\Pictures\GFS24hrs.png")
ImagenGFS24hrs.save(r"C:\Apache24\htdocs\imgpronos\GFS24hrs.png")

ImagenGFS36hrs= Image.open(r"C:\Users\videowall_03\Pictures\GFS36hrs.png")
ImagenGFS36hrs.save(r"C:\Apache24\htdocs\imgpronos\GFS36hrs.png")

ImagenGFS48hrs= Image.open(r"C:\Users\videowall_03\Pictures\GFS48hrs.png")
ImagenGFS48hrs.save(r"C:\Apache24\htdocs\imgpronos\GFS48hrs.png")

ImagenGFS72hrs= Image.open(r"C:\Users\videowall_03\Pictures\GFS72hrs.png")
ImagenGFS72hrs.save(r"C:\Apache24\htdocs\imgpronos\GFS72hrs.png")

ImagenGFS84hrs= Image.open(r"C:\Users\videowall_03\Pictures\GFS84hrs.png")
ImagenGFS84hrs.save(r"C:\Apache24\htdocs\imgpronos\GFS84hrs.png")

ImagenGFS96hrs= Image.open(r"C:\Users\videowall_03\Pictures\GFS96hrs.png")
ImagenGFS96hrs.save(r"C:\Apache24\htdocs\imgpronos\GFS96hrs.png")

ImagenCAPMA= Image.open(r"C:\Users\videowall_03\Pictures\MAPASUP.png")
ImagenCAPMA.save(r"C:\Apache24\htdocs\imgpronos\MAPASUP.png")

ImagenAIRElluvia= Image.open(r"C:\Users\videowall_03\Pictures\AIRE-PRECIPITACION.gif")
ImagenAIRElluvia.save(r"C:\Apache24\htdocs\imgpronos\AIRE-PRECIPITACION.gif")

ImagenAIREtepm= Image.open(r"C:\Users\videowall_03\Pictures\AIRE-TEMPERATURA.gif")
ImagenAIREtepm.save(r"C:\Apache24\htdocs\imgpronos\AIRE-TEMPERATURA.gif")

ImagenAIREviento= Image.open(r"C:\Users\videowall_03\Pictures\AIRE-VIENTO.gif")
ImagenAIREviento.save(r"C:\Apache24\htdocs\imgpronos\AIRE-VIENTO.gif")