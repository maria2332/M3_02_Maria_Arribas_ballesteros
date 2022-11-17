"""
Identificar los errores en los siguiente bloques de código y evaluarlos con excepciones especificas para evitar errores no controlados en nuestros programas. Añadem mensajes explicativos para el usuario.
Nota: Se tienen que evaluar excepciones concretas, no hacer referencia a Exception sin más.
3) Código a evaluar:
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
paises["alemania"]
"""

from ast import main 

def error_clave_fuera_diccionario(diccionario, clave):
    try:
        clave = diccionario[clave]
        return clave 
    except KeyError:
        print ("La clave {} no se encuentra en la lista y por tanto no se puede devolver su valor correspondiente".format(clave))     
    return 

error_clave_fuera_diccionario({ "españa":"español", "eeuu":"inglés", "italia":"italiano" } , "alemania")

if __name__=="__main__":
    main()