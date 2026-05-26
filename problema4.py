peliculas=[
    ["Inception", 2010, 9, "Ciencia Ficción"],
    ["Interstellar", 2014, 9, "Ciencia Ficción"],
    ["Coco", 2017, 8, "Animación"],
    ["Avengers: Infinity War", 2018, 9, "Acción"],
    ["Parasite", 2019, 9, "Drama"],
    ["Tenet", 2020, 7, "Acción"],
    ["Encanto", 2021, 8, "Animación"],
    ["Top Gun: Maverick", 2022, 9, "Acción"],
    ["The Whale", 2022, 8, "Drama"],
    ["Oppenheimer", 2023, 9, "Drama"]
    
]
def contar_populares_recientes (lista, umbral_calificacion, anio_limite):
    contador = 0
    for pelicula in lista:
        titulo, anio, calificacion, genero = pelicula
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1
    return contador

resultado = contar_populares_recientes(peliculas, 8, 2020)
print("Número de títulos populares y recientes:", resultado)