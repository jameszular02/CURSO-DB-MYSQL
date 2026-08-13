# función validar enteros, texto y flotantes, fechas y correos

#funcion que valida solo letras
def valletras(nom):
    while True: 
        if nom.isalpha():
            return(nom)
        else:
            print()
            nom = input('Error, letras unicamente')
