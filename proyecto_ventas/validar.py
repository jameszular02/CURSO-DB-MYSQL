'''
Validaciones de entrada para el mantenimiento de la tabla ventas
(base de datos meat_to_eat)
'''

import re
from datetime import datetime


def validar_entero(valor):
    '''Enteros positivos: ventUsuario, ventCantidad, idProductos'''
    return valor.strip().isdigit()


def validar_decimal(valor):
    '''Números con hasta 2 decimales: ventPrecio, ventImpuesto'''
    return bool(re.fullmatch(r"\d+(\.\d{1,2})?", valor.strip()))


def validar_fecha(fecha, formato='%Y-%m-%d'):
    '''Fecha en formato YYYY-MM-DD: ventFecha'''
    try:
        datetime.strptime(fecha.strip(), formato)
        return True
    except ValueError:
        return False


def validar_pago(pago):
    '''Solo "credito" o "contado": ventPago'''
    return pago.strip().lower() in ('credito', 'contado')


def validar_id_cliente(id_cliente):
    '''idCliente es varchar(18): alfanumérico, hasta 18 caracteres'''
    return bool(re.fullmatch(r"[A-Za-z0-9]{1,18}", id_cliente.strip()))


def validar_texto(texto):
    '''Solo letras y espacios: para saludar/despedirse por nombre'''
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ' ]+", texto.strip()))
