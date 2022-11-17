"""
Identificar los errores en los siguiente bloques de código y evaluarlos con excepciones especificas para evitar errores no controlados en nuestros programas. Añadem mensajes explicativos para el usuario.
Nota: Se tienen que evaluar excepciones concretas, no hacer referencia a Exception sin más.
1) Código a evaluar:
numero = 7/0
"""

from ast import main 

def error_division_0(numerador,denominador):
    try: 
        numero = numerador/denominador
        return numero 
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    return

error_division_0(7,0)

if __name__=="__main__":
    main()


