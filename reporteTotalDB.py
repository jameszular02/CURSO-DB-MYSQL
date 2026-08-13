'''
Mantenimiento en una base de datos XAMPP phpMyAdmin, base zapatería 
Tablas: clientes, productos, proveedores y ventas
Programa de reporte general de ventas.
***** Estamos construyendo el reporte general ***
alt + 200-201-205 --> ╚ ╔ ═ ╗
'''

#llamados de archivo de sistema
from connectorBD import* #importar el archivo de conexion
from validar import* #importar el archivo de validacion 
from datetime import datetime #importar la libreria de fecha y hora
import os #para limpiar pantalla en Linux (Codespaces) y Windows

def limpiar():
    os.system('clear' if os.name != 'nt' else 'cls')

#funcion consulta general
def consulta_general():
    cur = cnn.cursor()
    cur.execute('''SELECT * FROM clientes''')
    datos = cur.fetchall() #con fetchall() se obtiene todos los registros de la consulta
    if len(datos) != 0:
        for campos in datos:
            print('ID Cliente: ', campos[0])
            print('Nombre: ', campos[1])
            print('Primer Apellido: ', campos[2])
            print('Segundo Apellido: ', campos[3])
            print('Número de móvil: ', campos[4])
            print('Correo electrónico: ', campos[5])
            print('Dirección: ', campos[6])
            fecha = campos[7]  # ya es un objeto date/datetime, no hace falta volver a parsearlo
            print('Fecha de Registro: ', fecha)
            print('Estado: ', campos[8])
            print('-----------------------------')
    else:
        print('No se encontraron resultados')
    print(f'**   Cantidad de Clientes: {len(datos)}**')
    print('-----------------------------')
    print('Fin de la consulta')
    cur.close()

    
