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
            
            
     #funcion para mostrar los productos existentes       
    def show_products(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM productos")
                result = cursor.fetchall()
                return result       

            except Error as ex:
                print(Fore.RED + f"No hay nada para mostrar{ex}")
                
                
    def create_products(self,products):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "INSERT INTO productos(id,nombre,cantidad) values(id,'{0}','{1}')"
                cursor.execute(query.format(products[0],products[1]))
                self.conexion.commit()
                print("\nDatos guardados exitosamente")
            except Error as ex:
                print(Fore.RED + f"\nNo hay nada para mostrar{ex}")  
                
                
                
    def update_products(self,products):
        if self.conexion.is_connected():
            nombre,cantidad,codigo = products
            try:
                cursor = self.conexion.cursor()
                updates = f"UPDATE productos SET nombre='{nombre}',cantidad='{cantidad}' WHERE id={codigo}"
                cursor.execute(updates)
                self.conexion.commit()#se confirman los datos
                print(Fore.BLUE + "Datos Actualizados")
                
            except Error as ex:
                print(Fore.RED + f"No hay nada para mostrar  {ex}") 
               
                
                
                
    def delete_products(self,codigo,products):
        if self.conexion.is_connected():
            for i in products:
                if i[0] == codigo:
                    try:
                        cursor = self.conexion.cursor()
                        deletes = "DELETE FROM productos where id = '{0}'"
                        cursor.execute(deletes.format(codigo))
                        self.conexion.commit()
                        print("Producto eliminado")    
                    except Error as ex:
                        print(Fore.RED + f"No hay nada para mostrar  {ex}")              
                                  
                    










 
    
    
    




 