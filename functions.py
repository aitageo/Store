#por aitageo

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
    nombre = input("Ingrese el nombre: ")
    cantidad_valid = False
    while(cantidad_valid):
        try:
            cantidad = int(input("Ingresa la cantidad: "))
            cantidad_valid = True
        except ValueError:
            print("Valor incorrecto")
    
    products = (nombre,cantidad)#tupla con los datos
    return products 




def delete_data_products(products):
    try:
        codigo = int(input(Fore.RED + "Ingresa el codigo del producto a Eliminar: "))
        for i in products:
            if codigo == i:
                products.pop(codigo)
        return codigo
    except ValueError:
        print("valor erroneo")        
    
           