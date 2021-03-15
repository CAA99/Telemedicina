#import ipapi
from requests import get
import json
import webbrowser

def ubicacion():
    
    localizacion = get('http://ip-api.com/json/') # api para conseguir la localizacion del dispositivo
    datos = localizacion.json() # Guardamos los datos arrojados por la API en la variable datos
    
    with open('datos.json', 'w') as archivo:  #Crea y guarda el archivo con la informatcion en fortmato JSON
        json.dump(datos, archivo)
        #print('realizado')
    
    #Guardamos los datos del diccionario que quermos utilizar en variables
    ip = datos['query']
    pais = datos['country']
    departamento = datos['regionName']
    ciudad = datos['city']
    codPostal = datos['zip']
    print(f"su direccion ip es {ip} se encuentra ubicada en {pais} en el departamento de {departamento} en la ciudad de {ciudad} con codigo postal {codPostal}")
    navegador = webbrowser.open("https://meet.jit.si/telemedicina")
    
    

if __name__ == '__main':
    ubicacion()


