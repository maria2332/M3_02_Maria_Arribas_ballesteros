"""
Identificar los errores en los siguiente bloques de código y evaluarlos con excepciones especificas para evitar errores no controlados en nuestros programas. Añadem mensajes explicativos para el usuario.
Nota: Se tienen que evaluar excepciones concretas, no hacer referencia a Exception sin más.
4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = "2" + 10
"""

from ast import main 

def error_suma_string(*args):
    suma = 0
    for args in args:
        try:
            suma += args 
        except TypeError:
            print ("No se puede sumar un string a un int/float")     
    return 

error_suma_string("2", 10)

if __name__ == "__main__":
    main()