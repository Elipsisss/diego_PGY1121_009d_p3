import funciones as fn 
import numpy
import msvcrt
import time 
import os 


while True:
    print("""MENÚ"
    1. Ver habitaciones
    2. Registrarse
    3. Total a pagar
    4. Salir""")
    opcion = fn.validacion_opc()
    
    if opcion == 1:
        fn.ver_sala()
    elif opcion == 2:
        fn.validacion_registro()
    elif opcion == 3:
        fn.validar_dias()
    else:
        break
