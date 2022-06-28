#por aitageo

#import  curses #para poner o eliminar el cursor de la terminal
#stdscr = curses.initscr()
import time
from db import Connect  
from mysql.connector import Error  #modulo que da conexion a mysql o phpmyadmin
import functions #se importa el archivo de funciones
import os

import sys
import signal
from colorama import *
init(convert = True)


def main():
    continued = True
    #curses.curs_set()
    os.system("cls")
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
                
#funcion para salir presionando el 5 usando el modulo system       
def exit():
    print(Fore.RED +"\n[*]Saliendo...\n")
    time.sleep(1)
    os.system("cls")
    sys.exit()
        



def handler_functions(option):
    obconnect = Connect()
    if option == 1:
        products = functions.get_data_products()
        try:
            obconnect.create_products(products)
            
        except:
            print("Ha ocurrido un error")
            
            
    elif option == 2:
        try:
            products = obconnect.show_products()
            if len(products)> 0:
                functions.list_products(products)
            else:
                print("No se encontro nada")    
        except Error as er:
            print("No se encontro nada" + er) 
    
    
    elif option == 3:
        try:
            products = obconnect.update_products()
            if len(products)> 0:
                functions.list_products(products)
            else:
                print("No se encontro nada")    
        except Error as er:
            print("No se encontro nada" + er) 
            
            
            
    elif option == 4:
        try:
            products = obconnect.show_products()
            if len(products)> 0:
                functions.list_products(products)
                codigo = functions.delete_data_products(products)
                try:
                    obconnect.delete_products(codigo,products)
                    time.sleep(1)
                    products = obconnect.show_products()
                    functions.list_products(products)
                    
                except:
                    print("No se pudo borrar")    
            else:
                print("No se encontro nada")    
        except Error as er:
            print("No se encontro nada" + er)                      
                




    
    
#Manejador de señales de interrupcion     
def handler(a,b):
    print(Fore.LIGHTRED_EX  + "\n\n[*]Saliendo....\n")
    sys.exit()

signal.signal(signal.SIGINT,handler)    
    
    
    
if __name__ == "__main__":
    main()    
    