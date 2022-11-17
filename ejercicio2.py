"""
Identificar los errores en los siguiente bloques de código y evaluarlos con excepciones especificas para evitar errores no controlados en nuestros programas. Añadem mensajes explicativos para el usuario.
Nota: Se tienen que evaluar excepciones concretas, no hacer referencia a Exception sin más.
2) Código a evaluar:
lista = [4, 7, 30, 23, 5]
lista[10]
"""

from ast import main 

def error_elemento_fuera_lista(lista, elemento_lista):
    try:
        elemento = lista[elemento_lista]
        return elemento 
    except IndexError:
        print ("El elemento {} no se encuentra en la lista, ya que la lista solo contiene {} elemento".format(elemento_lista, len(lista)))     
    return 

error_elemento_fuera_lista([4, 7, 30, 23, 5], 10)

if __name__=="__main__":
    main()