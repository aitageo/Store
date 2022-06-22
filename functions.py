#por aitageo
import colorama 
from  colorama import*
init(convert= True)

def list_products(products):
    print(Fore.YELLOW + "Products")
    contador=1
    for i in products:
        data = "{0}. Codigo= {1} | Nombre= {2} | Cantidad= {3}"
        print(data.format(contador, i[0],i[1],i[2]))
        contador+=1
        print(Fore.YELLOW +"------------")