import os
import json
import requests
import re

def limpiar_titulo(titulo, longitud_maxima=100):
    # Reemplazar espacios con barras bajas
    titulo_limpio = titulo.replace(' ', '_')
    # Eliminar caracteres especiales y espacios adicionales del título
    titulo_limpio = re.sub(r'[^\w\s]', '', titulo_limpio)
    titulo_limpio = re.sub(r'\s+', ' ', titulo_limpio).strip()
    # Truncar el título si excede la longitud máxima
    if len(titulo_limpio) > longitud_maxima:
        titulo_limpio = titulo_limpio[:longitud_maxima]
    return titulo_limpio

def buscar_libros(parametros_busqueda):
    url = 'http://openlibrary.org/search.json'
    libros_encontrados = []

    try:
        # Creamos la carpeta json si no existe
        if not os.path.exists('json'):
            os.makedirs('json')

        for genero in parametros_busqueda:
            # Pasamos como parámetros los géneros literarios
            parametros = {'q': genero}

            # Realizamos una petición a la url de la página
            response = requests.get(url, params=parametros)
            data = response.json()

            if response.status_code == 200:
                # Iteramos sobre todas las páginas de resultados
                for pagina in range(1, (data['numFound'] // 100) + 2):  
                    parametros['page'] = pagina
                    response = requests.get(url, params=parametros)

                    try:
                        data = response.json()
                    except json.JSONDecodeError as e:
                        print(f"Error al decodificar JSON en la página {pagina} para el género {genero}: {e}")
                        continue
                    
                    # Cogemos los archivos json y los guardamos con el nombre del título
                    if response.status_code == 200:
                        if data['docs']:
                            for libro in data['docs']:
                                titulo = libro.get('title', 'No disponible')
                                titulo_limpio = limpiar_titulo(titulo)
                                with open(f'json/{titulo_limpio}.json', 'w', encoding='utf-8') as file:
                                    json.dump(libro, file, indent=4)
                                    libros_encontrados.append(libro)

        # Contamos el número de archivos descargados
        numero_archivos_descargados = len(os.listdir('json'))
        print(f"Se encontraron un total de {numero_archivos_descargados} archivos en la carpeta 'json'.")

        return libros_encontrados

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

# Ejemplo de uso con distintos géneros literarios
parametros_busqueda = ['science fiction', 'action', 'thriller', 'horror']
buscar_libros(parametros_busqueda)
