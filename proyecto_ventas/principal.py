'''
PROYECTO II - INTRODUCCION A PROGRAMACION - Universidad Creativa
Prof. Mauricio Torres Solano

Enunciado (resumido): crear un programa que implemente el mantenimiento
completo (insertar, consultar, modificar, eliminar y reporte general) de
la tabla `ventas` de la base de datos "meat_to_eat", usando la llave
primaria ventId como guía para las operaciones SQL en Python.
'''

# llamados de archivos del sistema
from connectorBD import *      # importar el archivo de conexión
from validar import *          # importar el archivo de validación
from reporteTotalDB import *   # importar el archivo de reporte general
from datetime import datetime  # importar la librería de fecha y hora
import os                      # para limpiar pantalla en Linux (Codespaces) y Windows


# funcion limpiar pantalla
def limpiar():
    os.system('clear' if os.name != 'nt' else 'cls')


# funcion encabezado
def encabezado():
    titulo = '''
    ╔══════════════════════════════════════════════════════════════╗
    ║                MANTENIMIENTO SISTEMA - VENTAS                ║
    ║                  Base de Datos meat_to_eat                   ║
    ╚══════════════════════════════════════════════════════════════╝
    '''
    print(titulo)


# funcion menu
def menu():
    opciones = '''
    ╔══════════════════════════════════════════════════════════════╗
    ║   1: => Insertar Venta                                        ║
    ║   2: => Consultar Venta                                       ║
    ║   3: => Modificar Venta                                       ║
    ║   4: => Eliminar Venta                                        ║
    ║   5: => Reporte General                                       ║
    ║   6: => Salir                                                 ║
    ╚══════════════════════════════════════════════════════════════╝
    '''
    print(opciones)


# funcion saludar (se ejecuta antes del menu principal)
def saludar():
    limpiar()
    nombre = input('¡Bienvenido/a al sistema de ventas! Ingrese su nombre: ')
    while not validar_texto(nombre):
        nombre = input('Error, ingrese solo letras. Ingrese su nombre: ')
    print(f'\nHola, {nombre}. Cargando el sistema...\n')
    input('Presione Enter para continuar...')
    return nombre


# funcion despedirse (se ejecuta al salir, por nombre)
def despedirse(nombre):
    print(f'\nGracias por usar el sistema, {nombre}. ¡Que tenga un excelente día!\n')


# funcion salir (verifica con el usuario la decision de salir)
def salir():
    confirmar = input('¿Seguro que desea salir? (s/n): ').strip().upper()
    if confirmar == 'S':
        return True
    print('Cancelado, volviendo al menú...')
    return False


# funcion auxiliar para mostrar una venta (evita repetir el bloque de prints)
def mostrar_venta(fila):
    print('** Registro de venta número: ', fila[0])
    print('Usuario (cajero): ', fila[1])
    print('Precio: ', fila[2])
    print('Impuesto: ', fila[3])
    print('Total: ', fila[4])
    print('Cantidad: ', fila[5])
    print('Fecha: ', fila[6])
    print('Pago: ', fila[7])
    print('ID Cliente: ', fila[8])
    print('ID Producto: ', fila[9])


