#Van a crear una lista vacia con su nombre y van a crear 5 elementos con input:
#(Nombre, preparatoria, lugar de residencia, edad, carrera)
print ("Lista de Axel:")
lista_Axel = []

nombre = input("Nombre: ")
lista_Axel.append(nombre)

preparatoria = input("Preparatoria: ")
lista_Axel.append(preparatoria)

lugar_residencia = input("Lugar de Residencia: ")
lista_Axel.append(lugar_residencia)

edad = input("Edad: ")
lista_Axel.append(edad)

carrera = input("Carrera: ")
lista_Axel.append(carrera)

print("\n📌 Tu lista es:")
for elementos in lista_Axel:
    print(f"- {elementos}")

print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/
