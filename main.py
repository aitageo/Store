#por aitageo

from db import Connect
from mysql.connector import Error
import functions

import sys
import signal
from colorama import *
init(convert = True)


def main():
    continued = True
    while(continued):
        optionCorrecta = False
        while (not optionCorrecta):
            print(Fore.YELLOW + "\n=====Menu Principal=====\n")
            print(Fore.BLUE + "1) Crear Productos")
            print("2) Listar Productos")
            print("3) Editar Productos")
            print(Fore.RED + "4) Eliminar Productos")
            print(Fore.RED + "5) Salir")
            print(Fore.WHITE + "")
            try:
                option = int(input("ingrese una opcion: "))
                if option < 1 or option > 5:
                    print(Fore.RED + "opcion incorrecta")
                elif option == 5:
                    optionCorrecta = True
                    continued = False
                    exit()
                else: 
                    handler_functions(option)    
                    
                
            except ValueError:
                print(Fore.RED + "Valores erroneos")
            except BufferError:
                print("Demasiados valores")    
                
       
def exit():
    print(Fore.RED +"\n[*]Saliendo...\n")
    sys.exit()    



def handler_functions(option):
    obconnect = Connect()
    try:
        products = obconnect.show_products()
        if len(products)> 0:
            pass
    except Error as er:
        print("No se encontro nada" + er)

    if option == 2:
        functions.list_products(products) 




    
    
#Manejador de señales de interrupcion     
def handler(a,b):
    print(Fore.LIGHTRED_EX  + "\n\n[*]Saliendo....\n")
    sys.exit()

signal.signal(signal.SIGINT,handler)    
    
    
    
if __name__ == "__main__":
    main()    
    