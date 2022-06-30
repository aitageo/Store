#por aitageo

import time
import colorama 
from  colorama import*
init(convert= True)

def list_products(products):
    print(Fore.YELLOW + "Products")
    contador=1
    for i in products:
        data = "{0}. Codigo = {1} | Cantidad = {2} | Nombre = {3}"
        print(data.format(contador, i[0],i[2],i[1]))
        contador+=1
        print(Fore.YELLOW +"------------")
        
        
        
def get_data_products():
    nombre = ""
    cantidad = 0
    cantidad_valid = False
    while not cantidad_valid:
        try:
            nombre = input("Ingrese el nombre: ")
            cantidad = int(input("Ingresa la cantidad: "))
            cantidad_valid = True
        except ValueError:
            print("Valor incorrecto")
    products = (nombre,cantidad)#tupla con los datos
    return products 



def update_data_products(products):
    list_products(products)
    nombre = ""
    cantidad = 0
    codigo = int(input("Ingresa el codigo del producto: "))
    for i in products:
        if i[0] == codigo:
            optionRight = False
            while not optionRight:
                try:
                    nombre = input("ingresa el nuevo nombre: ")
                    cantidad =  int(input("ingresa la nueva cantidad: ")) 
                    optionRight = True     
                except ValueError:
                    print("error")
            products = (nombre,cantidad,codigo)
            time.sleep(2)
            return products
           

 
def delete_data_products(products):
    try:
        codigo = int(input(Fore.RED + "Ingresa el codigo del producto a Eliminar: "))
        return codigo
    except ValueError:
        print("valor erroneo")        
    
           