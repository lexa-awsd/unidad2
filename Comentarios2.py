# ------------------------------------------------------------
# Demostración de comentarios y de la indentación en Python
# ------------------------------------------------------------

def saludo(nombre):
    """
    Función que devuelve un mensaje de bienvenida.
    Parámetro:
        nombre (str): nombre de la persona a saludar
    Retorna:
        str: mensaje de saludo
    """
    # El bloque siguiente está indentado 4 espacios
    mensaje = f"¡Hola, {nombre}!"
    return mensaje          # Comentario al final de la línea


def main():
    # Lista de nombres para probar la función
   nombres = ["Ana", "Luis", "María"]

    # Bucle for con su propio nivel de indentación
   for n in nombres:
        # Llamamos a la función saludo y mostramos el resultado
     print(saludo(n))   # Comentario corto al final

    # Ejemplo de error de indentación (comentado para que no rompa el programa)
    # if True:
    #print("Esto provocaría un IndentationError")   # <-- sin sangría

# Punto de entrada del script
if __name__ == "__main__":
    main()
