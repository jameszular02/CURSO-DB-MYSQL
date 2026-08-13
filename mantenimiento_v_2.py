'''
Mantenimiento en una base de datos XAMPP MariaDb, base labuenataza 
Tabla: Ventas
Versión 2
***** 
se implemento inserción, consulta, actualización y borrado de la tabla de clientes
10/08/2026
Se a implemento con exito el reporte general en la tabla de clientes
10/08/2026
respaldo de la tabla clientes
12/08/2026
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
    ║                       Python - MySql v.2                     ║
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
            print('** Registro de cliente numero: ', campos[0])
            print('Nombre: ', campos[1])
            print('Primer Apellido: ', campos[2])
            print('Segundo Apellido: ', campos[3])
            print('Número de móvil: ', campos[4])
            print('Correo electrónico: ', campos[5])
            print('Dirección: ', campos[6])
            fecha = campos[7]  # ya es un objeto date/datetime, no hace falta volver a parsearlo
            print('Fecha de Registro: ', fecha)
            print('Estado: ', campos[8])
    else:
        print('No se encontraron resultados')
    cur.close()
    return()


#funcion actualizar cliente
def actualizar_cliente():
    limpiar()
    print('**** ACTUALIZAR CLIENTE ****')
    print('*****************************')
    consulta = input('Ingrese el ID del cliente a actualizar: ')
    cur = cnn.cursor()
    cur.execute('''SELECT * FROM `clientes` WHERE `cliId` = {}'''.format(consulta,))
    datos_db = cur.fetchall()
    if len(datos_db) != 0:
        for campos in datos_db:
            print('** Registro de cliente numero: ', campos[0])
            print('Nombre: ', campos[1])
            print('Primer Apellido: ', campos[2])
            print('Segundo Apellido: ', campos[3])
            print('Número de móvil: ', campos[4])
            print('Correo electrónico: ', campos[5])
            print('Dirección: ', campos[6])
            fecha = campos[7]  # ya es un objeto date/datetime, no hace falta volver a parsearlo
            print('Fecha de Registro: ', fecha)
            print('Estado: ', campos[8])

        respuesta = input('¿Desea actualizar este cliente? (s/n): ')
        respuesta = respuesta.upper()
        if respuesta == 'S':
            print('Ingrese los nuevos datos del cliente')
            nombre = input('Ingrese el nuevo nombre del cliente: ')
            pape = input('Ingrese el nuevo primer apellido del cliente: ')
            sape = input('Ingrese el nuevo segundo apellido del cliente: ')
            movil = input('Ingrese el nuevo número de móvil del cliente: ')
            correo = input('Ingrese el nuevo correo electrónico del cliente: ')
            direccion = input('Ingrese la nueva dirección fisica del cliente: ')
            fecha = input('Ingrese la nueva fecha de registro (YYYY-MM-DD): ')
            fechaB = datetime.strptime(fecha, '%Y-%m-%d')  # Convertir a formato de fecha   
            estado = input('Ingrese el nuevo estado del cliente (activo/inactivo): ')
            cur = cnn.cursor()
            sql = ('''UPDATE `clientes` SET `cliNom`='{}',`cliPape`='{}',`cliSape`='{}',`cliMovil`='{}',
            `cliCorreo`='{}',`cliDireccion`='{}',`cliFecReg`='{}',`cliEstado`='{}' WHERE `cliId`={}'''.format(nombre, pape, sape, movil, correo, direccion, fechaB, estado, consulta))
            cur.execute(sql)
            cnn.commit()
            print(f'Registro de cliente #{campos[0]} actualizado correctamente.')
        else:
            print('Actualización cancelada.')



    else:
        print('No se encontraron resultados')
        print()
    cur.close()

#funcion borrar cliente
def borrar_cliente():
    limpiar()
    print('**** BORRAR CLIENTE ****')
    print('*****************************')
    #captura de datos
    consulta = input('Ingrese el ID del cliente a borrar: ')
    cur = cnn.cursor()
    cur.execute('''SELECT * FROM `clientes` WHERE `cliId` = {}'''.format(consulta,))
    datos_db = cur.fetchall() #fetchall() para traer todos los datos de la consulta
    if len(datos_db) != 0: 
        for campos in datos_db:
            print('** Registro de cliente numero: ', campos[0])
            print('Nombre: ', campos[1])
            print('Primer Apellido: ', campos[2])
            print('Segundo Apellido: ', campos[3])
            print('Número de móvil: ', campos[4])
            print('Correo electrónico: ', campos[5])
            print('Dirección: ', campos[6])
            fecha = campos[7]  # ya es un objeto date/datetime, no hace falta volver a parsearlo
            print('Fecha de Registro: ', fecha)
            print('Estado: ', campos[8])
        respuesta = input('¿Desea borrar este cliente? (s/n): ')
        respuesta = respuesta.upper()
        if respuesta == 'S':
            cur.execute('''DELETE FROM `clientes` WHERE `cliId` = {}'''.format(consulta,))
            cnn.commit()
            cur.close()
            print(f'Registro de cliente #{campos[0]} borrado correctamente.')
        else:
            print('Borrado cancelado.') 
    else:
        print()
        print('No se encontraron resultados')
    return()




#funcion principal: muestra el menu y despacha segun la opcion elegida
def ejecutar():
    while True:
        limpiar()
        encabezado()
        menu()
        opcion = input('Seleccione una opción: ')
        if opcion == '1':
            insertar_cliente()
        elif opcion == '2':
            consultar_cliente()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            consulta_general()
        elif opcion == '5':
            borrar_cliente()
        elif opcion == '6':
            print('Saliendo del sistema...')
            break
        else:
            print('Opción no válida, intente de nuevo.')
        input('\nPresione Enter para continuar...')

ejecutar()
consulta_general()
