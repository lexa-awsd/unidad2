Edades = {
    "Brayan": 25,
    "Luis": 30,
    "José": 22
}
print("Edad de Luis:", Edades["Luis"])    
Edades["Brayan"] = 28
print("\nDespués de añadir a Brayan:")
print(Edades)                               

Edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(Edades)                              

del Edades["José"]
print("\nDespués de eliminar a José:")
print(Edades)                               

print("\nRecorriendo el diccionario:")
for Nombre, Edad in Edades.items():         
    print(f"{Nombre} tiene {Edad} años")