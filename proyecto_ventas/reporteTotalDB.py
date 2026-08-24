'''
Reporte general de la tabla ventas de la base de datos meat_to_eat.
Se implementa en archivo aparte del principal, tal como pide el enunciado.
'''

from connectorBD import *


def reporte_general():
    cur = cnn.cursor()
    cur.execute('''SELECT * FROM ventas''')
    datos = cur.fetchall()  # fetchall() trae todos los registros de la consulta
    if len(datos) != 0:
        for fila in datos:
            print('ID Venta: ', fila[0])
            print('Usuario (cajero): ', fila[1])
            print('Precio: ', fila[2])
            print('Impuesto: ', fila[3])
            print('Total: ', fila[4])
            print('Cantidad: ', fila[5])
            print('Fecha: ', fila[6])
            print('Pago: ', fila[7])
            print('ID Cliente: ', fila[8])
            print('ID Producto: ', fila[9])
            print('-----------------------------')
    else:
        print('No se encontraron ventas registradas')
    print(f'**   Cantidad de Ventas: {len(datos)}  **')
    print('-----------------------------')
    print('Fin del reporte')
    cur.close()
