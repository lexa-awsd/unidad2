import json

Biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
    "978-84-663-2158-1": {
        "título": "Ficciones",
        "autor": ["Jorge Luis Borges"],
        "géneros": ["Fantasía", "Cuento breve", "Literatura de ideas"]
    },
    "978-968-16-1197-8": {
        "título": "Pedro Páramo",
        "autor": ["Juan Rulfo"],
        "géneros": ["Realismo mágico", "Novela corta", "Literatura mexicana"]
    },
    "978-950-07-0002-7": {
        "título": "Rayuela",
        "autor": ["Julio Cortázar"],
        "géneros": ["Novela", "Boom latinoamericano"]
    }
}

Isbn = "978-950-07-0002-7"
Info_libro = Biblioteca.get(Isbn)
print("\nInformación del libro:", Info_libro)

# Convertir el diccionario completo a JSON (útil para guardar en archivo)
json_str = json.dumps(Biblioteca, indent=2, ensure_ascii=False)
print("\nBiblioteca completa en formato JSON:\n", json_str)