# funcion insertar venta
def insertar_venta():
    limpiar()
    print('**** INSERTAR VENTA ****')
    print('*****************************')
    print('Ingrese los datos de la venta')
    print('(el ID de venta lo asigna la base de datos automáticamente)\n')

    usuario = input('Ingrese el número de cajero: ')
    while not validar_entero(usuario):
        usuario = input('Error, solo números. Ingrese el número de cajero: ')
    usuario = int(usuario)

    precio = input('Ingrese el precio de venta: ')
    while not validar_decimal(precio):
        precio = input('Error, ingrese un número válido. Precio: ')
    precio = float(precio)

    impuesto = input('Ingrese el impuesto de venta: ')
    while not validar_decimal(impuesto):
        impuesto = input('Error, ingrese un número válido. Impuesto: ')
    impuesto = float(impuesto)

    cantidad = input('Ingrese la cantidad de producto vendido: ')
    while not validar_entero(cantidad):
        cantidad = input('Error, solo números. Cantidad: ')
    cantidad = int(cantidad)

    total = round(precio * cantidad + impuesto, 2)
    print(f'Total calculado (precio x cantidad + impuesto): {total}')

    fecha = input('Ingrese la fecha de venta (YYYY-MM-DD): ')
    while not validar_fecha(fecha):
        fecha = input('Error, formato debe ser YYYY-MM-DD. Fecha: ')
    fechaB = datetime.strptime(fecha, '%Y-%m-%d')

    pago = input('Ingrese el tipo de pago (credito/contado): ').strip().lower()
    while not validar_pago(pago):
        pago = input('Error, escriba "credito" o "contado". Tipo de pago: ').strip().lower()

    id_cliente = input('Ingrese el ID del cliente: ')
    while not validar_id_cliente(id_cliente):
        id_cliente = input('Error, máximo 18 caracteres alfanuméricos. ID Cliente: ')

    id_producto = input('Ingrese el ID del producto: ')
    while not validar_entero(id_producto):
        id_producto = input('Error, solo números. ID Producto: ')
    id_producto = int(id_producto)

    # proceso para insertar datos en la tabla ventas (consulta parametrizada)
    cur = cnn.cursor()
    sql = '''INSERT INTO ventas
             (ventUsuario, ventPrecio, ventImpuesto, ventTotal,
              ventCantidad, ventFecha, ventPago, idCliente, idProductos)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    valores = (usuario, precio, impuesto, total, cantidad, fechaB, pago, id_cliente, id_producto)
    cur.execute(sql, valores)
    cnn.commit()
    nuevo_id = cur.lastrowid
    cur.close()
    print(f'\n✔ Venta registrada correctamente con ID {nuevo_id}.')


# funcion consultar venta
def consultar_venta():
    limpiar()
    print('**** CONSULTAR VENTA ****')
    print('*****************************')
    consulta = input('Ingrese el ID de la venta a consultar: ')
    while not validar_entero(consulta):
        consulta = input('Error, solo números. ID de venta: ')

    cur = cnn.cursor()
    cur.execute('''SELECT * FROM ventas WHERE ventId = %s''', (consulta,))
    datos_db = cur.fetchall()  # fetchall() para traer todos los datos de la consulta
    if len(datos_db) != 0:
        for fila in datos_db:
            mostrar_venta(fila)
    else:
        print('No se encontraron resultados')
    cur.close()


# funcion modificar venta
def modificar_venta():
    limpiar()
    print('**** MODIFICAR VENTA ****')
    print('*****************************')
    consulta = input('Ingrese el ID de la venta a modificar: ')
    while not validar_entero(consulta):
        consulta = input('Error, solo números. ID de venta: ')

    cur = cnn.cursor()
    cur.execute('''SELECT * FROM ventas WHERE ventId = %s''', (consulta,))
    datos_db = cur.fetchall()
    if len(datos_db) != 0:
        for fila in datos_db:
            mostrar_venta(fila)

        respuesta = input('¿Desea modificar esta venta? (s/n): ').strip().upper()
        if respuesta == 'S':
            print('\nIngrese los nuevos datos de la venta')
            usuario = input('Nuevo número de cajero: ')
            while not validar_entero(usuario):
                usuario = input('Error, solo números. Número de cajero: ')
            usuario = int(usuario)

            precio = input('Nuevo precio de venta: ')
            while not validar_decimal(precio):
                precio = input('Error, ingrese un número válido. Precio: ')
            precio = float(precio)

            impuesto = input('Nuevo impuesto de venta: ')
            while not validar_decimal(impuesto):
                impuesto = input('Error, ingrese un número válido. Impuesto: ')
            impuesto = float(impuesto)

            cantidad = input('Nueva cantidad de producto: ')
            while not validar_entero(cantidad):
                cantidad = input('Error, solo números. Cantidad: ')
            cantidad = int(cantidad)

            total = round(precio * cantidad + impuesto, 2)
            print(f'Total recalculado: {total}')

            fecha = input('Nueva fecha de venta (YYYY-MM-DD): ')
            while not validar_fecha(fecha):
                fecha = input('Error, formato debe ser YYYY-MM-DD. Fecha: ')
            fechaB = datetime.strptime(fecha, '%Y-%m-%d')

            pago = input('Nuevo tipo de pago (credito/contado): ').strip().lower()
            while not validar_pago(pago):
                pago = input('Error, escriba "credito" o "contado". Tipo de pago: ').strip().lower()

            id_cliente = input('Nuevo ID de cliente: ')
            while not validar_id_cliente(id_cliente):
                id_cliente = input('Error, máximo 18 caracteres alfanuméricos. ID Cliente: ')

            id_producto = input('Nuevo ID de producto: ')
            while not validar_entero(id_producto):
                id_producto = input('Error, solo números. ID Producto: ')
            id_producto = int(id_producto)

            cur2 = cnn.cursor()
            sql = '''UPDATE ventas SET ventUsuario=%s, ventPrecio=%s, ventImpuesto=%s,
                     ventTotal=%s, ventCantidad=%s, ventFecha=%s, ventPago=%s,
                     idCliente=%s, idProductos=%s WHERE ventId=%s'''
            valores = (usuario, precio, impuesto, total, cantidad, fechaB, pago,
                       id_cliente, id_producto, consulta)
            cur2.execute(sql, valores)
            cnn.commit()
            cur2.close()
            print(f'\n✔ Venta #{consulta} actualizada correctamente.')
        else:
            print('Modificación cancelada.')
    else:
        print('No se encontraron resultados')
    cur.close()


# funcion eliminar venta
def eliminar_venta():
    limpiar()
    print('**** ELIMINAR VENTA ****')
    print('*****************************')
    consulta = input('Ingrese el ID de la venta a eliminar: ')
    while not validar_entero(consulta):
        consulta = input('Error, solo números. ID de venta: ')

    cur = cnn.cursor()
    cur.execute('''SELECT * FROM ventas WHERE ventId = %s''', (consulta,))
    datos_db = cur.fetchall()  # fetchall() para traer todos los datos de la consulta
    if len(datos_db) != 0:
        for fila in datos_db:
            mostrar_venta(fila)
        respuesta = input('¿Desea eliminar esta venta? (s/n): ').strip().upper()
        if respuesta == 'S':
            cur.execute('''DELETE FROM ventas WHERE ventId = %s''', (consulta,))
            cnn.commit()
            print(f'\n✔ Venta #{consulta} eliminada correctamente.')
        else:
            print('Eliminación cancelada.')
    else:
        print('No se encontraron resultados')
    cur.close()


# funcion principal: muestra el menu y despacha segun la opcion elegida,
# controlada por un bucle que verifica con el usuario la decision de salir
def main():
    nombre = saludar()
    continuar = True

    while continuar:
        limpiar()
        encabezado()
        menu()
        opcion = input('Seleccione una opción: ')
        match opcion:
            case '1':
                insertar_venta()
            case '2':
                consultar_venta()
            case '3':
                modificar_venta()
            case '4':
                eliminar_venta()
            case '5':
                reporte_general()
            case '6':
                if salir():
                    continuar = False
            case _:
                print('Opción no válida, intente de nuevo.')
        if continuar:
            input('\nPresione Enter para continuar...')

    despedirse(nombre)
    cnn.close()  # cierra la conexión de la base de datos


if __name__ == '__main__':
    main()
