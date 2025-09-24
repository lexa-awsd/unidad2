#Funcion para mostrar menu principal al usuario
def mostrar_menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    
#Funcion para saludar
def opcion_saludar() -> None:
    nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {nombre}! Bienvenido/a.")

#Funcion para calcular la suma de dos numeros
def opcion_suma() -> None:
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    except ValueError:
        print(" Debes introducir valores numéricos.")

#Funcion para mostrar la tabla de multiplcar del 5
def opcion_tabla() -> None:
    numero = 5
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")

#Bucle que imprime la fucnion seleccionada por el usuario, pero la condicion simpre sera verdadera
#solo si el usuario selecciona 0 sera falsa y se detendra.
# ---------- Bucle principal ----------
continuar = True              
while continuar:
    mostrar_menu()             
    eleccion = input("Elige una opción: ").strip()

    if eleccion == "1":
        opcion_saludar()
    elif eleccion == "2":
        opcion_suma()
    elif eleccion == "3":
        opcion_tabla()
    elif eleccion == "0":
        print("\n ¡Hasta luego!")
        continuar = False
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")