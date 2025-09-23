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
    }
}

Isbn = "978-84-376-0494-7"
Info_libro = Biblioteca.get(Isbn)          
print("\nInformación del libro:", Info_libro)
