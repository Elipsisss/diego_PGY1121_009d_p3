
import numpy
import msvcrt
import time 
import os 

valor_dias = 15000
total = 0

lista_ruts = []
lista_nombre = []
lista_n_mascota = []
lista_filas = []
lista_columnas = []
lista_identificador = []

habitacion_canina = numpy.zeros((2,5), int)
def ver_sala ():
    print("HABITACIONES CANINAS\n")
    for x in range (2):
        print(f"FILA {x+1}", end=" ")
        for y in range (5):
            print(" ", habitacion_canina [x] [y], end=" ")
        print()
    print("Columna: 1   2   3   4   5")
    


def validacion_opc ():
    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if opcion in (1,2,3,4):
                return opcion
            else:
                print("ERROR, DEBES SELECCIONAR UNA OPCIÓN VALIDA")
        except:
            print("ERROR")
    


def validacion_registro():
    rut = validar_rut()
    nombre = validar_nombre()
    nombre_mascota = validar_n_mascota()
    ver_sala()
    fila = validar_fila()
    columna = validar_columna()


    lista_ruts.append(rut)
    lista_nombre.append(nombre)
    lista_n_mascota.append(nombre_mascota)
    lista_filas.append (fila)
    lista_columnas.append(columna)
    print("ASIENTO RESERVADO CON EXITO")
    return 
    

def validar_dias ():
    while True:
        try:
            dias = int(input("Ingrese cantidad de dias que se alojara su mascota: "))
            if dias >= 1:
                total = dias * valor_dias
                print(f"EL TOTAL A PAGAR ES: {total}")
                return dias
            else:
                print("ERROR, ALMENOS DEBE QUEDARSE UN DIA.")
        except:
            print("ERROR DEBES INGRESAR VALIDO")



def validar_n_mascota():
     while True:
        nombre_mascota = input("Ingrese el nombre de su mascota: ")
        if len(nombre_mascota.strip()) >= 3 and nombre_mascota.isalpha() and not nombre_mascota.isspace():
            return 
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")


   




def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha() and not nombre.isspace():
            return nombre
        else:
            print("El Nombre ingresado es muy corto (minimo debe tener 3 letras) o contiene caracteres no validos!")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese número columna( 1 - 10): "))
            if columna >= 1 and columna <= 10:
                return columna
            else:
                print("ERROR! COLUMNA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese número fila(1-2): "))
            if fila >= 1 and fila <= 2:
                return fila
            else:
                print("ERROR! FILA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
            
            






