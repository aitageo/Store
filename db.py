#por aitageo
import mysql.connector
from mysql.connector import Error
from colorama import *
init()



class Connect:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password="",
                database='tienda'
            )
        except Error as ex:
            print(Fore.RED + f"No se pudo conectar a la base de datos {ex}")
            
            
    def show_products(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM productos")
                result = cursor.fetchall()
                return result       

            except Error as ex:
                print(Fore.RED + f"No hay nada para mostrar{ex}");










 
    
    
    




 