'''
Mantenimiento en una base de datos XAMPP MariaDb, base labuenataza 
Tabla: Ventas
Versión 1 
***** 
se implemento inserción, consulta, actualización y borrado de venta
***** 
alt + 186-187-200-201-205 = ╚ ╔ ═ 
https://elcodigoascii.com.ar/ 
'''


#llamados de archivo de sistema
from connectorBD import* #importar el archivo de conexion
from validar import* #importar el archivo de validacion
from reporteTotalDB import* #importar el archivo de reporte total
from datetime import datetime #importar la libreria de fecha y hora
import mysql.connector #importar la libreria de mysql
import math
import subprocess #subprocess.run(["ls", "-l"]) #para ejecutar comandos de consola
import os #para limpiar pantalla en Linux (Codespaces) y Windows

#funcion limpiar pantalla
def limpiar():
    os.system('clear' if os.name != 'nt' else 'cls')
    return()

#funcion encabezado
def encabezado():
    fecha = datetime.now()
    print(f'* {fecha.day}-{fecha.month}-{fecha.year}')
    print('***************************')
    titulo = '''
    ╔══════════════════════════════════════════════════════════════╗
    ║                       MANTENIMIENTO SISTEMA                  ║
    ║                       Base De Datos                          ║
    ║                       Python - MySql v.1                     ║
    ╚══════════════════════════════════════════════════════════════╝
    '''
    print(titulo)
    return()

#funcion menu
def menu():
    opciones = ('''
     ╔══════════════════════════════════════════════════════════════╗
     ║                       MANTENIMIENTO SISTEMA                  ║
     ║                       Tabla Clientes                         ║
     ║                       Python - MySql v.1                     ║
     ║                       1: => Insertar Cliente                 ║
     ║                       2: => Consultar Clientes               ║
     ║                       3: => Actualizar Cliente               ║
     ║                       4: => Reporte Total Clientes           ║ 
     ║                       5: => Borrar Cliente                   ║
     ║                       6: => Salir                            ║
     ╚══════════════════════════════════════════════════════════════╝
    ''')
    print(opciones)
    return()

encabezado()
menu()

#funcion insertar venta
def insertar_cliente():
    limpiar()
    print('**** INSERTAR CLIENTE ****')
    print('*****************************')
    print('Ingrese los datos del cliente')
    #captura de datos
    id = input('Ingrese el ID del cliente: ')
    nombre = input('Ingrese el nombre del cliente: ')
    pape = input('Ingrese el primer apellido del cliente: ')
    sape = input('Ingrese el segundo apellido del cliente: ')
    movil = input('Ingrese el número de móvil del cliente: ')
    correo = input('Ingrese el correo electrónico del cliente: ')
    direccion = input('Ingrese la dirección fisica del cliente: ')
    fecha = input('Ingrese la fecha de registro (YYYY-MM-DD): ')
    fechaB = datetime.strptime(fecha, '%Y-%m-%d')  # Convertir a formato de fecha   
    estado = input('Ingrese el estado del cliente (activo/inactivo): ')
    #proceso para insertar datos en la tabla clientes
    cur = cnn.cursor()
    sql = ('''INSERT INTO `clientes`(`cliId`, `cliNom`, `cliPape`, `cliSape`, `cliMovil`, 
           `cliCorreo`, `cliDireccion`, `cliFecReg`, `cliEstado`) 
            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(id, nombre, pape, sape, movil, correo, direccion, fechaB, estado))
    cur.execute(sql)
    cnn.commit()
    cur.close()

#funcion consultar cliente
def consultar_cliente():
    limpiar()
    print('**** CONSULTAR CLIENTE ****')
    print('*****************************')
    #captura de datos
    consulta = input('Ingrese el ID del cliente a consultar: ')
    cur = cnn.cursor()
    cur.execute('''SELECT * FROM `clientes` WHERE `cliId` = {}'''.format(consulta,))
    datos_db = cur.fetchall() #fetchall() para traer todos los datos de la consulta
    if len(datos_db) != 0:
        for campos in datos_db:
            print('** Registro de cleinte numero: ', campos[0])
            print('Nombre: ', campos[1])
            print('Primer Apellido: ', campos[2])
            print('Segundo Apellido: ', campos[3])
            print('Número de móvil: ', campos[4])
            print('Correo electrónico: ', campos[5])
            print('Dirección: ', campos[6])
            print('Fecha de Registro: ', campos[7])
            print('Estado: ', campos[8])
    else:
        print('No se encontraron resultados')
    cur.close()
    return()

encabezado()
menu()
#insertar_cliente()
consultar_cliente()
