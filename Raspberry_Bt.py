# Librerias Importadas 

import gpiozero
import Localizacion
import shutDown_RP

boton = gpiozero.Button(4) #Definicion del pin del boton

def ejRaspberry():
    
    bandera = True
    bandera_2 = True
    
    while bandera:
        inicio = boton.wait_for_press() #Espera al que boton sea presionado para continuar con el codigo
        try:
            if (boton and bandera_2 == True ):
                
             #Consume la api de la Ubicación , genera un archivo JSON
                print ("seccion iniciada")
                Localizacion.ubicacion()
                bandera = True # nos vuelve a ejecutar el while para pasar a elif
                bandera_2 = False # poniendo esta bandera en falso nos deja ejecutar el elif 
                
                print(boton) #imprime estado del boton
                
            
            elif(boton != bandera_2):
                
                print('seccion terminada')
                #bandera_2= True
                print("El dispositivo se apagara")
                #shutDown_RP.apagar() #Ejecuta el modulo de apagar la Raspberry
                print(boton) #imprime estado del boton 
                break

        except:
            print("error inesperado")
            break
        bandera = True

if __name__ == '__main':
    ejRaspberry()